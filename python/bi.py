
import pyautogui
import time

pyautogui.press("win")
pyautogui.write("Google")
pyautogui.hotkey("enter")
time.sleep(0.3)
pyautogui.write("http://127.0.0.1:5500/login.html")
pyautogui.hotkey("enter")
pyautogui.click(x=948, y=263)
pyautogui.write("Jota Gameplay Ronaldo")
time.sleep(1)
pyautogui.click(x=947, y=290)
pyautogui.moveTo(x=947, y=290)
pyautogui.write("BANANANANA")
time.sleep(1)
pyautogui.moveTo(x=787, y=305)
pyautogui.click(x=787, y=305)
time.sleep(1)
pyautogui.moveTo(x=789, y=330)
pyautogui.click(x=789, y=330)
time.sleep(1)