#! /usr/bin/python3
# python_challenge.py 

import string, zipfile, os

list_of_comments = []
ext = "90052"

with zipfile.ZipFile("channel.zip") as my_zip:
    while True:
        try:
            content = my_zip.read(ext + ".txt").decode()
            comment = my_zip.getinfo(ext + ".txt").comment.decode()
            ext = content.split()[-1]
            list_of_comments.append(comment)
            print(content)
        except Exception as e:
            print(e)
            break

print("".join(list_of_comments))

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