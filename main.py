import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("Tic-Tac-Toe by Uros")
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
icon = PhotoImage(file="venv/tictactoe.ico")
root.iconphoto(False, icon)

board = [[" " for x in range(3)] for y in range(3)]

current_player = "X"

def button_click(row, col):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        if check_winner(current_player):
            tkinter.messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset()
        elif check_draw():
            tkinter.messagebox.showinfo("Game Over", "It's a draw!")
            reset()
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player ="X"
            label.config(text=f"{current_player}'s turn.")

def check_winner(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

def reset():
    global current_player, board

    current_player = "X"
    board = [[" " for m in range(3)] for n in range(3)]

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state=NORMAL)

label = Label(text=f"{current_player}'s turn.", font=("Helvetica", 20))
label.grid(row=0, column=1, sticky="nsew")

buttons = [[None, None, None] for b in range(3)]
for r in range(3):
    for c in range(3):
        root.rowconfigure(r, weight=1)
        root.columnconfigure(c, weight=1)
        buttons[r][c] = Button(root, text=" ", font=("Helvetica", 20), width=7, height=4,
                                   command=lambda row=r, col=c: button_click(row, col))
        buttons[r][c].grid(row=r+1, column=c, sticky="nsew")

root.mainloop()