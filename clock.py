import tkinter as tk
from datetime import datetime
import json

with open('config.json', 'r') as f:
    jsonFile = json.load(f)

    # Screen resolution
    SCREEN_WIDTH = jsonFile['SCREEN_WIDTH']
    SCREEN_HEIGHT = jsonFile['SCREEN_HEIGHT']
    SCREEN_OFFSET_X = jsonFile['SCREEN_OFFSET_X']
    SCREEN_OFFSET_Y = jsonFile['SCREEN_OFFSET_Y']

    # Windowed resolution
    W_SCREEN_WIDTH = jsonFile['W_SCREEN_WIDTH']
    W_SCREEN_HEIGHT = jsonFile['W_SCREEN_HEIGHT']
    W_SCREEN_OFFSET_X = jsonFile['W_SCREEN_OFFSET_X']
    W_SCREEN_OFFSET_Y = jsonFile['W_SCREEN_OFFSET_Y']

    FONT_SIZE = jsonFile['FONT_SIZE']
    W_FONT_SIZE = jsonFile['W_FONT_SIZE']

    FONT_NAME = jsonFile['FONT_NAME']

    ALPHA = jsonFile['ALPHA']
    W_ALPHA = jsonFile['W_ALPHA']


# Create the main window
root = tk.Tk()
root.configure(bg='black')
root.title('Digital Clock')
root.resizable(False, False)
root.geometry("{0}x{1}+{2}+{3}".format(W_SCREEN_WIDTH, W_SCREEN_HEIGHT, W_SCREEN_OFFSET_X, W_SCREEN_OFFSET_Y))


root.attributes('-topmost', True)

# Create the label for the time display
time_label = tk.Label(root, text='', font=(FONT_NAME, W_FONT_SIZE), fg='white', bg='black', pady=50)
time_label.pack(expand=True)

# Define a function to update the time label
def update_time():
    current_time = datetime.now().strftime('%H:%M')
    time_label.config(text="🕒 {0}".format(current_time))
    root.after(1000, update_time)

# Create the button for fullscreen mode
fullscreen_mode = False
def toggle_fullscreen():
    global fullscreen_mode
    if not fullscreen_mode:
        root.overrideredirect(True)
        root.geometry("{0}x{1}+{2}+{3}".format(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_OFFSET_X, SCREEN_OFFSET_Y))
        fullscreen_button.place_forget()
        time_label.config(font=(FONT_NAME, FONT_SIZE))
        root.attributes('-alpha', ALPHA)
    else:
        root.geometry("{0}x{1}+{2}+{3}".format(W_SCREEN_WIDTH, W_SCREEN_HEIGHT, W_SCREEN_OFFSET_X, W_SCREEN_OFFSET_Y))
        root.overrideredirect(False)
        root.attributes('-alpha', W_ALPHA)
        fullscreen_button.config(text='Fullscreen')
        fullscreen_button.pack(pady=10)
        fullscreen_button.place(relx=1.0, rely=0.0, x=-10, y=10, anchor='ne')
        time_label.config(font=(FONT_NAME, W_FONT_SIZE))

    fullscreen_mode = not fullscreen_mode

fullscreen_button = tk.Button(root, text='Fullscreen', font=(FONT_NAME, 20), fg='white', bg='grey', command=toggle_fullscreen)
fullscreen_button.pack(pady=10)
fullscreen_button.place(relx=1.0, rely=0.0, x=-10, y=10, anchor='ne')
fullscreen_button.configure(cursor='hand2')

# Bind the escape key to exit fullscreen mode
def exit_fullscreen(event):
    global fullscreen_mode
    if fullscreen_mode:
        toggle_fullscreen()
    else:
        exit()

root.bind('<Escape>', exit_fullscreen)

# Call the update_time function to start the clock
update_time()
# Transparency window
root.attributes('-alpha', W_ALPHA)
# Start the main event loop
root.mainloop()
