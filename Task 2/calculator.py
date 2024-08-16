import tkinter as tk
from math import sqrt

# Function to update the input field
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            if input_var.get().isdigit():
                value = int(input_var.get())
            else:
                value = eval(input_var.get())
            input_var.set(value)
            display.update()
        except Exception as e:
            input_var.set("Error")
            display.update()
    elif text == "C":
        input_var.set("")
        display.update()
    elif text == "√":
        try:
            value = str(sqrt(float(input_var.get())))
            input_var.set(value)
            display.update()
        except Exception as e:
            input_var.set("Error")
            display.update()
    elif text == "←":
        current_text = input_var.get()
        input_var.set(current_text[:-1])
        display.update()
    else:
        input_var.set(input_var.get() + text)
        display.update()

# Creating the GUI window
root = tk.Tk()
root.title("Advanced Calculator")

# Input field for the calculator
input_var = tk.StringVar()
input_var.set("")
display = tk.Entry(root, textvar=input_var, font="lucida 20 bold", bd=10, relief=tk.SUNKEN)
display.pack(fill=tk.BOTH, ipadx=8)

# Creating the buttons frame
button_frame = tk.Frame(root)
button_frame.pack()

# List of button texts
buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "√",
    "1", "2", "3", "-", "%",
    "0", ".", "+", "**", "=",
    "←"
]

# Adding buttons to the frame
row, col = 0, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="lucida 15 bold", padx=20, pady=20)

    # Set the clear button to be red
    if button_text == "C":
        button.config(bg="red", fg="white")
    
    # Place buttons in the grid
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col == 5:
        col = 0
        row += 1

root.mainloop()
