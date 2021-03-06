# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:31:42 2017

@author: Boyuan HUANG
def convert_pdf_to_txt(sourcefilepath, destinationdir):  
    filename_to_create = os.path.basename(sourcefilepath)[:-4]+'.txt'
    file_path = destinationdir + '\\' + filename_to_create
    if os.path.exists(file_path):
        return  
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
    string = retstr.getvalue()
    retstr.close()
    os.chdir(destinationdir)
    
    #print(filename)
    test1 = open(filename_to_create, "w")
    test1.write(string);
    test1.close()
    return 

"""

from subprocess import Popen, PIPE
#import docx
#import codecs
#http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
#from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#from pdfminer.converter import TextConverter
#from pdfminer.layout import LAParams
#from pdfminer.pdfpage import PDFPage
#from io import StringIO
import os, time

import textract
#from textract import pdf2txt


def getPdfText(sourcefilepath, destinationdir):
    text = textract.process(sourcefilepath, extension='pdf').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-4]+'.txt'
    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return

def getPPTtext(sourcefilepath, destinationdir):
    text = textract.process(sourcefilepath, extension='pptx').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-5]+'.txt'

    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return

def getdocxText(sourcefilepath, destinationdir):
    text = textract.process(sourcefilepath, extension='docx').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-5]+'.txt'
    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return


def getdocText(sourcefilepath, destinationdir):
    text = textract.process(sourcefilepath, extension='doc').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-5]+'.txt'
    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return
    
    
def gettxtText(sourcefilepath, destinationdir):
    text = textract.process(sourcefilepath, extension='txt').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-4]+'.txt'
    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return
    

def getxlsxText(sourcefilepath, destinationdir):
    #print(sourcefilepath)
    text = textract.process(sourcefilepath, extension='xlsx').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-5]+'.txt'
    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return

def getxlsText(sourcefilepath, destinationdir):
    #print(sourcefilepath)
    text = textract.process(sourcefilepath, extension='xls').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-5]+'.txt'
    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return

def getHtmlText(sourcefilepath, destinationdir):
    text = textract.process(sourcefilepath, extension='html').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-5]+'.txt'
    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return
    

def document_to_txt(fileadress, destinationdir):
    (filepath, filename) = os.path.split(fileadress)
    if filename[-4:].lower() == ".pdf"  and not(filename[:2]=='~$'):
        try:
            getPdfText(fileadress, destinationdir)
        except:
            pass
            print('pb document_to_txt: ')
            print(fileadress)
        return
    if filename[-4:].lower() == ".doc"  and not(filename[:2]=='~$'):
        try:
            getdocText(fileadress, destinationdir)
        except:
            pass
            print('pb document_to_txt: ')
            print(fileadress)
        return 
    if filename[-5:].lower() == ".docx" and not(filename[:2]=='~$'):
        try:
            getdocxText(fileadress, destinationdir)
        except:
            pass
            print('pb document_to_txt: ')
            print(fileadress)
        return
    if filename[-5:].lower() == ".pptx" and not(filename[:2]=='~$'):
        try:
            getPPTtext(fileadress, destinationdir)
        except:
            pass
            print('pb document_to_txt: ')
            print(fileadress)
        return
    if filename[-5:].lower() == ".xlsx"  and not(filename[:2]=='~$'):
        try:
            getxlsxText(fileadress, destinationdir)
        except:
            pass
            print('pb document_to_txt: ')
            print(fileadress)
        return
    if filename[-4:].lower()==".xls" and not(filename[:2]=='~$'):
        try:
            getxlsText(fileadress, destinationdir)
        except:
            pass
            print('pb document_to_txt: ')
            print(fileadress)
        return
    if filename[-4:].lower() == ".txt"  and not(filename[:2]=='~$'):
        try:
            gettxtText(fileadress, destinationdir)
        except:
            pass
            print('pb document_to_txt: ')
            print(fileadress)
        return
    if (filename[-5:].lower() == ".html" or filename[-4:].lower() == ".htm") and not(filename[:2]=='~$'):
        try:
            getHtmlText(fileadress, destinationdir)
        except:
            pass
            print('pb document_to_txt: ')
            print(fileadress)
        return
    return


###################################################################################

def extractext_without_recopy_again(motherdirpath, rootfoldername, copymotherdirpath):
    rootfolderpath = os.path.join(motherdirpath, rootfoldername)
    copypath = os.path.join(copymotherdirpath, rootfoldername)
    if not os.path.exists(copypath):
        os.makedirs(copypath)
    os.chdir(rootfolderpath)  
    dirlist = os.listdir()
    nb_contents = len(dirlist)
    for i in range(nb_contents) : 
        ieme_sonpath = os.path.join( rootfolderpath, dirlist[i])
        if os.path.isfile(ieme_sonpath):
            copy_txt_file_path = os.path.join(copypath, os.path.basename(ieme_sonpath))
            if not os.path.exists(copy_txt_file_path):
                document_to_txt(ieme_sonpath, copypath)
        elif  os.path.isdir(ieme_sonpath):
            extractext(rootfolderpath, dirlist[i], copypath)
    os.chdir(rootfolderpath)
    return      

def extractext(motherdirpath, rootfoldername, copymotherdirpath):
    rootfolderpath = os.path.join(motherdirpath, rootfoldername)
    #print(rootfolderpath)
    copypath = os.path.join(copymotherdirpath, rootfoldername)
    if not os.path.exists(copypath):
        os.makedirs(copypath)
    os.chdir(rootfolderpath)  
    try:     
        dirlist = os.listdir(rootfolderpath)
        nb_contents = len(dirlist)
        for i in range(nb_contents) : 
            ieme_sonpath = os.path.join( rootfolderpath, dirlist[i])
            if os.path.isfile(ieme_sonpath):
                document_to_txt(ieme_sonpath, copypath)
            elif  os.path.isdir(ieme_sonpath):
                extractext(rootfolderpath, dirlist[i], copypath)
        os.chdir(rootfolderpath)
    except:
        pass
        print('os chdir pb : ')
        print(rootfolderpath)
    return    

##########################################################
'''
destinationdir = r'/Users/uzik/anaconda/projetPietra/Trashr/Andre/CM/_DOCS/Bilans mensuels/2016/07.Septembre'

motherdirpath = r'/Volumes/Pietra/01_PROJET/Andre/CM/_DOCS/Bilans mensuels/2016/07.Septembre'
#r"/run/user/1000/gvfs/afp-volume:host=192.168.0.20,volume=Pietra/01_PROJET"



#motherdirpathdeskup = r'/home/bo/桌面/probleme files'

start_time = time.time()
 
#extractext(motherdirpath, 'VICHY', destinationdir)
extractext(motherdirpath, 'GOOGLE', destinationdir)
#fileadress= r'/home/bo/桌面/probleme files/ACCES COMPTES.docx'
#document_to_txt(fileadress, destinationdir)

#print(11111111111111)

elapse_time = time.time() - start_time
print(elapse_time)

'''










