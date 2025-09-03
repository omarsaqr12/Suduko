"""
Sudoku Game - Initial Page Module

This module handles the difficulty selection screen for the Sudoku game.
Provides a GUI interface for choosing between Easy, Medium, Hard, and Insane levels.
"""

import pygame
import gui

pygame.init()


run=True
insane=(255,0,0)
easy=(0,255,0)
medium=(0,0,255)
hard=(165,165,0)
screen=pygame.display.set_mode([300,450])
pygame.display.set_caption('Sudoku Game')
background=(255,255,255)
framereate=60
font=pygame.font.Font('freesansbold.ttf',16)
timer=pygame.time.Clock()
def draw_dif(color,y_coord,lev):
    pygame.draw.circle(screen,color,(30,y_coord),20,5)
    pygame.draw.rect(screen,color,[70,y_coord-15,200,30])
    leveldiff=font.render(lev,True,(0,0,0))
    screen.blit(leveldiff,(78,y_coord-10))
while run:
    screen.fill(background)
    draw_dif(easy,50,"easy")
    draw_dif(medium,150,"medium")
    draw_dif(hard,250,"hard")
    draw_dif(insane,350,"insane")
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            y=pygame.mouse.get_pos()[1]
            if y>=35 and y<65:
                level="Easy"
                gui.main(level)
            elif y>=135 and y<165:
                level="Medium"
                gui.main(level)
            elif y>=235 and y<265:
                level="Hard"
                gui.main(level)
            elif y>=335 and y<365:
                level="Insane"
                gui.main(level)
