from utils import show_error, cbox, open_data, plot_region, tk, window

tk.Tk.report_callback_exception = show_error

tk.Button(text='Open file', command=open_data).pack()
tk.Button(text='Plot', command=plot_region).pack()

cbox.pack()

window.mainloop()
