# Configuration
N = 4


def solve_n_queens(col, board, rows, lower_diag, upper_diag):
    # BASE CASE: If all queens are placed, we found a solution
    if col == N:
        return True

    for row in range(N):
        # BRANCH AND BOUND: Prune the search if a constraint is violated
        # lower_diag index: row + col
        # upper_diag index: (N-1) + col - row
        if (
            rows[row] == 0
            and lower_diag[row + col] == 0
            and upper_diag[N - 1 + col - row] == 0
        ):
            # 1. PLACE QUEEN
            board[row][col] = "Q"
            rows[row] = lower_diag[row + col] = upper_diag[N - 1 + col - row] = 1

            # 2. RECURSIVE STEP: Move to the next column
            if solve_n_queens(col + 1, board, rows, lower_diag, upper_diag):
                return True

            # 3. BACKTRACKING: Remove queen and reset constraints for next attempt
            board[row][col] = "."
            rows[row] = lower_diag[row + col] = upper_diag[N - 1 + col - row] = 0

    return False


# --- Initialization ---
board = [["." for _ in range(N)] for _ in range(N)]
rows = [0] * N
lower_diag = [0] * (2 * N - 1)
upper_diag = [0] * (2 * N - 1)

print(f"--- Solving {N}-Queens Problem ---")
if solve_n_queens(0, board, rows, lower_diag, upper_diag):
    for r in board:
        print("  ".join(r))
else:
    print("No solution exists.")
