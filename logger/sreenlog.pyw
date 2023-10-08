import pyautogui, time

i = 0
while True:
    i += 1
    pyautogui.screenshot(f"imglog/log{i}.jpg")
    time.sleep(2)