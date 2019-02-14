import tkinter
root=tkinter.Tk()

root.tiltle("Hello World!!!")
root.geometry("600x200")

my_label=tkinter.Lable(root)
my_label.config(text="Hello",fg="green")
my_label.grid()

root.mainloop()