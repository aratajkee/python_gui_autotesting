import pyautogui
import pyautogui as pag
import time
import pytesseract
import string

pyautogui.PAUSE = 1


class FirstInitMenu:
    def __init__(self, user: string):
        self.user = user

    def check_visible(self, filename: string, confidence: float = 0.8, min_search_time: int = 2) -> tuple[bool, object]:
        try:
            full_filename = 'screens/' + filename + '.png'
            target = pag.locateCenterOnScreen(full_filename, minSearchTime=min_search_time, confidence=confidence)
            print(f"Found {filename} at location: {target}")
            return True, target
        except pag.ImageNotFoundException as ex:
            print(f"Error finding image {filename}\nException: {ex}")
            return False, object

    def safe_click(self, filename: string, confidence: float = 0.8, min_search_time: int = 2, repeat: int = 1):
        found, target = self.check_visible(filename, confidence, min_search_time)
        if found:
            for i in range(1, repeat):
                pag.click(target)

    def open_emu_window(self):
        while not self.check_visible('ts_emu'):
            self.safe_click('ts_emu_icon')

    def click_up(self):
        self.safe_click('menu_up', min_search_time=1, repeat=1)

    def click_down(self):
        self.safe_click('menu_down', min_search_time=1, repeat=1)

    def click_ok(self):
        self.safe_click('menu_ok', min_search_time=1, repeat=1)

    def open_info(self):
        while not self.check_visible('info_selected', min_search_time=1)[0]:
            self.click_down()
        else:
            self.click_ok()


fin = FirstInitMenu(user='АсРЗИ')
fin.open_emu_window()
fin.check_visible(filename='title')
fin.open_info()
