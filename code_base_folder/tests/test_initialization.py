from ..first_init_menu import first_init_menu as fin
from .. import default_functions as df

init_menu = fin.FirstInitMenu(user='АсРЗИ')
df.check_visible(filename='title')
init_menu.open_emu_window()
init_menu.open_info()