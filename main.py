import pyautogui
from PIL import Image, ImageGrab
import os, time


def runcommand():
    li = ["a", "r", "p", "i", "t"]
    for i in li:
        pyautogui.keyDown(i)


def takescreenshot():
    image = ImageGrab.grab()
    image.show()

if __name__ == "__main__":
    # takescreenshot()
    os.startfile("cmd")
    time.sleep(1)
    pyautogui.press(["c", "o", "m", "m", "a", "n", "d", "enter"])
    # runcommand()
    # pyautogui.press('enter')
    pyautogui.hotkey('alt', 'f4')