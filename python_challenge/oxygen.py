#! /usr/bin/python3
# oxygen.py - Try to find hidden message in image file

import requests, os
from PIL import Image

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "oxygen.png")
print(path)
img = Image.open(path)

while True:
    try:
        img = Image.open("oxygen.png")
        print("file opened")
        break
    except Exception as e:
        print(e)
        file_to_save = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png")
        file_to_save.raise_for_status()
        open("oxygen.png", "wb").write(file_to_save.content)
    
width = img.width
for value in img.size:
    print(value)