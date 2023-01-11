import win32gui
import win32con
import compare_level
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
    now_level = compare_level.current_level()
    
    for aim_level in range(4, 21, 4):
        if now_level < aim_level:
            enhance.enhance(aim_level)
            break
