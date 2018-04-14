from tkinter import Tk

from GuiLootCrateGraph import GuiLootCrateGraph
from gui_pygubu import MainGUI

if __name__ == '__main__':
    root = Tk()
    root.withdraw()  # don't show blank window

    app = MainGUI(root)
    graph = GuiLootCrateGraph(root)
    root.mainloop()
