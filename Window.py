from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

from Constants import *

#A parent class for frames, handles windows and navigation
class Window:
    def __init__(self, tk, parent=None):
        self._parent = parent
        self._frame = Frame(tk, bg=PRIMARY)
        self._master = self._frame.master
        self._frame.grid(row=0, sticky="nsew")
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        print(self._frame)
        pass

    def _showFrame(self):
        self._frame.tkraise()

    def _goBack(self):
        self._parent._frame.tkraise()

    def getFont(self, fontName="Helvetica", fontSize=14):
        return tkFont.Font(family=fontName, size=fontSize)

    def _showMessage(self, title, message):
        messagebox.showerror(title, message)
