"""
REX - Reasoning Engine eXtended
A modular, extensible AI system inspired by JARVIS with advanced capabilities.

Main entry point for the REX AI system.
"""

import sys
import os
import logging
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Create necessary directories
os.makedirs("logs", exist_ok=True)
os.makedirs("memory", exist_ok=True)
os.makedirs("data", exist_ok=True)

from core.engine import AIEngine
from security.permission_system import PermissionManager
from config.settings import SYSTEM_CONFIG, LOG_LEVEL
from utils.logger import setup_logging

# Setup logging
logger = setup_logging(__name__, LOG_LEVEL)


class REXSystem:
    """Main REX AI System coordinator."""
    
    def __init__(self):
        """Initialize the REX system."""
        logger.info("Initializing REX AI System...")
        
        self.permission_manager = PermissionManager()
        self.engine = AIEngine(self.permission_manager)
        self.running = False
        
        logger.info("REX AI System initialized successfully")
    
    def start(self):
        """Start the REX system."""
        logger.info("Starting REX AI System")
        self.running = True
        self.engine.initialize()
        
        print("""
        ╔════════════════════════════════════════╗
        ║     REX - Reasoning Engine eXtended    ║
        ║          AI System v1.0                ║
        ╚════════════════════════════════════════╝
        """)
        print(f"System initialized at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Type 'help' for commands, 'exit' to quit\n")
    
    def process_input(self, user_input: str) -> str:
        """
        Process user input through the AI engine.
        
        Args:
            user_input: User's natural language input
            
        Returns:
            AI response
        """
        if user_input.lower() == 'exit':
            self.shutdown()
            return "REX shutting down. Goodbye."
        
        if user_input.lower() == 'help':
            return self.show_help()
        
        if user_input.lower() == 'status':
            return self.show_status()
        
        return self.engine.process(user_input)
    
    def show_help(self) -> str:
        """Show available commands."""
        help_text = """
        REX Commands:
        ─────────────
        help      - Show this help message
        status    - Show system status
        exit      - Shutdown REX
        
        You can also ask REX questions in natural language.
        Examples:
          - "What is the weather?"
          - "Execute the backup protocol"
          - "Learn about quantum computing"
          - "Set a reminder for tomorrow"
        """
        return help_text
    
    def show_status(self) -> str:
        """Show system status."""
        return self.engine.get_status()
    
    def shutdown(self):
        """Shutdown the REX system gracefully."""
        logger.info("Shutting down REX AI System")
        self.running = False
        self.engine.shutdown()
        sys.exit(0)
    
    def interactive_mode(self):
        """Run REX in interactive mode."""
        self.start()
        
        try:
            while self.running:
                try:
                    user_input = input("You: ").strip()
                    if user_input:
                        response = self.process_input(user_input)
                        print(f"\nREX: {response}\n")
                except KeyboardInterrupt:
                    print("\n")
                    self.shutdown()
                except Exception as e:
                    logger.error(f"Error processing input: {e}")
                    print(f"Error: {e}")
        except Exception as e:
            logger.critical(f"Critical error in interactive mode: {e}")
            self.shutdown()


def main():
    """Main entry point."""
    try:
        rex = REXSystem()
        rex.interactive_mode()
    except Exception as e:
        logger.critical(f"Failed to start REX: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
