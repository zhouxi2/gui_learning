import tkinter

root=tkinter.Tk()
root.title("Hello World!!!")
root.geometry("600x200")

my_label=tkinter.Label(root)
my_label.config(text="Hello",fg="green")
my_label.grid()

root.mainloop()