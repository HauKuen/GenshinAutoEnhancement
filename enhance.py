import pyautogui
import compare_level
import time
import configparser

config = configparser.ConfigParser()
config.read('./config.ini')


def enhance(aim_level):
    now_level = compare_level.current_level()  
    enhance = config['enhance']['x'], config['enhance']['y']
    quick = config['quick']['x'], config['quick']['y']
    realenhance = config['realenhance']['x'], config['realenhance']['y']
    details = config['details']['x'], config['details']['y']
    while now_level < aim_level:
        pyautogui.click(quick)
        pyautogui.click(realenhance)
        pyautogui.click(details)
        pyautogui.click(enhance)
        time.sleep(0.2)
        now_level = compare_level.current_level()
