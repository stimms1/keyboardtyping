from pynput.keyboard import Listener, Key 
userText = "" 
def on_press(key):
    global userText 
    try: 
        char = key.char
        userText += char
    except AttributeError:
        if key == Key.space:
            userText += " " 
        elif key == Key.enter:
            userText += "\n"
        elif key == Key.esc:
            print("Text is done!") # this is temporary lols
            print(userText)
            return False
        else: 
            pass
        



print("Listening now: ")
listener = Listener(on_press = on_press)

listener.start()

listener.join()