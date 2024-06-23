import tkinter as tk
from tkinter import messagebox

# Create the root window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Add a title label
lbl_title = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
lbl_title.pack(pady=10)

# Create a frame for the listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a listbox
listbox = tk.Listbox(frame, width=40, height=10, bd=0, font=("Helvetica", 12))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Entry box for new tasks
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Function to add a task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        # Mark the task as completed
        task = task + " [Completed]"
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, task)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to complete.")

# Add buttons to add, delete, and complete tasks
btn_add_task = tk.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.pack(pady=5)

btn_delete_task = tk.Button(root, text="Delete Task", fg="red", bg="white", command=delete_task)
btn_delete_task.pack(pady=5)

btn_complete_task = tk.Button(root, text="Complete Task", fg="blue", bg="white", command=complete_task)
btn_complete_task.pack(pady=5)

# Start the main event loop
root.mainloop()