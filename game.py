import win32gui
import win32con


def get_window_handle():
    hwnd = win32gui.FindWindow(None, "原神")
    if win32gui.IsIconic(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    else:
        win32gui.SetForegroundWindow(hwnd)