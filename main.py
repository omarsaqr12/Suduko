#!/usr/bin/env python3
"""
Sudoku Game - Main Entry Point

A Sudoku puzzle generator and solver with GUI interface.
Features different difficulty levels: Easy, Medium, Hard, and Insane.

Author: Your Name
"""

import sys
import pygame
from initial_page import *

def main():
    """Main entry point for the Sudoku game."""
    try:
        # Initialize pygame
        pygame.init()
        
        # Run the initial page (difficulty selection)
        print("Welcome to Sudoku Game!")
        print("Select your difficulty level in the GUI window that opens.")
        
        # The initial_page.py script will handle the rest
        # (The code from initial_page.py will run when imported)
        
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
