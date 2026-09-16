"""Pygame interface for the Sudoku puzzle generator and solver."""

import time

import pygame as p
from sudoku_solver import generate_board, solve


class Grid:
    def __init__(self, width, height, level):
        self.board = generate_board(level)
        self.solution = [row[:] for row in self.board]
        if not solve(self.solution):
            raise ValueError('Generated puzzle is not solvable')
        self.rows = self.cols = 9
        self.width, self.height = width, height
        self.cubes = [
            [Cube(self.board[r][c], r, c, width, height) for c in range(9)]
            for r in range(9)
        ]
        self.selected = None
        self.model = [row[:] for row in self.board]

    def update_model(self):
        self.model = [[self.cubes[r][c].value for c in range(9)] for r in range(9)]

    def place(self, val):
        if self.selected is None:
            return False
        row, col = self.selected
        if self.board[row][col] != 0 or self.cubes[row][col].value != 0:
            return False
        if val != self.solution[row][col]:
            self.cubes[row][col].set_temp(0)
            return False
        self.cubes[row][col].set(val)
        self.cubes[row][col].set_temp(0)
        self.update_model()
        return True

    def hints(self, win):
        """Reveal the solution value of the selected cell, or the first empty cell."""
        candidate = self.selected
        if candidate is None or self.cubes[candidate[0]][candidate[1]].value != 0:
            candidate = next(
                ((r, c) for r in range(9) for c in range(9)
                 if self.cubes[r][c].value == 0), None
            )
        if candidate is None:
            return False
        r, c = candidate
        self.cubes[r][c].set(self.solution[r][c])
        self.cubes[r][c].set_temp(0)
        self.update_model()
        self.draw(win)
        p.display.update()
        return True

    def solve_gui(self, win):
        """Reveal the known unique solution one cell at a time."""
        for r in range(9):
            for c in range(9):
                if self.cubes[r][c].value == 0:
                    self.cubes[r][c].set(self.solution[r][c])
                    self.cubes[r][c].set_temp(0)
                    self.cubes[r][c].draw_change(win, True)
                    p.display.update()
                    p.event.pump()
                    p.time.delay(45)
        self.update_model()
        return True

    def sketch(self, val):
        if self.selected is not None:
            r, c = self.selected
            if self.board[r][c] == 0 and self.cubes[r][c].value == 0:
                self.cubes[r][c].set_temp(val)

    def draw(self, win):
        for row in self.cubes:
            for cube in row:
                cube.draw(win)
        gap = self.width / 9
        for i in range(10):
            thick = 4 if i % 3 == 0 else 1
            p.draw.line(win, (80, 80, 80), (0, i * gap), (self.width, i * gap), thick)
            p.draw.line(win, (80, 80, 80), (i * gap, 0), (i * gap, self.height), thick)

    def select(self, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            return
        for line in self.cubes:
            for cube in line:
                cube.selected = False
        self.selected = (row, col)
        self.cubes[row][col].selected = True

    def clear(self):
        if self.selected is None:
            return
        r, c = self.selected
        if self.board[r][c] == 0:
            self.cubes[r][c].set(0)
            self.cubes[r][c].set_temp(0)
            self.update_model()

    def click(self, pos):
        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            return int(pos[1] * 9 / self.height), int(pos[0] * 9 / self.width)
        return None

    def is_finished(self):
        return all(self.cubes[r][c].value == self.solution[r][c]
                   for r in range(9) for c in range(9))


class Cube:
    def __init__(self, value, row, col, width, height):
        self.value, self.row, self.col = value, row, col
        self.original = value != 0
        self.temp = 0
        self.width, self.height = width, height
        self.selected = False

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val

    def draw(self, win):
        gap = self.width / 9
        x, y = self.col * gap, self.row * gap
        if self.original:
            p.draw.rect(win, (236, 238, 240), (x, y, gap, gap))
        value = self.value or self.temp
        if value:
            font = p.font.SysFont(None, 36 if self.value else 28)
            color = (20, 20, 20) if self.value else (100, 100, 100)
            text = font.render(str(value), True, color)
            win.blit(text, (x + (gap - text.get_width()) / 2,
                            y + (gap - text.get_height()) / 2))
        if self.selected:
            p.draw.rect(win, (40, 100, 210), (x, y, gap, gap), 3)

    def draw_change(self, win, correct=True):
        self.draw(win)
        gap = self.width / 9
        p.draw.rect(win, (0, 150, 80) if correct else (220, 40, 40),
                    (self.col * gap, self.row * gap, gap, gap), 3)


def format_time(seconds):
    minutes, secs = divmod(int(seconds), 60)
    return f'{minutes:02d}:{secs:02d}'


def main(level):
    p.init()
    win = p.display.set_mode((540, 600))
    p.display.set_caption('Sudoku — ' + level)
    board = Grid(540, 540, level)
    start, strikes = time.monotonic(), 0
    clock = p.time.Clock()
    running = True
    finished = False
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                clicked = board.click(event.pos)
                if clicked is not None:
                    board.select(*clicked)
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    running = False
                elif event.key in (p.K_DELETE, p.K_BACKSPACE):
                    board.clear()
                elif event.key == p.K_h and not finished:
                    board.hints(win)
                elif event.key == p.K_SPACE and not finished:
                    board.solve_gui(win)
                elif event.key in (p.K_RETURN, p.K_KP_ENTER) and not finished:
                    if board.selected is not None:
                        r, c = board.selected
                        guess = board.cubes[r][c].temp
                        if guess and not board.place(guess):
                            strikes += 1
                elif event.unicode and event.unicode in '123456789' and not finished:
                    board.sketch(int(event.unicode))
        finished = board.is_finished()
        win.fill((255, 255, 255))
        board.draw(win)
        font = p.font.SysFont(None, 27)
        elapsed = format_time(time.monotonic() - start)
        status = 'Solved!' if finished else f'Time {elapsed}   Mistakes {strikes}'
        win.blit(font.render(status, True, (25, 25, 25)), (15, 550))
        p.display.flip()
        clock.tick(30)
