import ctypes
import webbrowser

# Functions
def window_title(title):
	ctypes.windll.kernel32.SetConsoleTitleW(title)
def url_open(title):
	webbrowser.open(title)
def msgbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# Information about Module #
__version__ = '1.1'
__description__ = 'Jpower - module for python.\nIt adds some commands with and notification.'
