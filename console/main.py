from tkinter import Tk, ttk

from munchkin.base.settings import build_settings
from munchkin.munchkin import munchkin

print(munchkin())
build_settings()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
