import cv2
import numpy as np
import pyautogui

def current_level():
    now_level = 0
    best_score = float(0)
    screenshot = pyautogui.screenshot(region=(1200, 100, 60, 60))

    # Convert PIL image to numpy array and then to OpenCV format
    screenshot = np.array(screenshot)
    screen = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
    for level in range(0, 21):
        template = cv2.imread(f"./images/level{level}.png",)
        template_cropped = template[100:150, 1200:1260]

        result = cv2.matchTemplate(screen, template_cropped, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > best_score:
            best_score = max_val
            now_level = level
    return now_level