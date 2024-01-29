import os
import time

def shutdown_after(seconds):
    time.sleep(seconds)
    os.system("lol")

# Shutdown after 30 seconds
shutdown_after(1)
