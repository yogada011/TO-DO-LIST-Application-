from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
import datetime

# function to enter the task in the Listbox
def entertask():
    input_text=""
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            priority = priority_var.get()
            task = f"{input_text} [{priority}]"
            listbox_task.insert(END, task)
            root1.destroy()
    
    root1 = Tk()
    root1.title("Add task")
    
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    
    # Priority dropdown menu
    priority_var = StringVar(root1)
    priority_var.set("Low")  # default value
    priority_menu = OptionMenu(root1, priority_var, "High", "Medium", "Low")
    priority_menu.pack()
    
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    
    root1.mainloop()


# Function to delete task from the Listbox
def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])


# Function to mark completed
def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked = listbox_task.get(marked)
    temp_marked = temp_marked + " ✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


# Function to edit a selected task
def edittask():
    selected = listbox_task.curselection()
    if selected:
        selected_task = listbox_task.get(selected[0])
        new_task = simpledialog.askstring("Edit Task", f"Edit task: {selected_task}")
        if new_task:
            listbox_task.delete(selected[0])
            listbox_task.insert(selected[0], new_task)


# Function to search tasks
def searchtask():
    search_text = simpledialog.askstring("Search Task", "Enter task to search")
    if search_text:
        for idx in range(listbox_task.size()):
            task = listbox_task.get(idx)
            if search_text.lower() in task.lower():
                listbox_task.selection_set(idx)
                listbox_task.activate(idx)
                break
        else:
            tkinter.messagebox.showinfo("Not Found", "Task not found")


# Function to save tasks to a file
def savetasks():
    with open("tasks.txt", "w") as f:
        tasks = listbox_task.get(0, END)
        for task in tasks:
            f.write(task + "\n")
    tkinter.messagebox.showinfo("Save", "Tasks saved successfully")


# Function to load tasks from a file
def loadtasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox_task.insert(END, task.strip())
    except FileNotFoundError:
        tkinter.messagebox.showwarning("Error", "No saved tasks found")


# Creating the initial window
window = Tk()
window.title("Py To_Do_APP")

# Frame to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()

# Listbox to hold tasks
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Arial")
listbox_task.pack(side=LEFT)

# Scrollbar
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Button widgets
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

edit_button = Button(window, text="Edit selected task", width=50, command=edittask)
edit_button.pack(pady=3)

search_button = Button(window, text="Search task", width=50, command=searchtask)
search_button.pack(pady=3)

save_button = Button(window, text="Save tasks to file", width=50, command=savetasks)
save_button.pack(pady=3)

load_button = Button(window, text="Load tasks from file", width=50, command=loadtasks)
load_button.pack(pady=3)

window.mainloop()
