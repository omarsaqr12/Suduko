# Sudoku: puzzle generator, solver, and Pygame game

A desktop Sudoku project written in Python. It creates a filled 9×9 board, removes clues while checking that **exactly one solution remains**, and provides a keyboard-and-mouse game with answer checking, hints, and animated solution reveal.

This is a learning project, not a human-difficulty-rated puzzle service. The four difficulty names are **clue-count presets** rather than guaranteed difficulty ratings; an individual puzzle can retain more clues than its target if removing another would destroy uniqueness.

## Run the game

Requires Python 3.9+ and a graphical desktop (or an SDL-compatible display).

```bash
git clone https://github.com/omarsaqr12/Suduko.git
cd Suduko
python -m pip install -r requirements.txt
python main.py
```

Select Easy, Medium, Hard, or Insane from the opening screen. Click a cell and type a digit 1–9 to pencil in a candidate; press **Enter** to check and commit it. **Delete/Backspace** clears a non-given cell. **H** reveals a solution digit (not a logical explanation), **Space** reveals the remaining solution, and **Esc** closes the game. A wrong attempt counts as a mistake. Given clues cannot be changed.

For a deterministic puzzle in Python:

```python
import random
from sudoku_generator import generate_puzzle, count_solutions
from sudoku_solver import solve

puzzle = generate_puzzle('Medium', random.Random(42))
assert count_solutions(puzzle) == 1
answer = [row[:] for row in puzzle]
assert solve(answer)
```

## How it works

- [`sudoku_generator.py`](sudoku_generator.py): shuffles digits, rows within bands, columns within stacks, and band/stack order to produce valid complete grids. It removes clues in randomized order and **counts at most two solutions** using backtracking with minimum-remaining-values cell selection. A removal is kept only when there is one solution.
- [`sudoku_solver.py`](sudoku_solver.py): checks the row, column, and 3×3 box constraints, rejects inconsistent full grids, and solves by recursive backtracking. A failed solve restores tentative placements.
- [`gui.py`](gui.py): tracks the immutable clues, mutable player entries, and a precomputed solution separately. Move checking does not run an in-place solve on the displayed grid.
- [`initial_page.py`](initial_page.py) and [`main.py`](main.py): explicit difficulty-selection and application entry points; importing modules does not open a window.

The clue targets are Easy **40**, Medium **34**, Hard **30**, and Insane **26**; they are **not** ratings based on logical techniques, number of guesses, or human studies. Puzzle generation may take longer for the lower-clue presets.

## Verification

```bash
python -m unittest discover -s tests -v
```

[`tests/test_sudoku.py`](tests/test_sudoku.py) checks several fixed random seeds across all four presets, independently counts solutions, verifies that counting does not modify the puzzle, exercises an invalid completed board, and checks that GUI state remains consistent after correct and incorrect entries. [GitHub Actions](.github/workflows/test.yml) runs these tests with a headless SDL driver. This test set is finite; it does not prove the code has no defects or measure puzzle difficulty or performance across all random seeds.

## Limitations

The interface requires Pygame and has no browser/mobile build. Hinting reveals the answer rather than deriving an explainable next move. The animated reveal blocks normal input briefly. No accessible gameplay screenshot is currently included; the old README's placeholder image was not an actual capture.

The repository name is retained as `Suduko` so existing links continue to work. The game and puzzle are correctly called **Sudoku** here.

## License

See the existing [MIT license](LICENSE). No license changes are part of this update.
