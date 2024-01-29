import os
import time

def shutdown_after(seconds):
    time.sleep(seconds)
    os.system("shutdown /s /t 1")

# Shutdown after 30 seconds
shutdown_after(1)
