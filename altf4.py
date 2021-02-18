import pyautogui
from time import sleep

i = 10
sleep(3)
while i != 0:
    pyautogui.typewrite(str(i))
    pyautogui.press('enter')
    i = i - 1
pyautogui.press('backspace')