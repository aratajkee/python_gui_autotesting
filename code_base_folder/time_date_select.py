import pyautogui
import pyautogui as pag
import time
import pytesseract
import string
import platform
from code_base_folder import default_functions as df

PREFIX = 'screens_date/'


def check_page():
    df.wait_visible('time_and_date_page_title', path_prefix=PREFIX)
    df.wait_visible('date_block', path_prefix=PREFIX)
    df.wait_visible('time_block', path_prefix=PREFIX)
    df.wait_visible('time_zone_block', path_prefix=PREFIX)
