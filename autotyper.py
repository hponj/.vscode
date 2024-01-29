import pyautogui
import keyboard
import time

def auto_typing():
    while not keyboard.is_pressed("k"):
        pyautogui.write('lol')
        pyautogui.press('enter')

if __name__=="__main__":
    keyboard.wait('s')
    auto_typing()