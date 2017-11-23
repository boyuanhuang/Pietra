# script cercle.py
#(C) Fabrice Sincère
from tkinter import *
import random
import math 


def get_outer_point_list(number_list, center, taille):
    n = len(number_list)
    pts_outer = []
    degreelist = [math.pi/2]
    theta = 2*math.pi / n
    for i in range(n-1):
        degreelist.append(degreelist[len(degreelist)-1]+ theta)
    for i in range(n):
        pts_outer.append((taille*math.cos(degreelist[i])+center[0],-taille*math.sin(degreelist[i])-center[1]))
    return pts_outer

def get_words_postion_list(number_list, center, taille):
    n = len(number_list)
    wordsposition = []
    degreelist = [math.pi/2]
    theta = 2*math.pi / n
    for i in range(n-1):
        degreelist.append(degreelist[len(degreelist)-1]+ theta)
    for i in range(n):
        wordsposition.append((taille*(1.4)*math.cos(degreelist[i])+center[0],-taille*(1.2)*math.sin(degreelist[i])-center[1]))
    return wordsposition
    
    
def get_inner_point_list(number_list, center, taille):
    max_de_list = max(number_list)
    n = len(number_list)
    pts_inner = []
    degreelist = [math.pi/2]
    theta = 2*math.pi / n
    for i in range(n-1):
        degreelist.append(degreelist[len(degreelist)-1]+ theta)
    for i in range(n):
        pts_inner.append(((taille*math.cos(degreelist[i])*number_list[i]/max_de_list)+center[0],(-taille*math.sin(degreelist[i])*number_list[i]/max_de_list)-center[1]))
    return pts_inner
    

def creat_polygon_occurence_display(taille, stringlist, occu_list):
    Largeur = 4*taille
    Hauteur = 4*taille
    center = (2*taille,-2*taille)
    pointsout = get_outer_point_list(occu_list, center, taille)
    pointsin = get_inner_point_list(occu_list, center, taille)
    wordsposition = get_words_postion_list(occu_list, center, taille)
    Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
    Canevas.create_polygon(pointsout, fill="white", outline="black", width=2)
    Canevas.create_polygon(pointsin,  fill="red", outline="black", width=2)
    for i in range(len(pointsout)):
        Canevas.create_line(center[0], -center[1], pointsout[i][0], pointsout[i][1], width = 2)
        Canevas.create_text(wordsposition[i][0], wordsposition[i][1], text = stringlist[i]+ ' = '+  str(occu_list[i]))
        
    Canevas.pack(padx =5, pady =5)
    return None

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('test')

# Création d'un widget Canvas (zone graphique)
stringlist = ['a', 'b', 'c', 'd', 'e', 'f', 'Ruodan']
occu_list = [5,2,4,3,1, 3,  1]
taille = 200
creat_polygon_occurence_display(taille, stringlist, occu_list)
# Création d'un widget Button (bouton Go)

Mafenetre.mainloop()