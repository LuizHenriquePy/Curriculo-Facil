from tkinter import *

root = Tk()

a = Entry(root)
a.pack()

a.insert(0, "Luiz")

a.config(state="disabled")

root.mainloop()
