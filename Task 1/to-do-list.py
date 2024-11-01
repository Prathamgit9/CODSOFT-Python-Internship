import tkinter as tk
from tkinter import messagebox, filedialog
import os

# Task Manager Class
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x500")

        # Task List
        self.tasks = []

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Task Manager", font=("Arial", 18))
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.root, textvariable=self.task_var, font=("Arial", 12), width=30)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(self.root, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, height=10, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar for Task Listbox
        self.scrollbar = tk.Scrollbar(self.task_listbox)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Buttons Frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5)

        # Update, Delete, Save, Load Buttons
        self.update_task_button = tk.Button(self.button_frame, text="Update Task", font=("Arial", 12), command=self.update_task)
        self.update_task_button.grid(row=0, column=0, padx=10)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", font=("Arial", 12), command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=10)

        self.save_task_button = tk.Button(self.button_frame, text="Save Tasks", font=("Arial", 12), command=self.save_tasks)
        self.save_task_button.grid(row=0, column=2, padx=10)

        self.load_task_button = tk.Button(self.button_frame, text="Load Tasks", font=("Arial", 12), command=self.load_tasks)
        self.load_task_button.grid(row=0, column=3, padx=10)

    # Add a task to the task list
    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_var.set("")  # Clear the entry field
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")

    # Update the selected task
    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_var.get().strip()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
                self.task_var.set("")
            else:
                messagebox.showwarning("Input Error", "Task cannot be empty.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    # Delete the selected task
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    # Update the task listbox with tasks
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear current list
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Add all tasks to the listbox

    # Save tasks to a file
    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as f:
                for task in self.tasks:
                    f.write(task + '\n')
            messagebox.showinfo("Save Successful", f"Tasks saved to {file_path}")

    # Load tasks from a file
    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.update_task_listbox()
            messagebox.showinfo("Load Successful", f"Tasks loaded from {file_path}")
        else:
            messagebox.showwarning("File Error", "File not found or invalid.")


# Main function to run the Task Manager App
if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()
