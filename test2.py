import random
from random import randint
import string
from time import sleep
import pyautogui


def random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for c in range(length))
    return result_str


def random_string_length(lowest, highest):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for c in range(randint(lowest, highest)))
    return result_str


pyautogui.alert(text='Start the Spammer using the "OK" button', title='Spammer')
print("starting")
sleep(5)
i = 1
while i <= 100:
    pyautogui.typewrite(random_string_length(1, 20))
    pyautogui.hotkey('alt', 'f4')
    i += 1gi
