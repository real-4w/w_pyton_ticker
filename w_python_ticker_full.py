import yaml
import tkinter as tk
from itertools import cycle
from tkinter import font as tkFont

# Load ticker messages from yaml file
def load_ticker_text(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data['messages']

class TickerTape:
    def __init__(self, master, messages):
        self.master = master
        self.messages = cycle(messages)
        self.font = tkFont.Font(font=("Helvetica", 16))
        self.label = tk.Label(master, text='', font=self.font, fg='black')
        self.label.pack(fill='x')
        self.text_pixel_width = 0

    def scroll(self):
        x = self.label.winfo_x() - 5  # Move left by 5 pixels

        if x + self.text_pixel_width <= 0:
            self.update()
            self.label.place(x=self.master.winfo_screenwidth())  # Reset position to the right edge
        else:
            self.label.place(x=x)
        
        self.master.after(100, self.scroll)  # Continue to scroll

    def update(self):
        message = next(self.messages)
        self.text_pixel_width = self.font.measure(message)
        self.label.configure(text=message)

    def run(self):
        self.update()
        self.scroll()


# Close the window with 'Esc' key
def on_escape(event):
    root.quit()
# Main
if __name__ == "__main__":
    messages = load_ticker_text('ticker_text.yaml')
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    root.geometry(f"{screen_width}x40+0+0")
    root.configure(bg='white')  # Set background color of window to white
    root.attributes('-topmost', True)
    root.attributes('-transparentcolor', 'white')  # This makes only the white color transparent
    root.overrideredirect(True)
    root.bind('<Escape>', on_escape)
    ticker = TickerTape(root, messages)
    ticker.run()
    root.mainloop()
