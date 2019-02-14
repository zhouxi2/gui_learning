import tkinter
root=tkinter.Tk()

root.tiltle("Hello World!!!")
root.geometry("600x200")

my_lable=tkinter.Lable(root)
my_lable.config(text="Hello",fg="green")
my_lable.grid()

root.mainloop()