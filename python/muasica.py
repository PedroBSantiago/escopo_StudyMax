import pyautogui
import time

pyautogui.press("win")
pyautogui.write("Google")
pyautogui.hotkey("enter")
time.sleep(0.3)
pyautogui.write("http://127.0.0.1:5500/login.html")
pyautogui.hotkey("enter")
pyautogui.moveTo(x=24, y=470)
pyautogui.click(x=24, y=470)
time.sleep(1)
pyautogui.moveTo(x=1577, y=155)
pyautogui.click(x=1577, y=155)
time.sleep(1)
