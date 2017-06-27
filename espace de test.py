# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:18:59 2017

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


test = r'C:\Users\Damaris Durrleman\.spyder-py3\testwrite'
filepath = os.path.join(test, 'testpythondoc.txt')
if not os.path.exists(r'C:\Users\Damaris Durrleman\.spyder-py3'):
    os.makedirs(r'C:\Users\Damaris Durrleman\.spyder-py3')


str = getdocxText('testpythondoc.docx')
test1 = open(filepath, "w")
test1.write(str);
test1.close()


filepath = os.path.join(r'C:\Users\Damaris Durrleman\.spyder-py3', 'trytrytry') 
#print(filepath)
#print(os.path.basename(filepath))
os.makedirs(filepath)

jumppath = r'C:\Users\Damaris Durrleman\Desktop\test\couche1'
print(jumppath)
os.chdir(jumppath)
print(os.getcwd())
os.chdir(filepath)
print(os.getcwd())

root = r'C:\Users\Damaris Durrleman\Desktop'
os.mkdir(root)