from tkinter import *
from Constants import *
from Dashboard import *
from Window import *


root = Tk()
window = Dashboard(root)
root.title(APP_TITLE) 

root.resizable(False, False) #disabling window resize
root.configure(background=PRIMARY)

root.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.mainloop()
