#Simulates keypresses on Mac
from pynput.mouse import Button, Controller
import pyautogui
mouse = Controller()

#Bounce the cube by clicking on the screen
def bounce():
    # print('jump')
    # pyautogui.moveTo(1693, 393)
    pyautogui.click(1696, 963)
    #
    # mouse.position = (1696, 963)
    # mouse.click(Button.left, 1)

#Restart the level by clicking on the restart button
def restart():
    # print('restart')
    # mouse.position = (1580, 970)
    # mouse.click(Button.left, 1)
    #
    pyautogui.click(1580, 970)

