import time 
from pygame import mixer
import os
import sys
from colorama import Fore, Back, Style, init

# Initialize colorama for Windows color support
init(autoreset=True)

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(SCRIPT_DIR, 'sounds')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def speed():
    text = "The quick brown fox jumps over the lazy dog, is a sentence containing all the letters of the alphabet."
    typed_text = []
    wpm = 0
    start_time = time.time()
    
    mixer.init()
    
    while True:
        seconds_passed = max((time.time() - start_time), 1)
        cpm = int(len(typed_text) / (seconds_passed/60))
        wpm = round((cpm/5), 2)

        clear_screen()
        show_speed(text, typed_text, cpm, wpm, seconds_passed)

        if "".join(typed_text) == text:
            break
        
        try:
            keyPress = input()
            if len(keyPress) > 0:
                keyPress = keyPress[0]
            else:
                continue
        except KeyboardInterrupt:
            print("\n" + Fore.RED + "Typing test cancelled!")
            return False

        if keyPress == '\x1b':  # ESC key
            print(Fore.RED + "Test cancelled!")
            return False
        
        if keyPress == '\b' or keyPress == '\x7f':
            if len(typed_text) > 0:
                typed_text.pop()
        elif len(typed_text) < len(text):
            typed_text.append(keyPress)
            
            try:
                mixer.music.load(os.path.join(SOUND_DIR, 'typeSec.mp3'))
                mixer.music.play()
            except Exception as e:
                pass
        
        if len(typed_text) == len(text):
            break

    return True

def show_speed(text, typed_text, cpm, wpm, seconds_passed):
    """Display speed according to time passed and amount of text typed"""
    
    print(text)
    print()
    print(f"Typing Speed in characters per minute: {cpm}")
    print(f"Typing Speed in words per minute (wpm): {wpm}")
    print(f"Seconds elapsed: {round(seconds_passed, 2)} seconds")
    print()
    
    # Show what has been typed with color coding
    display_text = ""
    for index, letter in enumerate(typed_text):
        correct_char = text[index]
        if letter != correct_char:
            display_text += Fore.RED + letter + Style.RESET_ALL
        else:
            display_text += Fore.GREEN + letter + Style.RESET_ALL
    
    print("Your typing:")
    print(display_text)
    print()

def main():
    print(Fore.CYAN + "=== Typing Speed Test ===")
    print("Type the sentence as fast as you can!")
    print(Fore.YELLOW + "Press Ctrl+C to exit at any time.")
    print()
    
    while True:
        input("Press Enter to start the typing test...")
        
        if speed():
            # Test completed successfully
            mixer.init()
            try:
                mixer.music.load(os.path.join(SOUND_DIR, 'successMessage.mp3'))
                mixer.music.play()
                time.sleep(2)
            except Exception as e:
                pass
            
            clear_screen()
            print(Fore.GREEN + "🎉 Yay!! You completed the test!")
            
            try_again = input(Fore.CYAN + "Press Enter to try again or type 'quit' to exit: ").lower()
            if try_again == 'quit':
                print(Fore.YELLOW + "Thanks for using the Typing Speed Test!")
                break
        else:
            print(Fore.RED + "Test was cancelled.")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        sys.exit(1)