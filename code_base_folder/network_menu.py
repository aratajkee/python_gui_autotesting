import pyautogui as pag
import string
from code_base_folder import default_functions as df, time_date_select as tnd
import time
import pytesseract
from PIL import Image
import re

pag.PAUSE = 1
pag.FAILSAFE = True

PREFIX = 'screens_network/'
pag.PAUSE = 1


def check_page():
    df.check_visible('network_title', path_prefix=PREFIX)
    df.check_visible('name_block', path_prefix=PREFIX)
    df.check_visible('ip_address_block', path_prefix=PREFIX)
    df.check_visible('port_block', path_prefix=PREFIX)


def open_ip_address_input():
    df.safe_click('ip_address_block', path_prefix=PREFIX)


def open_ip_input():
    df.safe_click('ip_input_block', path_prefix=PREFIX)
    df.check_visible('ip_keyboard', path_prefix=PREFIX)


def click_enter():
    df.safe_click('num_enter', path_prefix=PREFIX)


def click_delete(repeat=1):
    df.safe_click('num_delete', repeat=repeat, path_prefix=PREFIX)


def clear_ip_cells():
    click_enter()
    click_enter()
    click_enter()
    click_delete(repeat=12)
    df.check_visible('ip_empty', path_prefix=PREFIX)


def click_num(num: string):
    num_name = 'num_' + num
    df.safe_click(num_name, path_prefix=PREFIX, confidence=0.95)


def input_ip(ip: string):
    clear_ip_cells()
    ip = ip.split('.')
    for quart in ip:
        for num in quart:
            click_num(num)
        click_enter()


def check_ip(ip_expected: string):
    is_visible, location = df.check_visible('ip_input_block', path_prefix=PREFIX, confidence=0.6)
    screenshot = pag.screenshot(region=(int(location.x - 100), int(location.y - 50), 200, 150),
                                imageFilename='screens/log/ip_input.png')
    ip_found = pytesseract.image_to_string(screenshot, lang='rus+eng')
    ip_found = re.sub(r'[^0-9.]', '', ip_found)
    assert ip_expected == ip_found.replace(" ", "").replace("\n",
                                                            ""), f"Expected ip: {ip_expected}\tbut found: {ip_found}"


input_ip('192.168.203.128')
df.click_arrow_right()
check_ip('192.168.203.128')


# TODO CHECK SCREESHOT IP TEXT

# print(pytesseract.image_to_string(Image.open('screens/screens_network/ip_address_text_block.png'),lang='rus+eng'))
# print(pytesseract.image_to_string(Image.open('screens/screens_network/img.png'),lang='rus+eng'))
# print(pytesseract.image_to_string(Image.open('screens/screens_network/img_1.png'),lang='rus+eng'))
# print(pytesseract.image_to_string(Image.open('screens/screens_network/img_2.png'),lang='rus+eng'))
# print(pytesseract.image_to_string(Image.open('screens/screens_network/img_3.png'),lang='rus+eng'))


# pag.moveTo(df.check_visible('ip_address_block', path_prefix=PREFIX)[1])
# pag.moveTo(df.check_visible('ip_input_block', path_prefix=PREFIX)[1])
