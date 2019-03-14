class Note:
    def __init__(self, title, text, category):
        self.__title = title
        self.__text = text
        self.__category = category

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_category(self):
        return self.__category


from tkinter import *

root = Tk()
root.title("Sophia's Note Takler")
root.option_add("*Font", "Consolas 20")
root.geometry("400x800")

notes = []


def save_note(window, title, body, category="Shopping"):

    new_note = Note(title.capitalize().strip(),
                    body.capitalize().strip(),
                    category.capitalize().strip())

    notes.append(new_note)
    print("Title:{}".format(new_note.get_title()))
    print("Body:{}".format(new_note.get_text()))
    print("Category:{}".format(new_note.get_category()))
    window.destroy()


def open_new_note(category):
    print("Open new not window")
    title_value = StringVar()


    new_note_window = Toplevel(root)

    new_note_title = Label(new_note_window, text="New Note")
    new_note_title.config(bg="black", fg="white")
    new_note_title.grid(sticky=E + W)

    title_label = Label(new_note_window, text="Title:")
    title_label.config(bg="black", fg="white")
    title_label.grid(sticky=W)

    title_entry = Entry(new_note_window, textvariable=title_value)
    title_entry.grid()

    note_label = Label(new_note_window, text="Note Text:")
    note_label.config(bg="black", fg="white")
    note_label.grid(sticky=W)

    note_text = Text(new_note_window)
    note_text.config(height=10, width=20)
    note_text.grid()

    button_frame = Frame(new_note_window)
    button_frame.grid()

    cancel_button = Button(button_frame, text="Cancel", command=new_note_window.destroy)
    cancel_button.config(bg="black", fg="white", )
    cancel_button.grid(row=0, column=1, sticky=E)

    save_button = Button(button_frame,
                         text="Save",
                         command=lambda: save_note(new_note_window, title_value.get(), note_text.get(1.0, END),
                                                   category))
    save_button.config(bg="black", fg="white")
    save_button.grid(row=0, column=2, sticky=E)


def open_list(list_category):
    print("Open {}".format(list_category))
    list_window = Toplevel(root)
    list_window.title(list_category)
    list_window.geometry("600x400")

    for note in notes:
        title = note.get_title()
        body = note.get_text()
        category = note.get_category()

        note_text = "***{}***\n{}\n".format(title, body)
        if category == list_category:
          Label(list_window, text=note_text).grid(sticky=W)


lbl_title = Label(root, text="Notes")
lbl_title.config(font=("Calibri", "30"), bg="black", fg="white", width=18)
lbl_title.grid(row=0, sticky=N + S + E + W)

btn_shopping_new = Button(root, text="Shopping List", command=lambda: open_list("Shopping"))
btn_shopping_new.config(bg="black", fg="white")
btn_shopping_new.grid(column=0, row=1, sticky=E + W)

btn_shopping = Button(root, text="+", command=lambda: open_new_note("Shopping"))
btn_shopping.config(bg="white", fg="black")
btn_shopping.grid(column=1, row=1, sticky=E + W)

btn_todo = Button(root, text="To Do List", command=lambda: open_list("To_do_list"))
btn_todo.config(bg="black", fg="white")
btn_todo.grid(column=0, row=2, sticky=E + W)

btn_todo_new = Button(root, text="+", command=lambda: open_new_note("Shopping"))
btn_todo_new.config(bg="white", fg="black")
btn_todo_new.grid(column=1, row=2, sticky=E + W)

btn_homework = Button(root, text="Homework WK1", command=lambda: open_list("Homework_WK1"))
btn_homework.config(bg="black", fg="white")
btn_homework.grid(column=0, row=3, sticky=E + W)

btn_homework_new = Button(root, text="+", command=lambda: open_new_note("Shopping"))
btn_homework_new.config(bg="white", fg="black")
btn_homework_new.grid(column=1, row=3, sticky=E + W)

root.mainloop()
