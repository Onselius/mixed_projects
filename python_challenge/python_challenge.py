#! /usr/bin/python3
# python_challenge.py 

import string, re, requests, pickle, zipfile, os, time

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb
          gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq
          pcamkkclbcb. lmu ynnjw ml rfc spj."""
translate = text.maketrans("koe", "mqg")

alphabet = list(string.ascii_lowercase)
alphabet.extend(string.ascii_lowercase)

new_text = ""
my_dict = {}
for i in range(26):
    my_dict[alphabet[i]] = i

for char in "map":
    if char in alphabet:
        i = my_dict[char]
        i += 2

        new_text += alphabet[i]
        continue
    new_text += char
print(new_text)

my_regex = re.compile(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')

match = re.match(my_regex, text)
#print(my_regex.match(text))

#for m in my_regex.findall(text):
#    print(m)

#print(match)
# for char in text:
#     if char in alphabet:
#         print(char, end=" ")

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=4413"

while True:
    try:
        page = requests.get(url)
    except Exception as e:
        print(e)
        break
    print(page.text)
    text = page.text.split()
    break # Uncomment to fix for loop
    for w in text:
        if w.isdigit():
            url = base_url + w
            print("new URL is: " + url)
            break

# file = open("banner.p", "rb")
# raw = pickle.load(file)
# file.close()
# for t in raw:
#     print("".join([k * v for k, v in t]))

# 90052
# files = zipfile.ZipFile("channel.zip", "r")
# files.extractall("zipfiles")

# ext = "90052"
# while True:
#     try:
#         file = open("zipfiles/" + ext + ".txt", "r")
#         text = file.readline()
#         print(text)
#         ext = text.split()[-1]
#     except Exception as e:
#         print(e)
#         break