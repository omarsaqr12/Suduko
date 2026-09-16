"""Difficulty selection screen; no GUI is started on import."""

import pygame

LEVELS = ('Easy', 'Medium', 'Hard', 'Insane')


def choose_difficulty():
    """Return the chosen clue-count preset, or None on window close."""
    pygame.init()
    screen = pygame.display.set_mode((320, 400))
    pygame.display.set_caption('Choose a Sudoku puzzle')
    font = pygame.font.SysFont(None, 32)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for i, level in enumerate(LEVELS):
                    if 40 <= x <= 280 and 50 + i * 85 <= y <= 105 + i * 85:
                        return level
        screen.fill((246, 247, 249))
        for i, level in enumerate(LEVELS):
            box = pygame.Rect(40, 50 + i * 85, 240, 55)
            pygame.draw.rect(screen, (220, 230, 247), box, border_radius=6)
            label = font.render(level, True, (20, 30, 45))
            screen.blit(label, label.get_rect(center=box.center))
        pygame.display.flip()
        clock.tick(30)
