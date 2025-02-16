print("Enter k:")
k = int(input())
print("Enter n:")
n = int(input())
board = [[0 for i in range(k**2)] for j in range(k**2)]

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def print_board():

    # find the digits of n
    x = n
    digit = 0
    while x > 0:
        x = x//10
        digit +=1

    #print the board
    for row in board:
        for col in row:
            if col == 0:
                print("|" + " "*digit, end='')
            else:
                print(f"|{col:>{digit}}", end='')

        print('|')

def make_move(mv):
    # find the row
    r1 = mv[0] // k
    r2 = mv[1] // k
    row = r1*k + r2
    # find the column
    c1 = mv[0] % k
    c2 = mv[1] % k
    col = c1*k + c2

    temp = board[row][col]
    board[row][col] = mv[2]

    return temp

def verify_board():

    invalid = False
    unsolved = False

    for i in range(0, len(board)):

        r1 = i // k
        c1 = i % k

        box_sum = 0
        row_sum = 0
        col_sum = 0
        for j in range(0, len(board)):
            row_sum += board[i][j]
            col_sum += board[j][i]
            r2 = j // k
            c2 = j % k
            col = k*c1 + c2
            row = k*r1 + r2
            box_sum += board[row][col]

        if col_sum > n or row_sum > n or box_sum > n:
            invalid = True
            break

        elif col_sum < n or row_sum < n or box_sum < n:
            unsolved = True

    if invalid:
        return -1
    if unsolved:
        return 0

    for row in board:
        for col in row:
            if col == 0:
                return 0

    return 1

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print_board()
print("Next Move:")
command = ""
while command != "end":
    usr_inp = input().split()
    command = usr_inp[0]
    if command == "move":
        move = int(usr_inp[1]), int(usr_inp[2]), int(usr_inp[3])
        prev_val = make_move(move)
        result = verify_board()
        # If not valid move, undo the move
        if -1 == result:
            move = move[0], move[1], prev_val
            make_move(move)
            print_board()
            print("Your move was invalid, please try again:")
        # If the board wins, end the game
        elif 1 == result:
            print_board()
            print("Congratulations! You have solved the puzzle!")
            break
        else:
            print_board()
            print("Next Move:")




