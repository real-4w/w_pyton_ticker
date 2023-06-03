import yaml, tkinter as tk
from itertools import cycle

def load_ticker_text(file_path):                                        
    with open(file_path, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
    return data['messages']

# Ticker Tape Class
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
        self.messages = cycle(messages) # to cycle through the list of messages
        self.label = tk.Label(master, text='', font=("Helvetica", 16), bg='black', fg='white', anchor='w')
        self.label.pack(fill='x')

    # Run the ticker
    def run(self):
        """
        Starts the ticker tape.
        """
        self.master.after(1000, self.update) # Update every 1 second

    # Update the label with the next message
    def update(self):
        """
        Updates the label with the next message from the cycle.
        """
        message = next(self.messages)
        message = message + ' ' * 200  # pad the message with spaces to fit screen width 
        self.show_message(message, message)


    def show_message(self, full_message, current_message):
        """
        Displays the current message and recursively calls itself to scroll the message.

        Args:
            full_message (str): The complete message that is being displayed.
            current_message (str): The current state of the message as it scrolls.
        """
        self.label.config(text=current_message)
        if len(full_message) > 0:
            # This will create a rotating effect
            next_message = full_message[1:] + full_message[0]
            self.master.after(100, lambda: self.show_message(next_message, next_message))
        else:
            self.master.after(1000, self.update)  # Update after 1 second when there's no more message to scroll


# Main
if __name__ == "__main__":
    messages = load_ticker_text('ticker_text.yaml')
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()  # get the screen width
    root.geometry(f"{screen_width}x60")  # set the window width to the screen width
    root.title("My Ticker Tape")  # set the window title here
    ticker = TickerTape(root, messages)
    ticker.run()
    root.mainloop()
