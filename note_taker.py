from tkinter import *

root = Tk()
root.title("Sophia's Note Takler")
root.option_add("*Font", "Consolas 20")
root.geometry("400x800")


def open_new_note():
    print("Open new not window")
    new_note_window = Toplevel(root)

    new_note_title = Label(new_note_window, text="New Note",bg="black", fg="white")
    new_note_title.grid()

    title_label = Label(new_note_window, text="Title:",bg="black", fg="white")
    title_label.grid()

    title_entry = Entry(new_note_window)
    title_entry.grid()

    note_label = Label(new_note_window, text="Note Text",bg="black", fg="white")
    note_label.grid()

    note_entry = Entry(new_note_window)
    note_entry.grid()


def open_list(list_name):
    print("Open a list")


lbl_title = Label(root, text="Notes")
lbl_title.config(font=("Calibri", "30"), bg="black", fg="white", width=20)
lbl_title.grid(row=0, sticky=E + W)

btn_newnote = Button(root, text="+New Note", command=lambda: open_new_note())
btn_newnote.config(bg="black", fg="white")
btn_newnote.grid(row=1, sticky=W)

btn_shopping = Button(root, text="Shopping List", command=lambda: open_list(shopping))
btn_shopping.config(bg="black", fg="white", width=20)
btn_shopping.grid(row=2, sticky=E + W)

btn_todo = Button(root, text="To Do List", command=lambda: open_list(todo))
btn_todo.config(bg="black", fg="white", width=20)
btn_todo.grid(row=3, sticky=E + W)

btn_homework = Button(root, text="Homework WK 1", command=lambda: open_list(homework))
btn_homework.config(bg="black", fg="white", width=20)
btn_homework.grid(row=4, sticky=E + W)

root.mainloop()
