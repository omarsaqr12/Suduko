"""Deterministic Sudoku correctness and GUI state regression tests."""
import random
import unittest

from sudoku_generator import CLUE_TARGETS, count_solutions, generate_puzzle, solved_grid
from sudoku_solver import is_consistent, solve, valid


class SudokuTests(unittest.TestCase):
    def test_solved_pattern_and_generations(self):
        for seed in (0, 1, 2):
            for level, target in CLUE_TARGETS.items():
                with self.subTest(seed=seed, level=level):
                    puzzle = generate_puzzle(level, random.Random(seed))
                    snapshot = [row[:] for row in puzzle]
                    self.assertTrue(is_consistent(puzzle))
                    self.assertGreaterEqual(sum(bool(n) for row in puzzle for n in row), target)
                    self.assertEqual(count_solutions(puzzle), 1)
                    self.assertEqual(puzzle, snapshot, 'counting mutated the input')
                    self.assertTrue(solve(snapshot))
                    self.assertTrue(is_consistent(snapshot))
                    self.assertTrue(all(n for row in snapshot for n in row))

    def test_rejects_inconsistent_completed_grid(self):
        bad = solved_grid(random.Random(2))
        bad[0][0] = bad[0][1]
        original = [row[:] for row in bad]
        self.assertFalse(is_consistent(bad))
        self.assertFalse(solve(bad))
        self.assertEqual(count_solutions(bad), 0)
        self.assertEqual(bad, original)

    def test_rejects_bad_inputs(self):
        with self.assertRaises(ValueError):
            generate_puzzle('Extreme')
        with self.assertRaises(ValueError):
            count_solutions([[0] * 9 for _ in range(9)], limit=0)
        self.assertFalse(valid([[0] * 9 for _ in range(9)], 10, (0, 0)))

    def test_gui_does_not_mutate_display_during_validation(self):
        import gui
        board = gui.Grid(540, 540, 'Easy')
        self.assertEqual(board.model, board.board)
        self.assertIsNone(board.click((540, 10)))
        self.assertEqual(board.click((90, 150)), (2, 1))
        r, c = next((r, c) for r in range(9) for c in range(9) if board.board[r][c] == 0)
        board.select(r, c)
        wrong = board.solution[r][c] % 9 + 1
        self.assertFalse(board.place(wrong))
        self.assertEqual(board.model, board.board)
        self.assertTrue(board.place(board.solution[r][c]))
        self.assertEqual(board.model[r][c], board.solution[r][c])
        board.clear()
        self.assertEqual(board.model[r][c], 0)


if __name__ == '__main__':
    unittest.main()
