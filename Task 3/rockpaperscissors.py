import tkinter as tk
import random
from tkinter import messagebox

# Game logic to determine the winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice and update the game
def play(user_choice):
    comp_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, comp_choice)
    
    # Update choice display
    user_choice_label.config(text=f"You chose: {user_choice}", bg="#4caf50")
    comp_choice_label.config(text=f"Computer chose: {comp_choice}", bg="#f44336")
    
    # Update result text with animation
    result_label.config(text=f"Result: {result}", fg="green" if result == "You win!" else "red")
    result_label.after(100, lambda: result_label.config(fg="white"))
    
    # Update score
    if result == "You win!":
        global user_score
        user_score += 1
    elif result == "Computer wins!":
        global comp_score
        comp_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

# Function to reset the game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_choice_label.config(text="You chose: ", bg="white")
    comp_choice_label.config(text="Computer chose: ", bg="white")
    result_label.config(text="Make your move!", fg="white")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Function to end the game and display final message
def end_game():
    if user_score > comp_score:
        final_message = f"Congratulations! You won the game with a score of {user_score} to {comp_score}!"
    elif user_score < comp_score:
        final_message = f"Better luck next time! The computer won with a score of {comp_score} to {user_score}."
    else:
        final_message = f"It's a tie! Both you and the computer scored {user_score}."

    if messagebox.askyesno("Game Over", f"{final_message}\n\nDo you want to play again?"):
        reset_game()
    else:
        window.destroy()  # Properly close the window if the user clicks 'No'

# Main application window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x600")
window.config(bg="#1e1e1e")

# Scores
user_score = 0
comp_score = 0

# Result label
result_label = tk.Label(window, text="Make your move!", font=("Helvetica", 18), bg="#1e1e1e", fg="white")
result_label.pack(pady=20)

# Score label
score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Helvetica", 14), bg="#1e1e1e", fg="#00ff00")
score_label.pack()

# Choice display frame
choice_frame = tk.Frame(window, bg="#1e1e1e")
choice_frame.pack(pady=20, fill="x")

user_choice_label = tk.Label(choice_frame, text="You chose: ", font=("Helvetica", 14), bg="white", fg="black", width=20, height=5)
user_choice_label.pack(side="left", padx=20)

comp_choice_label = tk.Label(choice_frame, text="Computer chose: ", font=("Helvetica", 14), bg="white", fg="black", width=20, height=5)
comp_choice_label.pack(side="right", padx=20)

# Buttons for Rock, Paper, Scissors
button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=12, height=2, command=lambda: play("Rock"), bg="#333", fg="white", activebackground="#444", activeforeground="white")
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=12, height=2, command=lambda: play("Paper"), bg="#333", fg="white", activebackground="#444", activeforeground="white")
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=12, height=2, command=lambda: play("Scissors"), bg="#333", fg="white", activebackground="#444", activeforeground="white")
scissors_button.grid(row=0, column=2, padx=10)

# Reset button
reset_button = tk.Button(window, text="Reset Game", command=reset_game, bg="orange", fg="white", height=2, width=15)
reset_button.pack(pady=10)

# End game button
end_button = tk.Button(window, text="End Game", command=end_game, bg="red", fg="white", height=2, width=15)
end_button.pack(pady=10)

# Closing the game properly
window.protocol("WM_DELETE_WINDOW", end_game)

# Start the GUI event loop
window.mainloop()
