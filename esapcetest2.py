# -*- coding: utf-8 -*-
import os




def quinestpasla(biglist, smallist):
    absent = []
    for i in range(len(biglist)):
        if not (biglist[i] in smallist):
            absent.append(biglist[i])
    return absent

'''
biglist = []
for pdf in os.listdir(r'/Users/uzik/anaconda/projetPietra/PDF samples'):
    biglist.append(pdf[:-4])


smallist = []
for pdf in os.listdir(r'/Users/uzik/anaconda/projetPietra/Trash/PDF samples'):
    smallist.append(pdf[:-4])




print(quinestpasla(biglist, smallist))
print(os.getcwd())
os.chdir(r'/Users')
print(os.getcwd())
'''
'/Volumes/Pietra/01_PROJET/VICHY/31 - AO social/00_AO/03 - Présentation/UZIK x VICHY Social Media.pdf.sb-1141d16c-mU5NQt'
'/Volumes/Pietra/01_PROJET/VICHY/31 - AO social+ graphic guidelines/00_AO/03 - Présentation/UZIK x VICHY Social Media.pdf.sb-1141d16c-mU5NQt'

samplespath = r'/Volumes/Pietra/01_PROJET/VICHY/31 - AO social+ graphic guidelines/00_AO/03 - Présentation/UZIK x VICHY Social Media.pdf.sb-1141d16c-mU5NQt'
samplesoldlist = os.listdir(samplespath)
print(samplesoldlist)
print(len(samplesoldlist))

"""

from Tkinter import *
from tkFileDialog import askopenfilename, askdirectory

def openfile():
   fileadress = askdirectory()
   print(fileadress)
   (file_container_path, filename) = os.path.split(fileadress)

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
"""




