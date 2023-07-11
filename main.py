from tkinter import *

window = Tk()
label = Label(text="First tkinter line")
label.place(x=100, y=200)
canvas = Canvas(window, bg='white')
# window.geometry("400x400")
def callback(event):
    print ("clicked at", event.x, event.y)
    canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, outline='black', fill='black')
canvas.bind("<Button-1>", callback)
canvas.pack(fill=BOTH, expand=True)
window.maxsize(800, 800)
window.mainloop()