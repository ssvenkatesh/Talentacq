# -*- coding: utf-8 -*-

from docx import Document
import os
import zipfile
from docxReader import get_docx_text 


def readandprintfile(file):
    if file.endswith('.docx'):
        print(file)
        readDocx(file) 

def readDocx(filepath):
    pars=get_docx_text(filepath)
    WriteToFile(pars)

def WriteToFile(text):
    file=open("output.txt","a")
    file.write(text.encode('utf8'))
    file.write('---------------')
    file.close()

def main():
    print("Reading file from dir")
    for root, dirs, files in os.walk("./../../data/resume/",topdown=False):
        for file in files:
            readandprintfile(os.path.join(root, file))
