from pynput.keyboard import Listener, Key 
import time 
userText = "" 
quote = "The quick brown fox jumps over the lazy dog."
startTime = None
endTime = None
i = 0
        
def compare(key):
    global i
    global quote 
    global userText
    global startTime
    global endTime

    if startTime is None and i == 0:
        startTime = time.time()

    try: 
        char = key.char

        if i >= len(quote) - 1 :
            endTime = time.time()
            duration = endTime - startTime

            wordCount = len(quote) / 5
            wpm = (wordCount) / (duration / 60)

            userText += char
            print(f"\nYour input: {userText}")
            print("\nQuote completed!")
            print(f"Time taken: {duration:.2f} seconds")
            print(f"Your WPM: {wpm:.2f}")
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