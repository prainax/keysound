from Xlib.display import Display
import threading
from random import choice
import subprocess
import os
import time
import sys


ZERO,SHIFT,ALT,CTL=[],[],[],[]
for i in range(0,32):
        ZERO.append(0)
        if i==6:
                SHIFT.append(4)
        else:
                SHIFT.append(0)
        if i==4:
                CTL.append(32)
        else:
                CTL.append(0)
        if i==8:
                ALT.append(1)
        else:
                ALT.append(0)

ignorelist=[ZERO,ALT,SHIFT,CTL]


class KeyPress(threading.Thread):
    def __init__(self, file):
        super().__init__()
        self.file = file

    def run(self):
        sound = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].isspace() else self.file
        try:
            subprocess.run(["aplay", sound], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error playing sound: {e}")

def main():
    # Select a random sound file from the 'sounds' directory
    sound_files = [f for f in os.listdir("sounds") if os.path.isfile(os.path.join("sounds", f))]
    file = choice(sound_files)
    # Initialize Xlib display
    disp = Display()

    print("press any key")
    while True:
        keymap = disp.query_keymap()
        if keymap not in ignorelist:
            KeyPress(f"sounds/{file}").start()
            time.sleep(0.08)

if __name__ == '__main__':
    main()
