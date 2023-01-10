import win32gui
import win32con
import win32api
import pyautogui
import argparse

def get_window_handle():
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(None, "原神")
    return hwnd


def enhance(n):
    i = 0
    while(i < n):
        pyautogui.click(1750, 760)
        pyautogui.click(1700, 1020)
        pyautogui.click(150, 155)
        pyautogui.click(170, 230)
        i += 1


def indow_handle(hwnd):
    if win32gui.IsIconic(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    else:
        win32gui.SetForegroundWindow(hwnd)


if __name__ == '__main__':
    hwnd = get_window_handle()
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=1)
    args = parser.parse_args()
    indow_handle(hwnd)
    enhance(args.n)