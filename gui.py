from tkinter import *

root = Tk()

def quit(e):
    root.destroy()

buttonQuit = Button(root, text="exit")
buttonQuit.pack()
buttonQuit.bind('<Button-1>', quit)

print("Before mainloop")
root.mainloop()
