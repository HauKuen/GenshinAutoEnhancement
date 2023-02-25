import compare_level
import enhance
from game import get_window_handle


def main():
    get_window_handle()
    now_level = compare_level.current_level()
    
    for aim_level in range(4, 21, 4):
        if now_level < aim_level:
            enhance.enhance(aim_level)
            break

if __name__ == '__main__':
    main()
