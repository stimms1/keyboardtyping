from pynput.keyboard import Listener, Key 
import time 
userText = "" 
quote = "The quick brown fox jumps over the lazy dog."
i = 0
        
def compare(key):
    global i
    global quote 
    global userText

    try: 
        char = key.char

        if i >= len(quote) - 1 :
            userText += char
            print(f"\nYour input: {userText}")
            print("Quote completed!") # add the time here once time is done.
            return False
        
        if char == quote[i]:
            userText += char
            i+=1 

            # this is to print the current sentence typed
            print(f"\rCurrent: {userText}_", end="", flush=True)
        else:
            print(f"\n*** INCORRECT CHARACTER! Expected: '{quote[i]}', Got: '{char}' ***")
            print(f"Current: {userText} <--- ERROR HERE")
            print(f"\rCurrent: {userText}_", end="", flush=True)

    except AttributeError: 
        if key == Key.space:
            if i < len(quote) and quote[i] == " ":
                userText += " "
                i += 1

                print(f"\rCurrent: {userText}_", end="", flush=True)
            else: 
                print(f"Incorrect Character!")
        else: 
            pass




print(f"Try this quote out!")
print(f"Target: {quote}")

listener = Listener(on_press = compare)

listener.start()
listener.join()