import tkinter as tk
from ui.main_window import build_main_window

root = tk.Tk()
root.title("Simple Order App")
root.geometry("400x400")

build_main_window(root)

root.mainloop()