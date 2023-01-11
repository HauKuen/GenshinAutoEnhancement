import win32gui
import win32con
import enhance


def get_window_handle():
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(None, "原神")
    return hwnd


def indow_handle(hwnd):
    if win32gui.IsIconic(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    else:
        win32gui.SetForegroundWindow(hwnd)


if __name__ == '__main__':
    hwnd = get_window_handle()
    indow_handle(hwnd)
    enhance.enhance(20)
    