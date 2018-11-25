#! /usr/bin/python3
# oxygen.py - Try to find hidden message in image file

import requests
from Pillow import Image

while True:
    try:
        img = open("oxygen.png", "r")
        img = Image.open
        print("file opened")
        break
    except Exception as e:
        print(e)
        file_to_save = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png")
        file_to_save.raise_for_status()
        open("oxygen.png", "wb").write(file_to_save.content)
        
width, height = img.size()
print(width)
print(height)