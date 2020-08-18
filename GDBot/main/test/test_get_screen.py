import numpy as np
import pyscreenshot
import pyautogui
import cv2
import torch
import torchvision.transforms as T
from PIL import Image
from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Gets one frame
def get_screen():
    # print('get_screen')
    # 470x410 (size of GD without the things
    # behind the cube being recorded and the top being cut off)
    # screen = np.array(pyscreenshot.grab(bbox=(150, 40, 620, 450)))
    # pyscreenshot.grab(bbox=(1441, 645, 1911, 1055))
    screen = np.asarray(pyautogui.screenshot().crop(box=(1441, 615, 1911, 1025)))
    # print(type(image))
    # pyautogui.screenshot().crop(box=(1441, 620, 1911, 1030)).show("s")
    # image.show("s")
    # screen = np.asarray(pyscreenshot.grab(bbox=(1441, 645, 1911, 1055)))
    # Simplify image
    # 转换为灰度图
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    # 
    gray_screen = cv2.Canny(gray_screen, threshold1=200, threshold2=300)
    # print(gray_screen)
    print(gray_screen.shape)  # (410, 470)
    # cv2.imshow('returned gray', gray_screen)
    # cv2.waitKey()
    # return gray_screen


def convert_to_n(screen):
    screen = np.ascontiguousarray(screen, dtype=np.float32) / 255
    screen = torch.from_numpy(screen)
    # print(screen)
    # print(screen.shape)  # torch.Size([410, 470])
    # Resize, and add a batch dimension (BCHW)
    resize = T.Compose([T.ToPILImage(),
                        T.Resize(40, interpolation=Image.CUBIC),
                        T.ToTensor()])
    return resize(screen).unsqueeze(0).to(device)


# x = convert_to_n(get_screen())
# print(x)
# print(x.shape)


def isalive(screen1, screen2):
    # (score, diff) = compare_ssim(screen1, screen2, full=True)
    score = structural_similarity(screen1, screen2)
    if score < 0.995:
        # print('is alive : True')
        return True
    else:
        return False
    pass


i = 0
last_screen = get_screen()
current_screen = get_screen()
while True:
    last_screen = get_screen()
    # current_screen = get_screen()
    # print(isalive(last_screen, current_screen))
    i += 1
    print(i)
