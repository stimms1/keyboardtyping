from pynput.keyboard import Listener, Key 
import time 
userText = "" 
quote = "The quick brown fox jumps over the lazy dog."
i = 0
        
def compare(key):
    global i
    global quote 
    try: 
        char = key.char

        if i >= len(quote) - 1 :
            print("Quote completed!") # add the time here once time is done.
            return False
        
        if char == quote[i]:
            i+=1 
        else:
            print(f"Incorrect Character!")

    except AttributeError: 
        if key == Key.space:
            if i < len(quote) and quote[i] == " ":
                i += 1
            else: 
                print(f"Incorrect Character!")
        else: 
            pass




print(f"Try this quote out! {quote}")
listener = Listener(on_press = compare)

listener.start()

listener.join()