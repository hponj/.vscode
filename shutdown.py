import os
import time

def shutdown_after(second):
    time.sleep(second)
    os.system("shutdown /s /t 1")

shutdown_after(1)