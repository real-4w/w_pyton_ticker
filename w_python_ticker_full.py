import yaml
import tkinter as tk
from itertools import cycle

# Load ticker messages from yaml file
def load_ticker_text(file_path):
    with open(file_path, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
    return data['messages']

# Ticker Tape Class
class TickerTape:
    def __init__(self, master, messages):
        self.master = master
        self.messages = cycle(messages) # to cycle through the list of messages
        self.label = tk.Label(master, text='', font=("Helvetica", 16), bg='black', fg='white', anchor='w')
        self.label.pack(fill='x')

    # Run the ticker
    def run(self):
        self.master.after(1000, self.update) # Update every 1 second

    # Update the label with the next message
    def update(self):
        message = next(self.messages)
        message = message + ' ' * 10 # pad the message
        self.show_message(message, message)

    def show_message(self, full_message, current_message):
        self.label.config(text=current_message)
        if len(full_message) > len(current_message):
            self.master.after(100, lambda: self.show_message(full_message, current_message[1:]))
        else:
            self.master.after(1000, self.update) # Update every 1 second

# Main
if __name__ == "__main__":
    messages = load_ticker_text('ticker_text.yaml')
    root = tk.Tk()
    root.geometry("1000x60") # This should be adjusted to the size of your screen
    ticker = TickerTape(root, messages)
    ticker.run()
    root.mainloop()
