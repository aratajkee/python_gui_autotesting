import pyautogui as pag
import time
import string
import pytesseract
from PIL import Image
import default_functions as df


pag.PAUSE = 1
pag.FAILSAFE = True

filename = 'screens/' + 'time' + '.png'
print(pytesseract.image_to_string(Image.open(filename), lang='rus+eng'))

df.check_visible(filename='time')
