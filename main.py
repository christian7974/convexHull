from tkinter import *

window = Tk()
label = Label(text="First tkinter line")
label.pack()

window.geometry("400x400")

window.maxsize(1000, 1000)
window.mainloop()