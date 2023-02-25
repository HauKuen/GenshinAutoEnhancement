import cv2
import configparser
from PIL import ImageGrab
from game import get_window_handle
import numpy as np

config = configparser.ConfigParser()
config.read('config.ini')

# 定义点击事件的回调函数
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        config['details'] = {'x': str(x), 'y': str(y)}
        with open('config.ini', 'w') as f:
            config.write(f)
        cv2.destroyAllWindows()

def main():
    get_window_handle()
    screenshot = ImageGrab.grab()
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    cv2.namedWindow('image')
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()