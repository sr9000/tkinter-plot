import tkinter as tk
import traceback
from tkinter import filedialog as fd
from tkinter import messagebox, ttk

from plot import plot
from why_not_f_ckin_csv import parse_not_f_ckin_csv

__all__ = ['tk', 'cbox', 'regions', 'show_error', 'open_data', 'plot_region', 'window']

window = tk.Tk()
cbox = ttk.Combobox(values=[])
regions = None


def show_error(self, *args):
    err = traceback.format_exception(*args)
    messagebox.showerror('Exception', err)


def open_data():
    global regions, cbox
    name = fd.askopenfilename()
    if not name:
        return
    regions = parse_not_f_ckin_csv(name)
    cbox.destroy()

    cbox = ttk.Combobox(values=list(regions.keys()))
    cbox.pack()


def plot_region():
    i = cbox.current()
    if i < 0 or regions is None:
        return
    reg = cbox['values'][i]
    plot(reg, regions[reg])
