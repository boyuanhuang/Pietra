# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:36:46 2017

@author: Damaris Durrleman


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
import subprocess, sys

def open_path(path):
    opener ="open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, path])
    return


