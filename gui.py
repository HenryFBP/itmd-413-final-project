from tkinter import *
import pygubu

class Application:
    def __init__(self, master, path="./gui.ui"):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file(path)

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow', master)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()