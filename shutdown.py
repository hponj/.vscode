import os
import time
import keyboard

def shutdown_after(second):
    keyboard.wait("s")
    time.sleep(second)
    os.system("shutdown /s /t 1")

shutdown_after(1)