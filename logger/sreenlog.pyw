import pyautogui, time, os

try:
    os.mkdir('imglog/')
except:
    pass

i = 0
while True:
    i += 1
    pyautogui.screenshot(f"imglog/log{i}.jpg")
    time.sleep(2)