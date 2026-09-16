"""Run the Sudoku GUI with ``python main.py``."""

import pygame
from initial_page import choose_difficulty
from gui import main as play


def main():
    try:
        level = choose_difficulty()
        if level is not None:
            play(level)
    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
