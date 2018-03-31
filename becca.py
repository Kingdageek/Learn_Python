# becca.py
import os
from os.path import join, getsize

"""
def recurse_files(file_path):
    for filename in os.listdir(file_path):
        if os.path.isfile(filename):
            total += os.path.getsize(os.path.join(file_path, filename))
        elif os.path.isdir(filename):
            recurse_files(os.path.join(file_path, filename))

recurse_files("D://")

print(total)
"""


for root, dirs, files in os.walk('D:'):
    print(root, " consumes ", end="")
    print(sum([getsize(join(root, name)) for name in files]), end="")
    print(" bytes in ", len(files), " non-directory files ")


