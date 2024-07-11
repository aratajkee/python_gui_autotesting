import string
import time

import pyautogui
import subprocess
from code_base_folder import default_functions


PREFIX = "autoinstall/"


def auto_install(sudo_pass: string, login: string, password: string):
    install_script = "install_script.sh"
    try:
        subprocess.run(['gnome-terminal', '--', 'bash', '-c', install_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running the script: {e}")
    time.sleep(2)
    pyautogui.write(sudo_pass, interval=0.25)
    pyautogui.press('enter')
    default_functions.wait_visible('ask_login', path_prefix=PREFIX)
    pyautogui.write(login)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(password)
    pyautogui.press('enter')

    simulation_script = "simulation.sh"
    try:
        subprocess.run(['gnome-terminal', '--', 'bash', '-c', simulation_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running the script: {e}")
    time.sleep(2)
    pyautogui.write(sudo_pass, interval=0.25)
    pyautogui.press('enter')

