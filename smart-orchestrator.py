#!/usr/bin/env python3
"""
Paired Agent Orchestrator for Cursor
Manages Dev and Critic mode switches through handoff.md
"""

import time
from pathlib import Path
import sys
from datetime import datetime
import os

class CursorOrchestrator:
    def __init__(self, max_cycles=10):
        self.max_cycles = max_cycles
        self.cycle = 0
        self.project_root = Path.cwd()
        
        # Ensure required files exist
        self.ensure_files_exist()
        
        # Check if we need initialization
        self.needs_init = self.check_needs_initialization()
    
    def check_needs_initialization(self):
        """Check if project needs initialization from idea"""
        project_init = Path('project-init.md')
        goals = Path('goals.md')
        
        if project_init.exists():
            goals_content = self.read_file('goals.md')
            if '[Add your first goal]' in goals_content or '**Goal #1**: [' in goals_content:
                return True
        
        return False
    
    def ensure_files_exist(self):
        """Create required files if they don't exist"""
        required_files = {
            'goals.md': '# goals.md\n\n## Project Vision\n[Add your project vision]\n\n## Active Goal (Current Sprint)\n**Goal #1**: [Add your first goal]\n- **Success criteria**: \n  - [ ] [Add criteria]\n- **Tests required**: \n  - [ ] [Add test scenarios]\n- **Status**: NOT_STARTED\n',
            'scratchpad.md': '# scratchpad.md\n\n## Current Session\n**Date**: ' + datetime.now().strftime('%Y-%m-%d') + '\n**Active Goal**: Goal #1\n**Cycle**: 0\n\n## Recent Changes\n_None yet_\n',
            'handoff.md': '# handoff.md\n\n## Current Turn: DEV\n\n## Status: WORKING\n\n**Valid statuses**: WORKING | READY_FOR_REVIEW | NEEDS_WORK | APPROVED | BLOCKED\n',
            'critic-notes.md': '# critic-notes.md\n\n## Current Review Cycle\n**Reviewing**: Goal #1\n**Dev Cycle**: 0\n**Date**: ' + datetime.now().strftime('%Y-%m-%d') + '\n',
        }
        
        for filename, default_content in required_files.items():
            filepath = Path(filename)
            if not filepath.exists():
                print(f"📝 Creating {filename}...")
                filepath.write_text(default_content)
    
    def read_file(self, filename):
        """Read file content safely"""
        try:
            return Path(filename).read_text() if Path(filename).exists() else ""
        except Exception as e:
            print(f"⚠️ Error reading {filename}: {e}")
            return ""
    
    def write_handoff(self, turn):
        """Update the current turn in handoff.md"""
        try:
            content = self.read_file('handoff.md')
            if 'Current Turn: DEV' in content:
                updated = content.replace('Current Turn: DEV', f'Current Turn: {turn}')
            elif 'Current Turn: CRITIC' in content:
                updated = content.replace('Current Turn: CRITIC', f'Current Turn: {turn}')
            else:
                lines = content.split('\n')
                lines.insert(2, f'\n## Current Turn: {turn}\n')
                updated = '\n'.join(lines)
            
            Path('handoff.md').write_text(updated)
        except Exception as e:
            print(f"⚠️ Error updating handoff.md: {e}")
    
    def get_status(self):
        """Extract current status from handoff.md"""
        handoff = self.read_file('handoff.md')
        
        if 'Status: APPROVED' in handoff or '@approved' in handoff.lower():
            return 'APPROVED'
        elif 'Status: READY_FOR_REVIEW' in handoff or '@critic-review' in handoff.lower():
            return 'READY_FOR_REVIEW'
        elif 'Status: NEEDS_WORK' in handoff or '@dev-continue' in handoff.lower():
            return 'NEEDS_WORK'
        elif 'Status: BLOCKED' in handoff or '@blocked' in handoff.lower():
            return 'BLOCKED'
        
        return 'WORKING'
    
    def update_cycle_count(self):
        """Update cycle count in scratchpad.md"""
        try:
            content = self.read_file('scratchpad.md')
            if '**Cycle**:' in content:
                import re
                updated = re.sub(r'\*\*Cycle\*\*: \d+', f'**Cycle**: {self.cycle}', content)
                Path('scratchpad.md').write_text(updated)
        except Exception as e:
            print(f"⚠️ Error updating cycle count: {e}")
    
    def prompt_user(self, mode, message):
        """Prompt user to work in Cursor"""
        print(f"\n{'═' * 60}")
        print(f"{'🔨 DEV MODE' if mode == 'DEV' else '🔍 CRITIC MODE'}")
        print(f"{'═' * 60}")
        print(f"\n📋 Instructions:")
        print(f"   {message}")
        print(f"\n💡 In Cursor:")
        print(f"   1. Open Composer (Cmd+I or Ctrl+I)")
        print(f"   2. You're in {mode} mode (check handoff.md)")
        print(f"   3. Follow the .cursorrules for {mode} mode")
        print(f"   4. Update handoff.md when done")
        print(f"\n⏸️  Press Enter when you've completed this phase...")
        input()
    
    def run_initialization(self):
        """Guide user through initialization"""
        print("\n" + "═" * 60)
        print("🌱 INITIALIZATION MODE")
        print("═" * 60)
        print("\n📋 Detected project-init.md with new app idea")
        print("   Need to generate goals first...\n")
        
        self.write_handoff('DEV')
        
        print("💡 In Cursor:")
        print("   1. Open Composer")
        print("   2. Say: 'Read project-init.md and generate goals'")
        print("   3. System will populate goals.md")
        print("   4. System will set Status: READY_FOR_REVIEW in handoff.md")
        print("\n⏸️  Press Enter when goals are generated...")
        input()
        
        status = self.get_status()
        
        if status == 'BLOCKED':
            print("\n🚫 Initialization BLOCKED - needs clarification")
            print("   Check project-init.md for questions")
            print("   Answer questions and run orchestrator again")
            return False
        
        if status == 'READY_FOR_REVIEW':
            print("\n🔍 Now reviewing goals in CRITIC mode...")
            self.write_handoff('CRITIC')
            
            print("\n💡 In Cursor:")
            print("   1. Open Composer")
            print("   2. Say: 'Review the generated goals'")
            print("   3. System will check goals are small, testable, ordered")
            print("   4. System will set Status: APPROVED or NEEDS_WORK")
            print("\n⏸️  Press Enter when review is complete...")
            input()
            
            status = self.get_status()
            
            if status == 'APPROVED':
                print("\n✅ Goals approved! Starting implementation...")
                return True
            else:
                print("\n⚠️ Goals need refinement. Run orchestrator again.")
                return False
        
        return False
    
    def run(self):
        """Main orchestration loop"""
        print("╔" + "═" * 58 + "╗")
        print("║" + " " * 12 + "CURSOR PAIRED AGENT ORCHESTRATOR" + " " * 13 + "║")
        print("╚" + "═" * 58 + "╝")
        print(f"\n📋 Configuration:")
        print(f"   Max cycles: {self.max_cycles}")
        print(f"   Project: {self.project_root}")
        
        # Check if initialization is needed
        if self.needs_init:
            print(f"\n🌱 Initialization required")
            if not self.run_initialization():
                print("\n⚠️ Initialization incomplete. Exiting.")
                return
            # Reset handoff for implementation
            self.write_handoff('DEV')
            Path('handoff.md').write_text(
                Path('handoff.md').read_text().replace('Status: APPROVED', 'Status: WORKING')
            )
        
        print(f"\n🎯 Starting paired agent session...\n")
        
        while self.cycle < self.max_cycles:
            self.cycle += 1
            self.update_cycle_count()
            
            print(f"\n{'═' * 60}")
            print(f"🔄 CYCLE {self.cycle}/{self.max_cycles}")
            print(f"{'═' * 60}")
            
            # ============================================
            # DEV PHASE
            # ============================================
            self.write_handoff('DEV')
            
            dev_message = (
                f"Work on active goal from goals.md (Cycle {self.cycle})\n"
                "   - Check handoff.md for critic feedback\n"
                "   - Write tests FIRST (TDD)\n"
                "   - Implement minimally (no over-engineering)\n"
                "   - Update handoff.md with Status: READY_FOR_REVIEW when done"
            )
            
            self.prompt_user('DEV', dev_message)
            
            status = self.get_status()
            print(f"\n📊 Status after DEV: {status}")
            
            if status == 'BLOCKED':
                print("\n🚫 DEV is BLOCKED. Check handoff.md for details.")
                print("   Resolve the blocker and run orchestrator again.")
                break
            
            if status != 'READY_FOR_REVIEW':
                print("\n⚠️ Dev didn't signal READY_FOR_REVIEW.")
                print("   Expected 'Status: READY_FOR_REVIEW' in handoff.md")
                print("   Update handoff.md and run orchestrator again.")
                break
            
            # ============================================
            # CRITIC PHASE
            # ============================================
            self.write_handoff('CRITIC')
            
            critic_message = (
                f"Review dev's work (Cycle {self.cycle})\n"
                "   - Check tests exist and pass\n"
                "   - Check code addresses ONLY active goal\n"
                "   - Check for over-engineering/scope creep\n"
                "   - Update critic-notes.md with findings\n"
                "   - Update handoff.md with Status: APPROVED or NEEDS_WORK"
            )
            
            self.prompt_user('CRITIC', critic_message)
            
            status = self.get_status()
            print(f"\n📊 Status after CRITIC: {status}")
            
            if status == 'APPROVED':
                print("\n" + "═" * 60)
                print("✅ GOAL APPROVED!")
                print("═" * 60)
                print("\n🎉 The critic has approved the implementation.")
                
                # Check if there are more goals
                goals_content = self.read_file('goals.md')
                if '## Up Next' in goals_content and '**Goal #' in goals_content.split('## Up Next')[1]:
                    print("\n📋 More goals remaining...")
                    print("   In Cursor, move next goal to 'Active Goal' section")
                    print("   Then run orchestrator again to continue.")
                else:
                    print("\n🏆 All goals complete! Project finished.")
                break
            
            elif status == 'BLOCKED':
                print("\n🚫 CRITIC found a BLOCKER.")
                print("   Check handoff.md and critic-notes.md for details.")
                print("   Resolve and run orchestrator again.")
                break
            
            elif status == 'NEEDS_WORK':
                print("\n🔄 Needs work. Starting next cycle...")
                print("   Dev will address feedback in next iteration.")
                continue
            
            else:
                print(f"\n⚠️ Unclear status: {status}")
                print("   Expected APPROVED, NEEDS_WORK, or BLOCKED.")
                print("   Check handoff.md for proper status format.")
                break
        
        # ============================================
        # SESSION COMPLETE
        # ============================================
        if self.cycle >= self.max_cycles:
            print(f"\n⏰ Reached maximum cycles ({self.max_cycles})")
            print("   Consider increasing max_cycles or breaking goal into smaller pieces.")
        
        print("\n" + "═" * 60)
        print("🏁 PAIRED SESSION COMPLETE")
        print("═" * 60)
        print(f"\n📈 Summary:")
        print(f"   Total cycles: {self.cycle}")
        print(f"   Final status: {self.get_status()}")
        print(f"\n📁 Check these files for details:")
        print(f"   - goals.md (goal status)")
        print(f"   - handoff.md (latest feedback)")
        print(f"   - critic-notes.md (review details)")
        print(f"   - scratchpad.md (session history)")
        print()

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Cursor Paired Agent Orchestrator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --cycles 5     # Run up to 5 dev-critic cycles
  %(prog)s --cycles 20    # For larger projects
  
Initialization:
  1. Create project-init.md with your app idea
  2. Run: %(prog)s --cycles 20
  3. Follow prompts to work in Cursor
        """
    )
    
    parser.add_argument(
        '--cycles',
        type=int,
        default=10,
        help='Maximum number of dev-critic cycles (default: 10)'
    )
    
    args = parser.parse_args()
    
    orchestrator = CursorOrchestrator(max_cycles=args.cycles)
    
    try:
        orchestrator.run()
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted by user. Session stopped.")
        print(f"   Completed {orchestrator.cycle} cycles.")
        sys.exit(0)

if __name__ == '__main__':
    main()