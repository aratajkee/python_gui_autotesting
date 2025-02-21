import pyautogui as pag
import time
import pytesseract
import platform
import string


def check_visible(filename: string, path_prefix=None, confidence=0.8, min_search_time=2) -> \
        tuple[bool, object]:
    try:
        if path_prefix is not None:
            full_filename = 'screens/' + path_prefix + filename + '.png'
        else:
            full_filename = 'screens/' + filename + '.png'

        print(f"\n\nFILE PATH {full_filename}\n\n")

        if platform.system() == 'Linux':
            full_filename = full_filename
        target = pag.locateCenterOnScreen(full_filename, minSearchTime=min_search_time, confidence=confidence)
        print(f"Found {filename} at location: {target}")
        return True, target
    except pag.ImageNotFoundException as ex:
        print(f"Error finding image {filename}\nException: {ex}")
        return False, (0, 0, 0, 0)


def safe_click(filename: string, path_prefix=None, confidence=0.8, min_search_time=2,
               repeat: int = 1):
    found, target = check_visible(filename=filename, path_prefix=path_prefix, confidence=confidence,
                                  min_search_time=min_search_time)
    if found:
        for i in range(0, repeat):
            print(f"Click on: {target}")
            pag.click(target)


# Ожидание видимости в бесконечном цыкле
def wait_visible(filename: string, path_prefix=None, confidence=0.8) -> bool:
    while not check_visible(filename, path_prefix, confidence, min_search_time=1)[0]:
        pass
    return True


def wait_click(filename: string, path_prefix=None, confidence=0.8):
    if wait_visible(filename, path_prefix, confidence):
        safe_click(filename, path_prefix, confidence)


# Повторяющиеся на разных страницах кнопки
def click_arrow_left():
    wait_click('arrow_left')


def click_arrow_right():
    wait_click('arrow_right', confidence=0.9)
