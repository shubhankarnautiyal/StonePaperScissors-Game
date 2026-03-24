import tkinter as tk
import random
from playsound import playsound
import threading

# sound function (runs in background)
def play_sound(file):
    threading.Thread(target=playsound, args=(file,), daemon=True).start()

# main data
choices = ["stone", "paper", "scissors"]
user_score = 0
computer_score = 0
round_num = 0
max_round = 5

# play function
def play(user_choice):
    global user_score, computer_score, round_num

    if round_num >= max_round:
        result_label.config(text="Game Over! Restart to play again")
        return

    round_num += 1

    computer_choice = random.choice(choices)

    # update images
    user_img_label.config(image=images[user_choice])
    comp_img_label.config(image=images[computer_choice])

    # animation effect
    result_label.config(text="Playing...", fg="yellow")
    root.update()
    root.after(300)

    # logic
    if user_choice == computer_choice:
        result = "Draw"
        color = "orange"
        play_sound("draw.mp3")

    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):

        user_score += 1
        result = "You Win!"
        color = "green"
        play_sound("win.mp3")

    else:
        computer_score += 1
        result = "Computer Wins!"
        color = "red"
        play_sound("lose.mp3")

    result_label.config(text=result, fg=color)

    score_label.config(
        text=f"Round {round_num}/5    You: {user_score}   Computer: {computer_score}"
    )

    # final winner
    if round_num == max_round:
        if user_score > computer_score:
            winner_label.config(text="🏆 YOU WON THE GAME!", fg="green")
        elif computer_score > user_score:
            winner_label.config(text="💻 COMPUTER WON!", fg="red")
        else:
            winner_label.config(text="GAME DRAW!", fg="orange")


# restart
def restart():
    global user_score, computer_score, round_num
    user_score = 0
    computer_score = 0
    round_num = 0

    score_label.config(text="Round 0/5    You: 0   Computer: 0")
    result_label.config(text="Choose your move", fg="white")
    winner_label.config(text="")

    user_img_label.config(image=blank)
    comp_img_label.config(image=blank)


# window
root = tk.Tk()
root.title("Professional Stone Paper Scissors")
root.geometry("600x500")
root.config(bg="#0f172a")

# load images
blank = tk.PhotoImage(width=150, height=150)

images = {
    "stone": tk.PhotoImage(file="stone.png"),
    "paper": tk.PhotoImage(file="paper.png"),
    "scissors": tk.PhotoImage(file="scissors.png")
}

# title
tk.Label(root, text="Stone Paper Scissors",
         font=("Arial", 24, "bold"),
         bg="#0f172a", fg="cyan").pack(pady=10)

# score
score_label = tk.Label(root,
                       text="Round 0/5    You: 0   Computer: 0",
                       font=("Arial", 14),
                       bg="#0f172a", fg="white")
score_label.pack()

# image frame
frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=20)

user_img_label = tk.Label(frame, image=blank, bg="#0f172a")
user_img_label.grid(row=0, column=0, padx=50)

comp_img_label = tk.Label(frame, image=blank, bg="#0f172a")
comp_img_label.grid(row=0, column=1, padx=50)

# result
result_label = tk.Label(root,
                        text="Choose your move",
                        font=("Arial", 18, "bold"),
                        bg="#0f172a", fg="white")
result_label.pack()

# winner
winner_label = tk.Label(root,
                        text="",
                        font=("Arial", 20, "bold"),
                        bg="#0f172a")
winner_label.pack()

# buttons
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="STONE", width=12,
          command=lambda: play("stone"),
          bg="#3b82f6", fg="white").grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="PAPER", width=12,
          command=lambda: play("paper"),
          bg="#22c55e", fg="white").grid(row=0, column=1, padx=10)

tk.Button(btn_frame, text="SCISSORS", width=12,
          command=lambda: play("scissors"),
          bg="#ef4444", fg="white").grid(row=0, column=2, padx=10)

# restart
tk.Button(root, text="Restart",
          font=("Arial", 14),
          command=restart,
          bg="orange").pack()

root.mainloop()