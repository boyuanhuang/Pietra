# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:31:42 2017

@author: Boyuan HUANG

"""

import os, time

import textract

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
    text = textract.process(sourcefilepath, extension='xlsx').lower()
    os.chdir(destinationdir)
    filename = os.path.basename(sourcefilepath)[:-5]+'.txt'
    test1 = open(filename, "wb")
    test1.write(text);
    test1.close()
    return

def getxlsText(sourcefilepath, destinationdir):
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
    global malfileadresslist
    (filepath, filename) = os.path.split(fileadress)
    if filename[-4:].lower() == ".pdf"  and not(filename[:2]=='~$'):
        try:
            getPdfText(fileadress, destinationdir)
        except:
            pass
            malfileadresslist.append(fileadress)
        return
    if filename[-4:].lower() == ".doc"  and not(filename[:2]=='~$'):
        try:
            getdocText(fileadress, destinationdir)
        except:
            pass
            malfileadresslist.append(fileadress)
        return 
    if filename[-5:].lower() == ".docx" and not(filename[:2]=='~$'):
        try:
            getdocxText(fileadress, destinationdir)
        except:
            pass
            malfileadresslist.append(fileadress)
        return
    if filename[-5:].lower() == ".pptx" and not(filename[:2]=='~$'):
        try:
            getPPTtext(fileadress, destinationdir)
        except:
            pass
            malfileadresslist.append(fileadress)
        return
    if filename[-5:].lower() == ".xlsx"  and not(filename[:2]=='~$'):
        try:
            getxlsxText(fileadress, destinationdir)
        except:
            pass
            malfileadresslist.append(fileadress)
        return
    if filename[-4:].lower()==".xls" and not(filename[:2]=='~$'):
        try:
            getxlsText(fileadress, destinationdir)
        except:
            pass
            malfileadresslist.append(fileadress)
        return
    if filename[-4:].lower() == ".txt"  and not(filename[:2]=='~$'):
        try:
            gettxtText(fileadress, destinationdir)
        except:
            pass
            malfileadresslist.append(fileadress)
        return
    if (filename[-5:].lower() == ".html" or filename[-4:].lower() == ".htm") and not(filename[:2]=='~$'):
        try:
            getHtmlText(fileadress, destinationdir)
        except:
            pass
            malfileadresslist.append(fileadress)
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
    print(rootfolderpath)
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

destinationdir = r'/Users/uzik/anaconda/projetPietra/Trash'

motherdirpath = r'/Volumes/Pietra/01_PROJET'

todolist1 =['Claudie_Pierlot', 'ALD_Automotive', 'LAB']

todototal = [ 'Teleparis', 'Alibaba', 'Peugeot', 'KLORANE', 'Uber', 'Givenchy', 'CHANEL', 'CANAL+', 'MAC', 'Institut_Français', 'Renault', 'VAL_D_ISERE', 'COLAS', 'Diptyque', 'GOOGLE', '_POUR_GOOGLE', 'VALENTINO', 'LAGARDERE_TRAVEL_RETAIL', 'Fivory', 'BasseTemp', 'Societe_Generale', '_KIT_PETIT_DEJ', 'Teambuilding_Before', 'Way', 'PARIS_ROOFTOP_FESTIVAL', '.TemporaryItems', 'Finley', 'PERRIER_JOUET', 'BNP_Paribas', 'X_Recos_UZIK', 'CAUDALIE', 'MGEN', 'Kering', 'PAYPAL', 'BREDIN_PRAT', 'SXM_Festival', 'Thomas_Duval', 'Oscaro', 'TAO', 'MEETIC', 'Deezer', 'VAN_CLEEF_&_ARPELS', 'SNCF', 'ROCHAS', 'Grand_Rivage', 'Hermes', 'BDRT', 'Thumbs.db', 'BPI', '_KIT_LAB', 'L-Oreal', 'EuroGroup', 'JPG', 'Moët_Hennessy', 'INSERM', 'GREENROOM', 'FACEBOOK', 'Christophe_Robin', 'Clos_Luce', 'Lillet', 'Philip_Morris', 'Pernod', '_KIT_TOUCH', 'ESTEE_LAUDER', '_garage', 'Nina_Ricci', 'Dassault_Systemes', 'Ciroc', 'Communion', 'SFR', 'KWAY', 'Ubisoft', 'PUIG', 'Parker', 'Venezia_festival', 'Salesforce', 'UNIQLO', 'INDEED', 'WAZE', 'Sephora', 'Veuve_Clicquot', 'Chaumet', 'Gobelins', 'BRINKS', 'Lanvin', 'Spotify']

malfileadresslist = []

for name in todolist1:
    print(name)
    start_time = time.time()
    try:
        extractext(motherdirpath, name, destinationdir)
    except:
        pass
    elapse_time = time.time() - start_time
    print(elapse_time)
    print("Pb extract doc HERE")
    print("Pb extract doc HERE")
    print("Pb extract doc HERE")
    print("Pb extract doc HERE")
    print("Pb extract doc HERE")
    print("Pb extract doc HERE")
    print("Pb extract doc HERE")
    print(malfileadresslist)

###############################################################################   HERE I tried to fix xls problem
"""
destinationdir = r'/Users/uzik/anaconda/projetPietra/Trashr/Andre/CM/_DOCS/Bilans mensuels/2016'

motherdirpath = r'/Volumes/Pietra/01_PROJET/Andre/CM/_DOCS/Bilans mensuels/2016'
#r"/run/user/1000/gvfs/afp-volume:host=192.168.0.20,volume=Pietra/01_PROJET"



#motherdirpathdeskup = r'/home/bo/桌面/probleme files'

start_time = time.time()
 
#extractext(motherdirpath, 'VICHY', destinationdir)
extractext(motherdirpath, '07.Septembre', destinationdir)
#fileadress= r'/home/bo/桌面/probleme files/ACCES COMPTES.docx'
#document_to_txt(fileadress, destinationdir)

#print(11111111111111)

elapse_time = time.time() - start_time
print(elapse_time)"""









