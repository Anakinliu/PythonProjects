#Helper functions
import numpy as np
import pyscreenshot
import pyautogui  # 因为pyscreenshot慢

import cv2
from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
# Gets one frame
def get_screen():
    # print('get_screen')
    # 470x410 (size of GD without the things
    # behind the cube being recorded and the top being cut off)
    # screen = np.array(pyscreenshot.grab(bbox=(150, 40, 620, 450)))  1436 672
    # screen = np.array(pyscreenshot.grab(bbox=(1441, 645, 1911, 1055)))
    # screen = np.array(pyscreenshot.grab(bbox=(1436, 672, 1906, 1082)))
    # screen = np.asarray(pyautogui.screenshot().crop(box=(1439, 676, 1909, 1086)))
    screen = np.asarray(pyautogui.screenshot().crop(box=(1441, 681, 1911, 1091)))
    # Simplify image
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    gray_screen = cv2.Canny(gray_screen, threshold1=200, threshold2=300)
    # print(screen)
    # print(screen.shape)  # (410, 470, 3)
    return gray_screen  # (410, 470)

# Compares two following images and returns a boolean for alive. If the image is the "Restart?"
# screen, structural similarity index will be 0.99+ which means the cube is dead. Else, it's alive.
def isalive(screen1, screen2):
    # (score, diff) = compare_ssim(screen1, screen2, full=True)
    score = structural_similarity(screen1, screen2)
    if score < 0.995:
        # print('is alive : True')
        return True
    else:
        return False

# Records and displays the screen
def screen_record():
    while(True):
        gray_printscreen = get_screen()
        cv2.imshow('window', gray_printscreen)
        #press q to exit screen recording
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
