import subprocess
import time
import pyautogui as pag


def run_hsm():
    command = 'cd /usr/local/bin/dotnet/Administrator && sudo dotnet ./Infotecs.TtpHsm.Administrator.Local.dll; exec bash'
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', command])
    time.sleep(2)
    pag.write('123', interval=0.25)
    pag.press('enter')
    pag.hotkey('win', 'd')

