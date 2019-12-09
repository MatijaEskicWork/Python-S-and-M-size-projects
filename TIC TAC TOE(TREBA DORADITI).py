import tkinter as tk
import tkinter.font as font
from tkinter import messagebox


window = tk.Tk()
window.title("Tic Tac Toe")

helv36 = font.Font(family='Helvetica', size=24, weight=font.BOLD)

player1 = {}
player1 = set()
player2 = {}
player2 = set()
ActivePlayer = 1
potez = 0

def OnClick(ind):
    global ActivePlayer
    global player1
    global player2
    global potez
    if ActivePlayer == 1:
        SetValue(ind,"X")
        player1.add(ind)
        print(player1)
        potez += 1
        ActivePlayer = 2
        window.title("Player 2 is on turn.")
    elif ActivePlayer == 2:
        SetValue(ind,"O")
        player2.add(ind)
        print(player2)
        potez += 1
        ActivePlayer = 1
        window.title("Player 1 is on turn.")
    CheckWinner()


def SetValue(broj,vrednost):
    buttons[broj].config(text=vrednost)
    buttons[broj].config(state="disabled")


def CheckWinner():
    global potez
    winner = -1

    if (potez<=9) and (0 in player1) and (1 in player1) and (2 in player1):
        winner = 1
    elif (potez<=9) and (0 in player2) and (1 in player2) and (2 in player2):
        winner = 2
    elif (potez<=9) and (3 in player1) and (4 in player1) and (5 in player1):
        winner = 1
    elif (potez<=9) and (3 in player2) and (4 in player2) and (5 in player2):
        winner = 2
    elif (potez<=9) and (6 in player1) and (7 in player1) and (8 in player1):
        winner = 1
    elif (potez<=9) and (6 in player2) and (7 in player2) and (8 in player2):
        winner = 2
    elif (potez<=9) and (0 in player1) and (3 in player1) and (6 in player1):
        winner = 1
    elif (potez<=9) and (0 in player2) and (3 in player2) and (6 in player2):
        winner = 2
    elif (potez<=9) and (1 in player1) and (4 in player1) and (7 in player1):
        winner = 1
    elif (potez<=9) and (1 in player2) and (4 in player2) and (7 in player2):
        winner = 2
    elif (potez<=9) and (2 in player1) and (5 in player1) and (8 in player1):
        winner = 1
    elif (potez<=9) and (2 in player2) and (5 in player2) and (8 in player2):
        winner = 2
    elif (potez<=9) and (0 in player1) and (4 in player1) and (8 in player1):
        winner = 1
    elif (potez<=9) and (0 in player2) and (4 in player2) and (8 in player2):
        winner = 2
    elif (potez<=9) and (2 in player1) and (4 in player1) and (6 in player1):
        winner = 1
    elif (potez<=9) and (2 in player2) and (4 in player2) and (6 in player2):
        winner = 2

    if winner == 1:
        messagebox.showinfo(title="CONGRATULATIONS!", message="PLAYER 1 HAS WON, PLAYER 2 IS STUPID.")
    elif winner == 2:
        messagebox.showinfo(title="CONGRATULATIONS!", message="PLAYER 2 HAS WON, PLAYER 1 IS STUPID.")
    elif (winner == -1) and (potez == 9):
        messagebox.showinfo(title="CONGRATULATIONS!", message="TIED. YOU TWO ARE SMART PEOPLE")

buttons = []
for id in range(9):
    button = tk.Button(window,text=' ', height=2, width=6, font=helv36 )
    button.grid(column=id % 3, row=id // 3)
    buttons.append(button)

for ind,el in enumerate(buttons):
    el.config(command = lambda ind=ind:OnClick(ind))





window.mainloop()
