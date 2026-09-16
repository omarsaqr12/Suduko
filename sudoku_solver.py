"""Sudoku constraints and a backtracking solver for 9x9 integer grids.

Zero represents an empty cell. ``solve`` modifies its input only on success.
"""


def valid(board, num, pos):
    """Whether placing a digit at (row, column) violates no Sudoku constraint."""
    row, col = pos
    if not (0 <= row < 9 and 0 <= col < 9 and isinstance(num, int) and 1 <= num <= 9):
        return False
    if len(board) != 9 or any(len(line) != 9 for line in board):
        return False
    if any(board[row][c] == num for c in range(9) if c != col):
        return False
    if any(board[r][col] == num for r in range(9) if r != row):
        return False
    return not any(
        board[r][c] == num and (r, c) != pos
        for r in range(row // 3 * 3, row // 3 * 3 + 3)
        for c in range(col // 3 * 3, col // 3 * 3 + 3)
    )


def find_empty(board):
    return next(((r, c) for r in range(9) for c in range(9) if board[r][c] == 0), None)


def is_consistent(board):
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False
    return all(
        type(board[r][c]) is int and 0 <= board[r][c] <= 9
        and (board[r][c] == 0 or valid(board, board[r][c], (r, c)))
        for r in range(9) for c in range(9)
    )


def solve(board):
    """Solve a consistent puzzle in place, returning whether it has a solution."""
    if not is_consistent(board):
        return False

    def search():
        best = None
        options = None
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    choices = [n for n in range(1, 10) if valid(board, n, (r, c))]
                    if not choices:
                        return False
                    if options is None or len(choices) < len(options):
                        best, options = (r, c), choices
        if best is None:
            return True
        r, c = best
        for n in options:
            board[r][c] = n
            if search():
                return True
        board[r][c] = 0
        return False

    return search()


def generate_board(level):
    from sudoku_generator import generate_puzzle
    return generate_puzzle(level)


def print_board(board):
    for row in board:
        print(' '.join(str(n) if n else '.' for n in row))
