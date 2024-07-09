import pyautogui as pag
import time
import pytesseract
import platform
import string


def check_visible(filename: string, confidence: float = 0.8, min_search_time: int = 2) -> \
        tuple[bool, object]:
    try:
        full_filename = 'screens/' + filename + '.png'
        print(f"\n\nFILE PATH {full_filename}\n\n")
        if platform.system() == 'Linux':
            full_filename = full_filename
        target = pag.locateCenterOnScreen(full_filename, minSearchTime=min_search_time, confidence=confidence)
        print(f"Found {filename} at location: {target}")
        return True, target
    except pag.ImageNotFoundException as ex:
        print(f"Error finding image {filename}\nException: {ex}")
        return False, object


def safe_click(filename: string, confidence: float = 0.8, min_search_time: int = 2,
               repeat: int = 1):
    found, target = check_visible(filename=filename, confidence=confidence,
                                  min_search_time=min_search_time)
    if found:
        for i in range(0, repeat):
            print(f"Click on: {target}")
            pag.click(target)


# Повторяющиеся на разных страницах кнопки
def click_arrow_left():
    safe_click('arrow_left')


def click_arrow_right():
    safe_click('arrow_right')
