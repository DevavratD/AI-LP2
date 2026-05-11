import heapq


# 1. Goal Check Function
def check_win(board, player):
    win_conds = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for combo in win_conds:
        flag = True

        for i in combo:
            if board[i] != player:
                flag = False

        if flag:
            return True

        return False


# 2. Heuristic Function h(n)
# Estimates cost to reach goal (Win). Lower is better.
def get_h(board):
    if check_win(board, "X"):
        return 0  # Goal reached

    # Block opponent 'O' from winning (High priority/low cost)
    win_conds = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for combo in win_conds:
        if (
            sum(1 for i in combo if board[i] == "O") == 2
            and sum(1 for i in combo if board[i] == " ") == 0
        ):  # Check if we just blocked
            return 1

    if board[4] == "X":
        return 2  # Strategic Center
    return 4  # Other moves


# 3. A* Search Function
def a_star(current_board):
    # g(n): Number of moves made so far (path cost)
    g_n = sum(1 for slot in current_board if slot != " ")
    open_list = []

    for i in range(9):
        if current_board[i] == " ":
            temp_board = current_board.copy()
            temp_board[i] = "X"

            # f(n) = g(n) + h(n)
            h_n = get_h(temp_board)
            f_n = (g_n + 1) + h_n

            # Store in Priority Queue
            heapq.heappush(open_list, (f_n, temp_board))

    return heapq.heappop(open_list) if open_list else (None, None)

# --- Execution ---
test_board = ['O', 'X', ' ', 
              'O', 'X', ' ', 
              ' ', ' ', ' '] # AI should block O's diagonal win at index 8

print("Current Board:")
for i in range(0, 9, 3):
    print(f"{test_board[i]} | {test_board[i + 1]} | {test_board[i + 2]}")

f_score, next_move = a_star(test_board)

print(f"\nAI Move (f(n)={f_score}):")
for i in range(0, 9, 3):
    print(f"{next_move[i]} | {next_move[i + 1]} | {next_move[i + 2]}")
