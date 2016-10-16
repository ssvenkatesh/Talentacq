# -*- coding: utf-8 -*-

import os

def readandprintfile(file):
    print(file)
    f = open(file,"r")
    print(f.read())
    f.close()

def main():
    print("Reading file from dir")
    for root, dirs, files in os.walk("./../../data/resume/",topdown=False):
        for file in files:
            readandprintfile(os.path.join(root, file))
