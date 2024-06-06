from tkinter import *  

# Function to add a task
def add_task():
    task = task_var.get().strip()
    if task:
        tasks.append(task)
        update_task_listbox()
        task_var.set("")
        save_tasks()

# Function to edit a task
def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_task = task_listbox.get(selected_index)

        # Creating New Window to edit a task
        edit_window = Toplevel(root)
        edit_window.title("Edit Task")
        edit_window.geometry("450x200")
        edit_window.configure(bg="#2c2d2e")

        # Creating label for "Edit Your Tasks"
        edit_label=Label(edit_window, text="Edit Your Tasks",font=("",20,"bold"),bg="#2c2d2e",fg="white")
        edit_label.grid(row=0, column=0, padx=0, pady=10)

        # creating Input box to Edit Tasks
        edited_task_entry =Entry(edit_window, width=25 ,font=("",20))
        edited_task_entry.grid(row=1, column=0,padx=50, pady=10)
        save_button = Button(edit_window, text="Save",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#5452f1",width=8, command=lambda: save_edited_task(edit_window, selected_index, edited_task_entry))
        save_button.grid(row=2, column=0, padx=5, pady=10)
        edited_task_entry.insert(END, selected_task)
        edit_window.mainloop()

# Function to save edited task
def save_edited_task(edit_window, selected_index, edited_task_entry):
    edited_task = edited_task_entry.get().strip()
    if edited_task:
        tasks[selected_index[0]] = edited_task
        update_task_listbox()
        save_tasks()
        edit_window.destroy()

# Function to delete a task
def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        del tasks[selected_index[0]]
        update_task_listbox()
        save_tasks()

# Function to update the listbox with tasks
def update_task_listbox():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks.extend(line.strip() for line in f.readlines())
            update_task_listbox()
    except FileNotFoundError:
        pass

# Function to save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Creating tasks list
tasks = []

# Create the main window
root = Tk()
root.title("To-Do List App")
root.geometry("480x500")
root.configure(bg="#2c2d2e")

# Creating label for "Enter Your Tasks"
task_label=Label(root, text="Enter Your Tasks",font=("",20,"bold"),bg="#2c2d2e",fg="white")
task_label.grid(row=0, column=0, padx=0, pady=10)

# creating enter to add tasks
task_var = StringVar()
task_entry = Entry(root, textvariable=task_var, width=25 ,font=("",20))
task_entry.grid(row=1, column=0, padx=50, pady=10)

# Add Button to add tasks
add_button = Button(root, text="Add",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#5452f1",width=8, command=add_task)
add_button.grid(row=2, column=0,  pady=10)

# Listbox to display tasks
task_listbox = Listbox(root, width=35,font=("",15))
task_listbox.grid(row=3, column=0, padx=50, pady=5)

# Frame for Buttons
frame1=Frame(root)
frame1.configure(bg="#2c2d2e")
frame1.grid(row=4, column=0, padx=5, pady=5)
# Button to edit tasks
edit_button = Button(frame1, text="Edit",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#1f862a",width=8, command=edit_task)
edit_button.grid(row=0, column=0, padx=60, pady=5)

# Button to delete tasks
delete_button = Button(frame1, text="Delete", font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#e71d18",width=8,command=delete_task)
delete_button.grid(row=0, column=1, padx=60, pady=5)

# Load tasks from file
load_tasks()


root.mainloop()
