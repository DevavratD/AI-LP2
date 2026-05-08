class NQueen:

    def __init__(self, n):

        self.n = n

        # Create empty board
        self.board = []

        for i in range(n):

            row = []

            for j in range(n):
                row.append(0)

            self.board.append(row)

    # Display Board
    def display(self):

        print()

        for row in self.board:
            print(row)

    # Check Safe Position
    def isSafe(self, row, col):

        # Check left side
        for i in range(col):

            if self.board[row][i] == 1:
                return False

        # Upper diagonal
        i = row
        j = col

        while i >= 0 and j >= 0:

            if self.board[i][j] == 1:
                return False

            i -= 1
            j -= 1

        # Lower diagonal
        i = row
        j = col

        while i < self.n and j >= 0:

            if self.board[i][j] == 1:
                return False

            i += 1
            j -= 1

        return True

    # Solve using Backtracking + Branch and Bound
    def solve(self, col):

        # All queens placed
        if col >= self.n:
            return True

        # Try every row
        for row in range(self.n):

            # Branch and Bound Condition
            if self.isSafe(row, col):

                # Place Queen
                self.board[row][col] = 1

                # Recursive Call
                if self.solve(col + 1):
                    return True

                # Backtrack
                self.board[row][col] = 0

        return False


# ----------------------------------------
# 4 Queen Visualization
#
# [0, 0, 1, 0]
# [1, 0, 0, 0]
# [0, 0, 0, 1]
# [0, 1, 0, 0]
#
# 1 = Queen
# 0 = Empty
# ----------------------------------------


n = int(input("Enter Number of Queens: "))

game = NQueen(n)

if game.solve(0):

    print("\nSolution Found")

    game.display()

else:

    print("\nSolution Does Not Exist")