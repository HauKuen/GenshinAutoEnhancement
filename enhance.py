import pyautogui
import compare_level
import time

def enhance(aim_level):
    now_level = compare_level.current_level()
    while now_level < aim_level:
        pyautogui.click(1750, 760)
        pyautogui.click(1700, 1020)
        pyautogui.click(150, 155)
        pyautogui.click(170, 230)
        time.sleep(0.1)
        now_level = compare_level.current_level()
