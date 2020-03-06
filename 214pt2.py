import tkinter as tk 

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

# blue screen
blue = tk.Frame(root)
blue.grid(row = 0, column = 0)
blue.config(height = "100", width = "125", bg = "blue")

# red screen
red = tk.Frame(root)
red.grid(row = 1, column = 0)
red.config(height = "100", width = "125", bg = "red")

# yellow screen
yellow = tk.Frame(root)
yellow.grid(row = 1, column = 1)
yellow.config(height = "100", width = "75", bg = "yellow")

# green screen
green = tk.Frame(root)
green.grid(row = 0, column = 1)
green.config(height = "100", width = "75", bg = "lime green")

root.mainloop()