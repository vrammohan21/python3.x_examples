""" tkinter = tk + inter. tk= Tool Kit & inter= Interface. tkinter is a standard
    Python interface to the Tk GUI toolkit"""
import tkinter as tk
root=tk.Tk()#root is the main window in which we will place all our widgets.
root.title("My Imventory Management System")
root.geometry("800x600")

#Label widget is used to display one or more lines of text that users can’t modify.
product_label=tk.Label(root,text="Enter the name of the Product")
product_label.pack()#pack() is used to place the widget on the window.
product_name=tk.Entry(root)
product_name.pack()#pack() is used to place the widget on the window.
root.mainloop()#This is the main event loop that waits for events to happen.