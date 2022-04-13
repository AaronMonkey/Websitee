from pynput.keyboard import Key, Controller
import pyautogui
import time
mkeyboard = Controller ()
time.sleep(5)
mkeyboard.type("ipconfig")
pyautogui.press('enter')