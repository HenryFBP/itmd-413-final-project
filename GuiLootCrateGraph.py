from pprint import *
import matplotlib as mpl
import numpy as np
import tkinter as tk

from pygubu import *

from Game import *
from GuiLootItem import *
from GuiLootCrateGraph import *
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class GuiLootCrateGraph:

    def __init__(self, master, path='./gui_graph.ui'):
        # 1: Create a builder
        self.builder = Builder()

        # 2: Load an ui file
        self.builder.add_from_file(path)

        # 3: Create the widget using a master as parent
        self.mainwindow: Toplevel = self.builder.get_object('mainwindow', master)

        # get canvas object for GRAFFIN STUFF
        self.canvas: Canvas = self.builder.get_object('CanvasGraph', master)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        self.canvas = FigureCanvasTkAgg(f, self.canvas)
        self.canvas.show()
        self.canvas._tkcanvas.pack()
