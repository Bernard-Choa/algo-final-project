from tkinter import *
import random

# Activates every time a button is pressed
def next_turn(r_gr, c_gr, row, col):
    global player, act_grid
    # Main branch of the game
    if megagrid[r_gr][c_gr][row][col]['text'] == "" and not check_winner_global() and not grid_status[r_gr][c_gr] and not grid_status[row][col] and (act_grid == [None, None] or act_grid == [r_gr, c_gr]) and empty_spaces_local(row, col):
        # Player x's turn
        if player == players[0]:
            megagrid[r_gr][c_gr][row][col]['text'] = player
            megagrid[r_gr][c_gr][row][col].config(fg="red")
            # Sets next turn to player o after checking that there's no winner yet
            if check_winner_global() == False:
                player = players[1]
                announcer.config(text=(players[1] + "'s turn"))
            # Declares player x as winner
            elif check_winner_global() == True:
                announcer.config(text=(players[0] + " wins"))
            # Declares tie
            elif check_winner_global() == "Tie":
                announcer.config(text=("It's a tie!"))
            # Sets next active grid
            act_grid[0] = row
            act_grid[1] = col

        # Player o's turn
        else:
            megagrid[r_gr][c_gr][row][col]['text'] = player
            megagrid[r_gr][c_gr][row][col].config(fg="blue")
            # Sets next turn to player x after checking that there's no winner yet
            if check_winner_global() == False:
                player = players[0]
                announcer.config(text=(players[0] + "'s turn"))
            # Declares player x as winner
            elif check_winner_global() == True:
                announcer.config(text=(players[1] + " wins"))
            # Declares tie
            elif check_winner_global() == "Tie":
                announcer.config(text=("It's a tie!"))
            # Sets next active grid
            act_grid[0] = row
            act_grid[1] = col

        for h_gr in range(3):
            for v_gr in range(3):
                # Active grid is highlighted in white
                if [h_gr, v_gr] == act_grid and not check_winner_global():
                    for r in range(3):
                        for c in range(3):
                            megagrid[h_gr][v_gr][r][c].config(bg="white")
                # Grids that are won will be marked in either red or blue depending on the victor
                elif grid_status[h_gr][v_gr]:
                    if grid_status[h_gr][v_gr] == players[0]:
                        for r in range(3):
                            for c in range(3):
                                megagrid[h_gr][v_gr][r][c].config(bg="#8E0D0D")
                    elif grid_status[h_gr][v_gr] == players[1]:
                        for r in range(3):
                            for c in range(3):
                                megagrid[h_gr][v_gr][r][c].config(bg="#0D238E")
                # Full grids with no victor (draw) are coloured yellow
                elif not empty_spaces_local(h_gr, v_gr):
                    for r in range(3):
                        for c in range(3):
                            megagrid[h_gr][v_gr][r][c].config(bg="yellow")
                # Non-active grids are coloured gray
                else:
                    for r in range(3):
                        for c in range(3):
                            megagrid[h_gr][v_gr][r][c].config(bg="grey")

    # Alternative branch for when the next grid is already won/tied
    elif (grid_status[row][col] or not empty_spaces_local(row, col)) and not check_winner_global():
        # Player x's turn
        if player == players[0]:
            megagrid[r_gr][c_gr][row][col]['text'] = player
            megagrid[r_gr][c_gr][row][col].config(fg="red")
            # Sets next turn to player o after checking that there's no winner yet
            if check_winner_global() == False:
                player = players[1]
                announcer.config(text=(players[1] + "'s turn"))
            # Declares player x as winner
            elif check_winner_global() == True:
                announcer.config(text=(players[0] + " wins"))
            # Declares tie
            elif check_winner_global() == "Tie":
                announcer.config(text=("It's a tie!"))
            # Resets active grid to None
            act_grid[0] = None
            act_grid[1] = None
        # Player o's turn
        else:
            megagrid[r_gr][c_gr][row][col]['text'] = player
            megagrid[r_gr][c_gr][row][col].config(fg="blue")
            # Sets next turn to player x after checking that there's no winner yet
            if check_winner_global() == False:
                player = players[0]
                announcer.config(text=(players[0] + "'s turn"))
            # Declares player o as winner
            elif check_winner_global() == True:
                announcer.config(text=(players[1] + " wins"))
            # Declares tie
            elif check_winner_global() == "Tie":
                announcer.config(text=("It's a tie!"))
            # Resets active grid to None
            act_grid[0] = None
            act_grid[1] = None

        for h_gr in range(3):
            for v_gr in range(3):
                # Active grids are highlighted in white
                if grid_status[h_gr][v_gr] == "":
                    for r in range(3):
                        for c in range(3):
                            megagrid[h_gr][v_gr][r][c].config(bg="white")
                # Grids that are won will be marked in either red or blue depending on the victor
                elif grid_status[h_gr][v_gr]:
                    if grid_status[h_gr][v_gr] == players[0]:
                        for r in range(3):
                            for c in range(3):
                                megagrid[h_gr][v_gr][r][c].config(bg="#8E0D0D")
                    elif grid_status[h_gr][v_gr] == players[1]:
                        for r in range(3):
                            for c in range(3):
                                megagrid[h_gr][v_gr][r][c].config(bg="#0D238E")
                # Full grids with no victor (draw) are coloured yellow
                elif not empty_spaces_local(h_gr, v_gr):
                    for r in range(3):
                        for c in range(3):
                            megagrid[h_gr][v_gr][r][c].config(bg="yellow")
                    print('this better fking work')
                # Non-active grids are coloured gray
                else:
                    for r in range(3):
                        for c in range(3):
                            megagrid[h_gr][v_gr][r][c].config(bg="grey")
                print(not empty_spaces_local(h_gr, v_gr))


