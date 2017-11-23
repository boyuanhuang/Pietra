# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:36:46 2017

@author: Boyuan HUANG


target_file_name = os.path.basename(target_file_adress)
    path = os.path.join(destination_dir_path, target_file_name + '.lnk')
   
    wDir =  os.path.join(target_file_adress, os.pardir)
    icon = target_file_adress

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target_file_adress
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()
    return
    
    
"""
import Parsetxt, strfinder
import os  
import sys

"""
import time, shutil
def removedirafter(duree, path_to_remove):
    time.sleep(duree)
    shutil.rmtree(path_to_remove)
    return
"""
import subprocess

def open_path(path):
    opener ="open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, path])
    return

def creat_shortcut(target_file_adress, destination_dir_path):
    createdlinkpath = os.path.join(destination_dir_path, os.path.basename(target_file_adress))    
    if not os.path.exists(createdlinkpath):
        os.symlink(target_file_adress, createdlinkpath)
    return

#############################################################################


def render_search_file(dirpathlist, strings, Historique_container_path):
    resultdir = Historique_container_path+'/' + strings
    if not os.path.exists(resultdir):
        os.mkdir(resultdir)
    for i in range (len(dirpathlist)):
        creat_shortcut(dirpathlist[i], resultdir)

    return resultdir

def render_search_dir(dirpathlist, strings, Historique_container_path):
    resultdir = Historique_container_path+'/Repertoire_racine_de_' + strings
    if not os.path.exists(resultdir):
        os.mkdir(resultdir)
    for i in range (len(dirpathlist)):
        creat_shortcut(dirpathlist[i], resultdir)

    return resultdir
    
#############################################################################    

def render_dossier(strings, search_targetfile_name, rootpath, copymotherdirpath, Historique_container_path):
    stringlist = strings.split(' ')
    if not os.path.exists(os.path.join(copymotherdirpath, search_targetfile_name)):
        Parsetxt.extractext(rootpath, search_targetfile_name, copymotherdirpath)

    rootdirpath = copymotherdirpath +'/'+search_targetfile_name
    pathlist = []
    occurencelist = []

    strfinder.localiseur(rootdirpath,stringlist, pathlist, occurencelist)

    strfinder.tracebackdir(rootpath, copymotherdirpath, pathlist)

    return render_search_dir(pathlist, strings, Historique_container_path)
 
    
    
    
def render_files(strings, search_targetfile_name, rootpath, copymotherdirpath, Historique_container_path):
    stringlist = strings.split(' ')
    if not os.path.exists(os.path.join(copymotherdirpath, search_targetfile_name)):
        Parsetxt.extractext(rootpath, search_targetfile_name, copymotherdirpath)
        
    rootdirpath = copymotherdirpath +'/'+search_targetfile_name
    pathlist = []
    occurencelist = []

    strfinder.localiseur(rootdirpath,stringlist, pathlist, occurencelist)

    strfinder.tracebackfiles(rootpath, copymotherdirpath, pathlist)

    render_search_file(pathlist, strings, Historique_container_path)

    return (pathlist, occurencelist)
###########################################################################


