import pyautogui
import string
from code_base_folder import default_functions as df, time_date_select as tnd, network_menu, create_account
import pytesseract
from PIL import Image
import re

PREFIX = 'screens_init/'
pyautogui.PAUSE = 1


class FirstInitMenu:
    def __init__(self, user: string):
        self.user = user

    def open_emu_window(self):
        while not df.check_visible('ts_emu', path_prefix=PREFIX)[0]:
            df.safe_click('ts_emu_icon', path_prefix=PREFIX)

    def click_up(self):
        df.safe_click('menu_up', path_prefix=PREFIX, min_search_time=1, repeat=1)

    def click_down(self):
        df.safe_click('menu_down', path_prefix=PREFIX, min_search_time=1, repeat=1)

    def click_ok(self):
        df.safe_click('menu_ok', path_prefix=PREFIX, min_search_time=1, repeat=1)

    def scroll_to_menu_option_and_click(self, filename: string):
        while not df.check_visible(filename, path_prefix=PREFIX, min_search_time=1)[0]:
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

    def check_end_init(self):
        df.wait_visible('end_init_title', path_prefix=PREFIX)
        df.wait_visible('separate_kx', path_prefix=PREFIX)
        df.wait_visible('export_sertificate', path_prefix=PREFIX)

    def open_export_sertificate(self):
        df.wait_click('export_sertificate', path_prefix=PREFIX)
        df.wait_visible('device_to_export_title', path_prefix=PREFIX)

    def find_device_on_screen(self, device_name: string) -> bool:
        location = df.check_visible('device_to_export_name', path_prefix=PREFIX)[1]
        device_name = re.sub(r'[^a-zA-Z0-9]', '', device_name)
        screenshot = pyautogui.screenshot(region=(int(location.x - 85), int(location.y - 35), 200, 50),
                                          imageFilename='screens/log/device_name.png')
        device_name_found = pytesseract.image_to_string(screenshot, lang="rus+eng")
        device_name_found = re.sub(r'[^a-zA-Z0-9]', '', device_name_found)
        return device_name_found == device_name

    def select_device_to_export(self, device_name: string):
        df.safe_click('reload_btn', path_prefix=PREFIX)
        while not self.find_device_on_screen(device_name):
            df.safe_click('white_arrow_down', path_prefix=PREFIX)


class SelectAlg:
    def __init__(self):
        pass

    def select_gost(self):
        while not df.check_visible('alg_gost', path_prefix=PREFIX):
            df.safe_click('arrow_right', path_prefix=PREFIX)
            pass

    def select_stb(self):
        while not df.check_visible('alg_stb', path_prefix=PREFIX):
            df.safe_click('arrow_right', path_prefix=PREFIX)


def test_initialization():
    fin = FirstInitMenu(user='АсРЗИ')
    fin.open_emu_window()
    df.check_visible(filename='title', path_prefix=PREFIX)
    fin.open_first_init()
    df.click_arrow_right()

    df.wait_visible('select_alg_title', path_prefix=PREFIX)
    sel_alg = SelectAlg()
    sel_alg.select_gost()

    df.click_arrow_right()
    df.click_arrow_right()

    tnd.check_page()

    df.click_arrow_right()
    df.click_arrow_right()

    network_menu.check_page()
    network_menu.open_ip_address_input()
    network_menu.open_ip_input()
    network_menu.input_ip('198.168.203.128')
    df.click_arrow_right()
    network_menu.check_ip('198.168.203.128')
    df.click_arrow_right()
    df.click_arrow_right()
    df.click_arrow_right()

    create_account.check_page()
    create_account.open_pin_input()
    create_account.input_pin('11111111')
    df.click_arrow_right()
    create_account.open_pin_admin_input()
    create_account.input_pin('87654321')
    df.click_arrow_right()
    create_account.open_key_input()
    create_account.select_key('asrzi')
    df.click_arrow_right()
    df.click_arrow_right()
    df.click_arrow_right()

    create_account.open_pin_input()
    create_account.input_pin('11111111')
    df.click_arrow_right()
    create_account.open_pin_admin_input()
    create_account.input_pin('87654321')
    df.click_arrow_right()
    create_account.open_key_input()
    create_account.select_key('aib')
    df.click_arrow_right()
    df.click_arrow_right()


fin = FirstInitMenu(user='АсРЗИ')
fin.select_device_to_export('/media/user/KINGSTON')
# test_initialization()
