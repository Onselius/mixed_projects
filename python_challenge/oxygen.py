#! /usr/bin/python3
# oxygen.py - Try to find hidden message in image file

import requests
from PIL import Image

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

print(img.height)
middle = int(img.height / 2)
print(middle)
list_of_pixels = []
for x in range(img.width):
    pixel = img.getpixel((x, middle))
    if pixel[0] != pixel[1] and pixel[0] != pixel[2]:
        continue
    if len(list_of_pixels) == 0:
        list_of_pixels.append(pixel[0])
    elif list_of_pixels[-1] != pixel[0]:
        list_of_pixels.append(pixel[0])

print(len(list_of_pixels))
print(list_of_pixels)
answer = ""
for letter in list_of_pixels:
    answer += str(chr(letter))
print()
print(answer)
for letter in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
    print(str(chr(letter)), end="")