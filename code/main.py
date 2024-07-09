import pyautogui as pag
import time
import string

pag.PAUSE = 1
pag.FAILSAFE = True


def is_found(filename: string) -> tuple[bool, object]:
    filename = 'screens/' + filename + '.png'
    try:
        res = pag.locateCenterOnScreen(filename, minSearchTime=5, confidence=0.7)
        print(f"Found {filename}")
        return True, res
    except pag.ImageNotFoundException as ex:
        print(f"Not found: {filename}\nError: {ex}")
        return False, object


def safe_click(filename: string):
    is_found_bool, location = is_found(filename)
    if is_found_bool: pag.click(location)


safe_click('menu')
safe_click('arrow')
safe_click('arrow')
safe_click('arrow')
safe_click('arrow')
safe_click('arrow')
safe_click('ip_address')
safe_click('ip_box')
safe_click('delete_btn')

safe_click('num_1')
safe_click('num_9')
safe_click('num_2')
safe_click('go_right')
safe_click('go_right')
safe_click('delete_btn')

safe_click('num_1')
safe_click('num_6')
safe_click('num_8')
safe_click('go_right')
safe_click('go_right')
safe_click('delete_btn')

safe_click('num_2')
safe_click('num_0')
safe_click('num_3')
safe_click('go_right')
safe_click('go_right')
safe_click('delete_btn')

safe_click('num_1')
safe_click('num_2')
safe_click('num_8')
safe_click('go_right')
safe_click('go_right')
safe_click('delete_btn')

safe_click('go_right')
pag.position()
