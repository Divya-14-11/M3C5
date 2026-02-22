from tkinter import *
from tkinter import messagebox
import random

# Main window
window = Tk()
window.geometry("400x400")
window.title("Main Window")
window.config(bg="#1e1e2f")

l = Label(window,text="Rock Paper Scissors Game",font=("Segoe UI", 16, "bold"), bg="#1e1e2f",fg="white")
l.pack()

# Game window function
def game_window():
    top = Toplevel()
    top.geometry("400x400")
    top.title("Rock Paper Scissors")
    top.config(bg="#2a2a40")

    choices = ["Rock", "Paper", "Scissors"]

    player_label = Label(top,text="Player Choice: ",font=("Segoe UI", 12),bg="#2a2a40",fg="white")
    player_label.pack()

    computer_label = Label(top,Text="Computer Choice: ",font=("Segoe UI", 12),bg="#2a2a40",fg="white" )
    computer_label.pack()

    # Game logic
    def play(choice):
        computer_choice = random.choice(choices)

        player_label.config(text="Player Choice: " + choice)
        computer_label.config(text="Computer Choice: " + computer_choice)

        if choice == computer_choice:
            messagebox.showinfo("Result", "It's a Tie!")
        elif (
            (choice == "Rock" and computer_choice == "Scissors") or
            (choice == "Paper" and computer_choice == "Rock") or
            (choice == "Scissors" and computer_choice == "Paper")
        ):
            messagebox.showinfo("Result", "🎉 You Win!")
        else:
            messagebox.showinfo("Result", "😢 Computer Wins!")
    def rock():
        play("Rock")

    def paper():
        play("Paper")

    def scissors():
        play("Scissors")

    def reset():
        player_label.config(text="Player Choice: ")
        computer_label.config(text="Computer Choice: ")

    # Button style (CSS-like)
    btn_style = {
        "width": 15,
        "font": ("Segoe UI", 11, "bold"),
        "bg": "#4cafef",
        "fg": "white",
        "bd": 0,
    }

    Button(top, text="Rock", command=rock, **btn_style).pack()
    Button(top, text="Paper", command=paper, **btn_style).pack()
    Button(top, text="Scissors", command=scissors, **btn_style).pack()

    Button(
        top,
        text="Reset Game",
        width=15,
        font=("Segoe UI", 11, "bold"),
        bg="#ff5252",
        fg="white",
        command=reset)
    Button.pack()

# Start Game button
Button(
    window,
    text="Start Game",
    font=("Segoe UI", 14, "bold"),
    bg="#00c853",
    fg="white",
    width=16,
    command=game_window).pack()

window.mainloop()