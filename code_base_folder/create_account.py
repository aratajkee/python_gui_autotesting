import pyautogui as pag
import string
from code_base_folder import default_functions as df, time_date_select as tnd
import time
import pytesseract
from PIL import Image
import re

pag.PAUSE = 1
pag.FAILSAFE = True
PREFIX = 'screens_account/'


def check_page():
    df.wait_visible('title', path_prefix=PREFIX)
    df.wait_visible('mark', path_prefix=PREFIX)
    df.wait_visible('pin', path_prefix=PREFIX)
    df.wait_visible('pin_admin', path_prefix=PREFIX)
    df.wait_visible('key', path_prefix=PREFIX)


def open_pin_input():
    df.safe_click('pin', path_prefix=PREFIX)
    df.check_visible('pin_input_title', path_prefix=PREFIX)


def open_pin_admin_input():
    df.safe_click('pin_admin', path_prefix=PREFIX)
    df.check_visible('pin_input_title', path_prefix=PREFIX)


def open_key_input():
    df.safe_click('key', path_prefix=PREFIX)
    df.check_visible('key_input_title', path_prefix=PREFIX)


def keyboard_switch_mode(mode: string):
    if mode == 'eng':
        if df.check_visible('keyboard_switch_eng', path_prefix=PREFIX):
            df.safe_click('keyboard_switch_eng', path_prefix=PREFIX)
    if mode == 'ru':
        pass
    if mode == 'num':
        if df.check_visible('keyboard_switch_num', path_prefix=PREFIX):
            df.safe_click('keyboard_switch_num', path_prefix=PREFIX)


def click_num(num: string):
    num_name = 'num_' + num
    df.safe_click(num_name, path_prefix=PREFIX, confidence=0.95)


def input_pin(pin: string):
    for num in pin:
        click_num(num)


# TODO Ввод метки
def select_key(key_name: string):
    #     match key_name:
    #         case 'aib':
    #             while not df.check_visible('aib_key', path_prefix=PREFIX)[0]:
    #                 df.safe_click('white_arrow_right', path_prefix=PREFIX)
    #         case 'asrzi':
    #             while not df.check_visible('asrzi_key', path_prefix=PREFIX)[0]:
    #                 df.safe_click('white_arrow_right', path_prefix=PREFIX)
    #         case _:
    #             print(f"Error! Wrong key name :{key_name}")
    # #         TODO other keys

    if (key_name == 'aib'):
        while not df.check_visible('aib_key', path_prefix=PREFIX)[0]:
            df.safe_click('white_arrow_right', path_prefix=PREFIX)
    elif (key_name == 'asrzi'):
        while not df.check_visible('asrzi_key', path_prefix=PREFIX)[0]:
            df.safe_click('white_arrow_right', path_prefix=PREFIX)
    else:
        print(f"Error! Wrong key name :{key_name}")
