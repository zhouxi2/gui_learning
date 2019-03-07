from tkinter import *
import Note2

root = Tk()
root.title("Sophia's Note Takler")
root.option_add("*Font", "Consolas 20")
root.geometry("400x800")


def open_new_note():
    print("Open new not window")
    title_value=StringVar()
    text_value=StringVar()

    new_note_window = Toplevel(root)

    new_note_title = Label(new_note_window, text="New Note")
    new_note_title.config(bg="black", fg="white")
    new_note_title.grid(sticky=E + W)

    title_label = Label(new_note_window, text="Title:")
    title_label.config(bg="black", fg="white")
    title_label.grid(sticky=W)

    title_entry = Entry(new_note_window,textvariable=title_value)
    title_entry.grid()

    note_label = Label(new_note_window, text="Note Text")
    note_label.config(bg="black", fg="white")
    note_label.grid(sticky=W)

    note_text = Text(new_note_window, textvariable=text_value)
    note_text.config(height=10, width=20)
    note_text.grid()

    button_frame = Frame(new_note_window)
    button_frame.grid()

    cancel_button = Button(button_frame, text="Cancel", command = new_note_window.destroy)
    cancel_button.config(bg="black", fg="white", command= save_note())
    cancel_button.grid(row=0, column=1, sticky=E)

    save_button = Button(button_frame, text="Save")
    save_button.config(bg="black", fg="white")
    save_button.grid(row=0, column=2, sticky=E)


def open_list(list_name):
    print("Open a list")


lbl_title = Label(root, text="Notes")
lbl_title.config(font=("Calibri", "30"), bg="black", fg="white", width=20)
lbl_title.grid(row=0, sticky=E + W)

btn_newnote = Button(root, text="+ New Note", command=lambda: open_new_note())
btn_newnote.config(bg="black", fg="white")
btn_newnote.grid(row=1, sticky=W)

btn_shopping = Button(root, text="+ Shopping List", command=lambda: open_list("Shopping"))
btn_shopping.config(bg="black", fg="white", width=20)
btn_shopping.grid(row=2, sticky=E + W)

btn_todo = Button(root, text="+ To Do List", command=lambda: open_list("To_do_list"))
btn_todo.config(bg="black", fg="white", width=20)
btn_todo.grid(row=3, sticky=E + W)

btn_homework = Button(root, text="+ Homework WK1", command=lambda: open_list("Homework_WK1"))
btn_homework.config(bg="black", fg="white", width=20)
btn_homework.grid(row=4, sticky=E + W)

root.mainloop()