# Checks local winner on a specific grid
def check_winner_local(r_gr, c_gr):
    global player, grid_status
    # Checks all three rows for a local winner
    for r in range(3):
        if megagrid[r_gr][c_gr][r][0]['text'] == megagrid[r_gr][c_gr][r][1]['text'] == megagrid[r_gr][c_gr][r][2]['text'] != "" and grid_status[r_gr][c_gr] == "":
            grid_status[r_gr][c_gr] = player
    # Checks all three columns for a local winner
    for c in range(3):
        if megagrid[r_gr][c_gr][0][c]['text'] == megagrid[r_gr][c_gr][1][c]['text'] == megagrid[r_gr][c_gr][2][c]['text'] != "" and grid_status[r_gr][c_gr] == "":
            grid_status[r_gr][c_gr] = player
    # Checks top-left to bottom-right diagonal for a local winner
    if megagrid[r_gr][c_gr][0][0]['text'] == megagrid[r_gr][c_gr][1][1]['text'] == megagrid[r_gr][c_gr][2][2]['text'] != "" and grid_status[r_gr][c_gr] == "":
        grid_status[r_gr][c_gr] = player
    # Checks top-right to bottom-left diagonal for a local winner
    elif megagrid[r_gr][c_gr][0][2]['text'] == megagrid[r_gr][c_gr][1][1]['text'] == megagrid[r_gr][c_gr][2][0]['text'] != "" and grid_status[r_gr][c_gr] == "":
        grid_status[r_gr][c_gr] = player
    # Declares tie on said grid
    elif empty_spaces_local(r_gr, c_gr) is False:
        return "Tie"
    else:
        return (False, "")


# Checks the global winner
def check_winner_global():
    for r_gr in range(3):
        # Initialises all nine grids
        check_winner_local(r_gr, 0)
        check_winner_local(r_gr, 1)
        check_winner_local(r_gr, 2)
        # Checks all three rows for a global winner
        if grid_status[r_gr][0] == grid_status[r_gr][1] == grid_status[r_gr][2] != "":
            return True
    # Checks all three columns for a global winner
    for c_gr in range(3):
        if grid_status[0][c_gr] == grid_status[1][c_gr] == grid_status[2][c_gr] != "":
            return True
    # Checks top-left to bottom-right diagonal for a global winner
    if grid_status[0][0] == grid_status[1][1] == grid_status[2][2] != "":
        return True
    # Checks top-right to bottom-left diagonal for a global winner
    elif grid_status[0][2] == grid_status[1][1] == grid_status[2][0] != "":
        return True

    for r_gr in range(3):
        for c_gr in range(3):
            # Checks all grids
            if empty_spaces_local(r_gr, c_gr) or not grid_status[r_gr][c_gr]:
                continue
            # Then declares global tie if all of the grids are full/have a victor
            else:
                for r in range(3):
                    for c in range(3):
                        megagrid[r_gr][c_gr][r][c].config(bg="yellow")
                return "Tie"

    else:
        return False


def empty_spaces_local(r_gr, c_gr):
    all_spaces = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]

    for r in range(3):
        for c in range(3):
            # Decrements the integer for every space taken until it reaches null
            if megagrid[r_gr][c_gr][r][c]['text'] != "":
                all_spaces[r_gr][c_gr] -= 1
    # Returns False if all the spaces in a particular grid are all occupied
    if all_spaces[r_gr][c_gr] == 0:
        return False
    else:
        return True


# Restarts game, this function is still glitched and not operational
def new_game():
    global player

    # Randomises starting player again
    player = random.choice(players)

    announcer.config(text=player+"'s turn")

    # Resets active grid as None
    act_grid[0], act_grid[1] = None, None

    for r_gr in range(3):
        for c_gr in range(3):
            for r in range(3):
                for c in range(3):
                    megagrid[r_gr][c_gr][r][c].config(text="", bg="#F0F0F0")
            grid_status[r_gr][c_gr] = ""


# Initialises main window
main_window = Tk()
main_window.title("Ultimate Tic Tac Toe")
# Initialises the players
players = ["x", "o"]
player = random.choice(players)
# Initialises the grid
grid1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid5 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid6 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid7 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid8 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid9 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
megagrid = [[grid1, grid2, grid3], [grid4, grid5, grid6], [grid7, grid8, grid9]]
grid_status = [["", "", ""], ["", "", ""], ["", "", ""]]
act_grid = [None, None]

# Displays announcer
announcer = Label(font=("consolas", 16), text=f"{player}'s turn")
announcer.pack(side="top")

# Displays restart button
restarter = Button(font=("consolas", 16), text="restart", command=new_game)
restarter.pack(side="bottom")

# Displays grid
frame = Frame(main_window)
frame.pack()

# Initialises every integer from the megagrid nested list as a Button object
for r_gr in range(3):
    for c_gr in range(3):
        for row in range(3):
            for col in range(3):
                megagrid[r_gr][c_gr][row][col] = Button(frame, text="", font=("consolas", 20), bg="white", width=3, height=1,
                                           command = lambda r_gr = r_gr, c_gr = c_gr, row = row, col = col: next_turn(r_gr, c_gr, row, col))
                megagrid[r_gr][c_gr][row][col].grid(row=(3 * r_gr) + row, column=(3 * c_gr) + col)


main_window.mainloop()
