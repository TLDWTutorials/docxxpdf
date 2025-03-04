

from docx2pdf import convert
from os import listdir
from os.path import isfile, join
import ctypes
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
ctypes.windll.user32.MessageBoxW(0, "Hit OK to select the file folder with the MS Word DOCX files you wish to convert to PDFs.", "Complete", 0)
word_path = filedialog.askdirectory()
ctypes.windll.user32.MessageBoxW(0, "Hit OK to select the file folder where you want to save your PDFs.", "Complete", 0)
pdf_path = filedialog.askdirectory()
convert(word_path, pdf_path)

