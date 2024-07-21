# Function to generate RGB escape codes
def rgb_escape_code(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


# Colors for text
WINNER_COLOR = rgb_escape_code(171, 157, 255)  # lilac for winner
RED_COLOR = rgb_escape_code(255, 157, 169)  # for crit failure (rolling 1)
FIRST_COLOR = rgb_escape_code(157, 255, 179)  # first player color
SECOND_COLOR = rgb_escape_code(157, 226, 255)  # second player color

RESET = "\033[0m"  # Reset color


def print_board(board):
    print(f"\n{SECOND_COLOR}[{board[0]}{board[1]}{board[2]}]\n[{board[3]}{board[4]}{board[5]}]\n[{board[6]}{board[7]}{board[8]}]{RESET}\n")


def check_board(board, current_player):
    tie = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == current_player for i in combo):
            print(f"✨{WINNER_COLOR}{current_player} is the winner!{RESET}✨")
            return True
    for i in tie:
        if i in board:
            break
        if i == tie[-1]:
            if i not in board:
                print(f"{SECOND_COLOR}It's a tie!{RESET}")
                return True
    return False


def play(board, x, o):

    plays = True
    player_current = x

    while plays:
        print(f"On what position do you want to place the {player_current}? Pick a number to place your sign: ")
        try:
            pick = int(input())
            if pick < 1 or pick > 9 or board[pick - 1] in [x, o]:
                print(f"{RED_COLOR}Invalid move. Try again.{RESET}")
                continue
        except ValueError:
            print(f"{RED_COLOR}Invalid input. Please enter a number between 1 and 9.{RESET}")
            continue
        board[pick - 1] = player_current
        print_board(board)
        check = check_board(board, player_current)
        if check:
            print("Do you want to play again? Y/N: ")
            ask = input().strip().upper()
            if ask == "Y":
                player_current = x
                board[:] = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
                print_board(board)
            elif ask == "N":
                print(f"{WINNER_COLOR}Thank you for playing!💜{RESET}")
                plays = False

        else:
            if player_current == x:
                player_current = o
            else:
                player_current = x


print(f"\n✖️🌕 {WINNER_COLOR}Welcome to XOXO{RESET} 🌕✖️\n")

x = "✖️"
o = "🌕"

player1 = input(f"{FIRST_COLOR}Player X will be: {RESET}")
player2 = input(f"{SECOND_COLOR}Player O will be: {RESET}")

ref_board2 = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
print_board(ref_board2)

play(ref_board2, x, o)

