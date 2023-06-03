import tkinter as tk

root = tk.Tk()

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()  # you can use this if you want full screen height

print("Screen width:", screen_width)
print("Screen height:", screen_height)

root.mainloop()
