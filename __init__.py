import ctypes
import webbrowser
import colorama
from colorama import Fore, Back, Style
colorama.init()

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Functions
def window_title(title):
	ctypes.windll.kernel32.SetConsoleTitleW(title)
def url_open(title):
	webbrowser.open(title)
def msgbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# Information about Module #
__version__ = '1.1'
__author__ = 'Jesewe'
__description__ = 'Jpower - module for python.\nIt adds some commands with errors, and notification.\n© 2022 JeseweHack.'
