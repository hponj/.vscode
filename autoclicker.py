import pyautogui
import keyboard
import time

def auto_clicker():
    while not keyboard.is_pressed('k'):
        pyautogui.click()
        time.sleep(0.0001)

if __name__=="__main__":
    keyboard.wait('s')
    auto_clicker()
