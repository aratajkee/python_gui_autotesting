import pyautogui
import pyautogui as pag
import time
import pytesseract
import string
import platform
from code_base_folder import default_functions as df


def check_page():
    df.check_visible('time_and_date_page_title')
    df.check_visible('date_block')
    df.check_visible('time_block')
    df.check_visible('time_zone_block')
