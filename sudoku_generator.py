"""Generate Sudoku puzzles with an independently counted unique solution.

Difficulty labels are clue-count *presets*, not validated human difficulty ratings.
"""

import random

CLUE_TARGETS = {'Easy': 40, 'Medium': 34, 'Hard': 30, 'Insane': 26}


def count_solutions(board, limit=2):
    """Count up to ``limit`` completions without mutating the caller's grid."""
    from sudoku_solver import is_consistent, valid
    if limit < 1:
        raise ValueError('limit must be positive')
    if not is_consistent(board):
        return 0
    work = [row[:] for row in board]

    def count():
        best, choices = None, None
        for r in range(9):
            for c in range(9):
                if work[r][c] == 0:
                    candidates = [n for n in range(1, 10) if valid(work, n, (r, c))]
                    if not candidates:
                        return 0
                    if choices is None or len(candidates) < len(choices):
                        best, choices = (r, c), candidates
        if best is None:
            return 1
        r, c = best
        found = 0
        for n in choices:
            work[r][c] = n
            found += count()
            if found >= limit:
                work[r][c] = 0
                return found
        work[r][c] = 0
        return found

    return count()


def solved_grid(rng):
    """Randomize a known valid Latin/Sudoku pattern by valid symmetries."""
    digits = list(range(1, 10))
    rng.shuffle(digits)
    bands, stacks = [0, 1, 2], [0, 1, 2]
    rng.shuffle(bands)
    rng.shuffle(stacks)
    rows = [b * 3 + i for b in bands for i in rng.sample(range(3), 3)]
    cols = [b * 3 + i for b in stacks for i in rng.sample(range(3), 3)]
    return [[digits[(r * 3 + r // 3 + c) % 9] for c in cols] for r in rows]


def generate_puzzle(level='Medium', rng=None):
    """Return a 9x9 grid with exactly one solution, targeting a clue count.

    The number of clues may exceed the target when further removal would break
    uniqueness. This is not a guarantee of a particular human difficulty.
    """
    if level not in CLUE_TARGETS:
        raise ValueError('level must be one of: ' + ', '.join(CLUE_TARGETS))
    rng = rng if rng is not None else random.Random()
    puzzle = solved_grid(rng)
    positions = list(range(81))
    rng.shuffle(positions)
    clues = 81
    for index in positions:
        if clues <= CLUE_TARGETS[level]:
            break
        r, c = divmod(index, 9)
        previous = puzzle[r][c]
        puzzle[r][c] = 0
        if count_solutions(puzzle) != 1:
            puzzle[r][c] = previous
        else:
            clues -= 1
    return puzzle


def main(level):
    """Compatibility entry point for the original GUI."""
    return generate_puzzle(level)
