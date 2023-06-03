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
        self.label = tk.Label(master)
        self.label.pack()

    # Run the ticker
    def run(self):
        self.master.after(1000, self.update) # Update every 1 second

    # Update the label with the next message
    def update(self):
        self.label.config(text=next(self.messages))
        self.master.after(1000, self.update) # Update every 1 second

# Main
if __name__ == "__main__":
    messages = load_ticker_text('ticker_text.yaml')
    root = tk.Tk()
    ticker = TickerTape(root, messages)
    ticker.run()
    root.mainloop()
