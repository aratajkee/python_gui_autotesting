import pyautogui
import pyautogui as pag
import time
import pytesseract
import string
import platform
from code_base_folder import default_functions as df
from code_base_folder.time_and_date import time_date_select as tnd

PATH = '/home/user/py/automate_gui/python_gui_autotesting/code_base_folder/first_init_menu/'

pyautogui.PAUSE = 1


class FirstInitMenu:
    def __init__(self, user: string):
        self.user = user

    def open_emu_window(self):
        while not df.check_visible('ts_emu')[0]:
            df.safe_click('ts_emu_icon')

    def click_up(self):
        df.safe_click('menu_up', min_search_time=1, repeat=1)

    def click_down(self):
        df.safe_click('menu_down', min_search_time=1, repeat=1)

    def click_ok(self):
        df.safe_click('menu_ok', min_search_time=1, repeat=1)

    def scroll_to_menu_option_and_click(self, filename: string):
        while not df.check_visible(filename, min_search_time=1)[0]:
            self.click_down()
        else:
            self.click_ok()

    def open_first_init(self):
        self.scroll_to_menu_option_and_click('first_init_selected')

    def open_restore_kx(self):
        self.scroll_to_menu_option_and_click('vosst_kx_selected')

    def open_restore_from_reserved_copy(self):
        self.scroll_to_menu_option_and_click('vosst_reserv_selected')

    def open_return_to_factory_new(self):
        self.scroll_to_menu_option_and_click('return_to_factory_new_selected')

    def open_info(self):
        self.scroll_to_menu_option_and_click('info_selected')

    def open_turn_off(self):
        self.scroll_to_menu_option_and_click('off_selected')

    def open_reboot(self):
        self.scroll_to_menu_option_and_click('reeboot_selected')


class SelectAlg:
    def __init__(self):
        pass

    def select_gost(self):
        while not df.check_visible('alg_gost'):
            df.safe_click('arrow_right')
            pass

    def select_stb(self):
        while not df.check_visible('alg_stb'):
            df.safe_click('arrow_right')


def test_initialization():
    fin = FirstInitMenu(user='АсРЗИ')
    fin.open_emu_window()
    df.check_visible(filename='title')
    fin.open_first_init()
    df.click_arrow_right()

    df.check_visible('select_alg_title')
    sel_alg = SelectAlg()
    sel_alg.select_gost()

    df.click_arrow_right()
    df.click_arrow_right()

    tnd.check_page()

    df.click_arrow_right()
    df.click_arrow_right()



test_initialization()
