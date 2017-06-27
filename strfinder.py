# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:11:04 2017

@author: Damaris Durrleman
"""

from subprocess import Popen, PIPE
import docx

#http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os

def stroccurence(folderpath, filename, string):
    os.chdir(folderpath)
    f = open(filename, 'r')
    occurences = f.read().count(string)
    return  occurences


folderpath = r'C:\Users\Damaris Durrleman\.spyder-py3\test\couche1\couche2'
filename = '20150703_BLACKXS_VIDEOS.txt'
str = 'video'
stroccurence(folderpath,filename,str)


#################################################################

def localiseur(rootdirpath,string, pathlist, occurencelist):
    
    os.chdir(rootdirpath)  
    dirlist = os.listdir()
    nb_contents = len(dirlist)
    
    for i in range(nb_contents) : 
        ieme_sonpath = os.path.join( rootdirpath, dirlist[i])
        if dirlist[i][-4:] == ".txt":
            nb_occurence = stroccurence(rootdirpath, dirlist[i], string)
            if nb_occurence > 0 : 
                pathlist.append(ieme_sonpath)
                occurencelist.append(nb_occurence)
            
        elif  os.path.isdir(ieme_sonpath):
            localiseur(ieme_sonpath, string, pathlist, occurencelist)
    os.chdir(rootdirpath)
    return   

#################################################################

def traceback(pathlist):
    





#################################################################
rootdirpath = r'C:\Users\Damaris Durrleman\.spyder-py3\test'
string = 'video'

pathlist = []
occurencelist = []

localiseur(rootdirpath,string, pathlist, occurencelist)
 
print(pathlist)
print('\n')
print(occurencelist)
 
 
 
 
 
 
 
 
 
 
 
 
 