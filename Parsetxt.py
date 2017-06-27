# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:31:42 2017

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


def convert_pdf_to_txt(sourcefilepath, destinationdir):  
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(sourcefilepath, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-4]+'.txt'
    #print(filename)
    test1 = open(filename, "w")
    test1.write(str);
    test1.close()
    return 




def getdocxText(sourcefilepath, destinationdir):
    doc = docx.Document(sourcefilepath)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-4]+'.txt'
    #print(filename)
    str = '\n'.join(fullText)
    test1 = open(filename, "w")
    test1.write(str);
    test1.close()
    return 


def document_to_txt(fileadress, destinationdir):
    (filepath, filename) = os.path.split(fileadress)
    if filename[-4:] == ".pdf":
        return convert_pdf_to_txt(fileadress, destinationdir)
    



###################################################################################

def extractext(motherdirpath, rootfoldername, copymotherdirpath):
    rootfolderpath = os.path.join(motherdirpath, rootfoldername)
    copypath = os.path.join(copymotherdirpath, rootfoldername)
    os.makedirs(copypath)
    os.chdir(rootfolderpath)  
    dirlist = os.listdir()
    nb_contents = len(dirlist)
    for i in range(nb_contents) : 
        ieme_sonpath = os.path.join( rootfolderpath, dirlist[i])
        if os.path.isfile(ieme_sonpath):
            document_to_txt(ieme_sonpath, copypath)
        elif  os.path.isdir(ieme_sonpath):
            extractext(rootfolderpath, dirlist[i], copypath)
    os.chdir(rootfolderpath)
    return      









##########################################################
def extract2(rootdirpath, copymotherdirpath):
    os.chdir(rootdirpath) 
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            destinationdir = 
            convert_pdf_to_txt(sourcefilepath, destinationdir)
        for name in dirs:
            copypath = os.path.join(copymotherdirpath, rootfoldername)
            os.makedirs(copypath)
    return

           

copymotherdirpath = r'C:\Users\Damaris Durrleman\.spyder-py3'   

rootpath = r'C:\Users\Damaris Durrleman\Desktop'

#extractext(rootpath,'test', copymotherdirpath, )
fileadress = r'C:\Users\Damaris Durrleman\Desktop\test\couche1\PACO_RABANNE_REGLEMENT_FANTASY _FR.docx'
#document_to_txt(fileadress, rootpath)
#getdocxText(fileadress, rootpath)




































