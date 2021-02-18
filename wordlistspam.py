from time import sleep

import pyautogui

f = open("wortliste.txt", 'r')
sleep(4)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
