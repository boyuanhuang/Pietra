# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:11:04 2017

@author: Damaris Durrleman
"""

import os

# find 'string in 'filename' which is contained in folderpath'
def stroccurence(folderpath, filename, stringlist):
    os.chdir(folderpath)
    f = open(filename, 'r')
    text_contenu = f.read()
    local_occurence_list =[]
    for i in range(len(stringlist)):
        local_occurence_list.append(text_contenu.count(stringlist[i]))
        #print(local_occurence_list)
    return  local_occurence_list

#################################################################
# localiser les document .txt contenant 'string' dans un folder 'rootdirpath'
def localiseur(rootdirpath, stringlist, pathlist, occurencelist):
    os.chdir(rootdirpath)  
    dirlist = os.listdir(rootdirpath)
    nb_contents = len(dirlist)
    for i in range(nb_contents) : 
        ieme_sonpath = os.path.join( rootdirpath, dirlist[i])
        if dirlist[i][-4:] == ".txt":
            local_occurence_list = stroccurence(rootdirpath, dirlist[i], stringlist)
            if  not (0 in local_occurence_list): 
                pathlist.append(ieme_sonpath)
                occurencelist.append(local_occurence_list)
        elif  os.path.isdir(ieme_sonpath):
            localiseur(ieme_sonpath, stringlist, pathlist, occurencelist)
    os.chdir(rootdirpath)
    return   

#################################################################

#modifier pathlist en vrai address dans realfolder
def tracebackdir( targetfile_container_path_str, copy_file_container_path_str, pathlist):
    slash_copydirname = '/'+os.path.basename(copy_file_container_path_str)
    for i in range(len(pathlist)):
        string =  targetfile_container_path_str + pathlist[i].split(slash_copydirname)[1]
        leafname = '/'+ os.path.basename(string)
        pathlist[i] = string.split(leafname)[0]
    return
    
    
def tracebackfiles(targetfile_container_path_str, copy_file_container_path_str, pathlist):
    for i in range(len(pathlist)):          
        this_file_name = os.path.basename(pathlist[i])[: -4]  #.txt
        this_parentdir =  os.path.dirname(pathlist[i]) # this .txt's parent dir
        parentdir_of_target = targetfile_container_path_str + this_parentdir.split(copy_file_container_path_str)[1]

        dirlist = os.listdir(parentdir_of_target)
        for x in dirlist :
            if x[: len(this_file_name)] == this_file_name :
                this_file_type = x.split(this_file_name)[1]
        this_real_full_name = this_file_name+ this_file_type
        pathlist[i] = os.path.join(parentdir_of_target, this_real_full_name)
    return


    
#################################################################
