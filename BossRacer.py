"""
BossRacer.py
By
Rahat Hossain

INTERVAL_OF_TYPING here is safe for small and medium type texts.
For large texts it still gets caught by the site.
"""

import pytesseract as tess
from PIL import Image
import time, os
import pyautogui as pg


try: input = raw_input
except NameError: pass

DELAY_TO_START = 1.5
INTERVAL_OF_TYPING = 0.1

def getImageName():
	return newest(os.getcwd())

def newest(path):
    files = os.listdir(path)
    newfiles = []
    for file in files:
    	if file[0:10] == "Screenshot":
    		newfiles.append(file)
    files = newfiles
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def firstPart():
	try:
		name = getImageName()
		print(name)
		with Image.open(name) as img:
			text = tess.image_to_string(img)
			text = refineText(text)
			secondPart(text)
	except:
		print("Halted")

def refineText(text):
	old = text
	old = old.split("\n")
	text = ""
	for line in old:
		text += line
		text += " "
 	if text[0] == '|' and text[1] == ' ':
 		text = text[1:]
 	text = text.replace("|", "I")
 	return text


def secondPart(text):
	print("PLACE OVER THE TEXTING AREA WITHIN {0} SECONDS".format(DELAY_TO_START))
	time.sleep(DELAY_TO_START)
	pg.click()
	pg.typewrite(text, interval = INTERVAL_OF_TYPING)

firstPart()
