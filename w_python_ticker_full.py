import yaml, tkinter as tk
from itertools import cycle

def load_ticker_text(file_path):                                        
    with open(file_path, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
    return data['messages']

class TickerTape:                                                                                                               
    """
    TickerTape is a class that creates a scrolling ticker tape in a tkinter window.

    The ticker tape scrolls messages from right to left across the window. 
    The messages are loaded from a YAML file and are cycled continuously.

    Attributes:
        master (tkinter.Tk): The tkinter root widget.
        messages (cycle): A cycle iterator of the messages to be displayed.
        label (tkinter.Label): The label widget that displays the messages.

    Methods:
        run: Starts the ticker tape.
        update: Updates the label with the next message from the cycle.
        show_message: Displays the current message and recursively calls itself to scroll the message.
    """
    def __init__(self, master, messages):
        """
        Constructs all the necessary attributes for the TickerTape object.

        Args:
            master (tkinter.Tk): The tkinter root widget.
            messages (list): The messages to be displayed.
        """
        self.master = master
        self.messages = cycle(messages)                                                                                     # to cycle through the list of messages
        self.label = tk.Label(master, text='', font=("Helvetica", 16), bg='black', fg='white', anchor='w')
        self.label.pack(fill='x')

    def run(self):
        """
        Starts the ticker tape.
        """
        self.master.after(1000, self.update)                                                                                # Update every 1 second
    def get_text_width(text, font):
        temp = tk.Tk()
        temp.withdraw()  # make sure it's not shown
        width = tk.Font(font=font).measure(text)
        temp.destroy()
        return width

    def update(self):
        """
        Updates the label with the next message from the cycle.
        """
        message = next(self.messages)
        message = ' ' * 200 + message                                                                                       # pad the message with spaces to fit screen width
        self.show_message(message)

    def show_message(self, message):
        """
        Displays the current message and recursively calls itself to scroll the message.

        Args:
            message (str): The current state of the message as it scrolls.
        """
        self.label.config(text=message)
        if len(message) > 1:                                                                                                # This will create a scrolling effect
            next_message = message[1:]
            self.master.after(100, lambda: self.show_message(next_message))
        else:
            self.master.after(1000, self.update)                                                                            # Update after 1 second when there's no more message to scroll

if __name__ == "__main__":                                                                                                  # Main body
    messages = load_ticker_text('ticker_text.yaml')
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()                                                                                 # get the screen width
    root.geometry(f"{screen_width}x20+0+0")                                                                                 # set the window width to the screen width
    root.attributes('-topmost', True)                                                                                       # keep the window on top of other windows
    root.title("Willem Ticker Tape")                                                                                        # set the window title here
    root.overrideredirect(True)
    root.attributes('-alpha', 0.7)  # making the window transparent
    ticker = TickerTape(root, messages)
    ticker.run()
    root.mainloop()
