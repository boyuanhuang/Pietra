# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import os, math,shutil

import output_shortcuts

########################################################################################################################
#FUNCTIONS
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def OnMouseWheel(event):
    zone_file.yview_scroll(-1*(event.delta/120), "units")
    
"""Searche module starts"""####################################################

def lancer_recherche():
    global canvas_strings_container
    canvas.delete("all")
    canvas_strings_container.delete("all")
    global pathlist, occurencelist, stringlist
    strings = stringlist[0]
    if len(stringlist)>1 :
        for i in range(1, len(stringlist)):
            strings = strings + ' '+ stringlist[i]
    pathlist, occurencelist = output_shortcuts.render_files(strings,'VICHY', rootpath, copymotherdirpath, Historique_container_path)  
    render_clickable_result_list(pathlist)
    return 


def some_callback(event): # note that you must include the event as an arg, even if you don't use it.
    e.delete(0, "end")
    return None

def see_in_directory():
    global pathlist, occurencelist, stringlist
    strings = stringlist[0]
    if len(stringlist)>1 :
        for i in range(1, len(stringlist)):
            strings = strings + ' '+ stringlist[i]
    resultdirpath = output_shortcuts.render_dossier(strings,'VICHY', rootpath, copymotherdirpath, Historique_container_path)
    output_shortcuts.open_path(resultdirpath)
    print(resultdirpath)

    
def voir_Historiques():
    global Historique_container_path
    output_shortcuts.open_path(Historique_container_path)

    
def vider_historiques():
    global Historique_container_path
    shutil.rmtree(Historique_container_path)
    os.mkdir(Historique_container_path)
    
def Enter_clearword_and_create_checkbutton(event):

    stringlist.append(e.get())
    keyword = tk.Label(canvas_strings_container, text=e.get(), height = 1, bg = "white",anchor='e')
    keyword.pack()
    
    e.delete(0, "end")
    return
    
def Empty_researche():
    global canvas_strings_container
    global stringlist, pathlist, occurencelist
    stringlist = []
    pathlist = []
    occurencelist = []
    canvas.delete("all")
    canvas_strings_container.destroy()
    canvas_strings_container = Canvas(displayframe,bg='#FFFFFF',width=100,height=100,scrollregion=(0,0,50000,50000))
    canvas_strings_container.pack(side=LEFT,expand=True,fill=BOTH)

"""Searche module ends"""####################################################

"""Polygone creater starts """####################################################
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
    

def creat_polygon_occurence_display( stringlist, occu_list, center):
    taille = 50
    #Largeur = 4*taille
    #Hauteur = 3*taille
    #center = (Largeur/2,-Hauteur/2)
    pointsout = get_outer_point_list(occu_list, center, taille)
    pointsin = get_inner_point_list(occu_list, center, taille)
    wordsposition = get_words_postion_list(occu_list, center, taille)
    #Canevas_poly = Canvas(root, width = Largeur, height =Hauteur, bg ='white')
    canvas.create_polygon(pointsout, fill="white", outline="black", width=1)
    canvas.create_polygon(pointsin,  fill="red", outline="black", width=1)
    for i in range(len(pointsout)):
        canvas.create_line(center[0], -center[1], pointsout[i][0], pointsout[i][1], width = 1)
        canvas.create_text(wordsposition[i][0], wordsposition[i][1], text = stringlist[i]+ ' = '
        +  str(occu_list[i]))
        
    #Canevas_poly.pack()
    return None  
    
def display_in_zone_polygone(event):
    global occurencelist
    canvas.delete("all")
    occu_list = occurencelist[0]
    creat_polygon_occurence_display(stringlist, occu_list)
    return
"""Polygone Creater ends"""####################################################

"""Clickable result list with icon"""##########################################
def populate1(canvas, pathlist):
    for i,path in enumerate(pathlist):
        t=os.path.basename(pathlist[i])
        for j in range(1):
            if t[-3:] == 'pdf':
                label_nb = tk.Label(canvas, image = pdfimg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                canvas.create_window(50, 100+110*i, window=label_nb) 
                break
            if t[-4:] == 'docx':
                label_nb = tk.Label(canvas, image = docximg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                canvas.create_window(50, 100+110*i,window=label_nb) 
                break
            if t[-4:] == 'pptx':
                label_nb = tk.Label(canvas, image = pptximg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                canvas.create_window(50, 100+110*i,window=label_nb) 
                break
            if t[-4:] == 'xlsx':
                label_nb = tk.Label(canvas, image = exlsimg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                canvas.create_window(50, 100+110*i,window=label_nb) 
                break
            if t[-3:] == 'txt':
                label_nb = tk.Label(canvas, image = txtimg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                canvas.create_window(50, 100+110*i,window=label_nb) 
                break
            if t[-4:] == 'html':
                label_nb = tk.Label(canvas, image = htmlimg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                canvas.create_window(50, 100+110*i,window=label_nb) 
                break

        ith_label_clickabletxt = tk.Label(canvas, text=t, height = 5, bg = "white",anchor='e')
        #ith_label_clickabletxt.grid(row=i, column=1, sticky = W)
        canvas.create_window( 100+ 6*len(t)/2, 100+110*i, window=ith_label_clickabletxt)
        
        #ith_label_clickabletxt.bind("<Button-1>",display_in_zone_polygone)
        
        ith_label_clickabletxt.bind("<Double-Button-1>",lambda e,path=path: output_shortcuts.open_path(path))
       
def populate2(canvas, pathlist):
    for i,path in enumerate(pathlist):
        #t=os.path.basename(pathlist[i])
        ith_center = (600, -140-110*i)        
        occu_list = occurencelist[i]
        creat_polygon_occurence_display(stringlist, occu_list, ith_center)
       

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))
    return

    
def render_clickable_result_list(pathlist):
    populate1(canvas, pathlist)
    populate2(canvas, pathlist)

def callback(event):
    root.focus_set()
    print ("clicked at", event.x, event.y)
    
"""Clickable result list with icon ends """####################################
########################################################################################################################  
root = tk.Tk()
root.title('Pietra Data Explorer')
###############################################################################  MENU HERE
menubar = tk.Menu(root)
############## File menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Upload", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
#############  Historique menu
Historiquemenu = tk.Menu(menubar, tearoff=0)
Historiquemenu.add_command(label="Voir les historiques de recherche", command=voir_Historiques)

Historiquemenu.add_separator()

Historiquemenu.add_command(label="Vider l'historique", command=vider_historiques)
menubar.add_cascade(label="Historique", menu=Historiquemenu)
############## Help 
#
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
############################################################################### Global Data
Historique_container_path = r'/Users/uzik/anaconda/projetPietra/Historiques'

rootpath = r'/Volumes/Pietra/01_PROJET'
#rootpath = r'/Users/uzik/anaconda/projetPietra'
copymotherdirpath = r'/Users/uzik/anaconda/projetPietra/Trash' 

pdfimg  = PhotoImage(file=r'/Users/JulienBailly/anaconda/projetPietra3,0/format icon/pdf.gif')
docximg = PhotoImage(file=r'/Users/JulienBailly/anaconda/projetPietra3,0/format icon/docxresize.gif')
exlsimg = PhotoImage(file=r'/Users/JulienBailly/anaconda/projetPietra3,0/format icon/excelresize.gif')
pptximg = PhotoImage(file=r'/Users/JulienBailly/anaconda/projetPietra3,0/format icon/pptresize.gif')
txtimg  = PhotoImage(file=r'/Users/JulienBailly/anaconda/projetPietra3,0/format icon/txtresize.gif')
htmlimg = PhotoImage(file=r'/Users/JulienBailly/anaconda/projetPietra3,0/format icon/htmlresize.gif')

stringlist = []
pathlist = []
occurencelist = []
 

###############################################################################Clickable file name 
#with icon 
displayframe=Frame(root,width=800,height=800)
displayframe.grid(row=0,column=0)
canvas=Canvas(displayframe,bg='#FFFFFF',width=100,height=100,scrollregion=(0,0,100000,100000))
#canvas = ResizingCanvas(displayframe,width=850, height=400, bg="#FFFFFF",scrollregion=(0,0,50000,50000), highlightthickness=0)
canvas_strings_container = Canvas(displayframe,bg='#FFFFFF',width=200,height=100,scrollregion=(0,0,50000,50000))
#canvas_strings_container = ResizingCanvas(displayframe,width=100, height=100, bg="#FFFFFF",scrollregion=(0,0,50000,50000), highlightthickness=0)
vbar=Scrollbar(displayframe,orient=VERTICAL)
vbar.pack(side=RIGHT,expand=True, fill=Y)
vbar.config(command=canvas.yview)

canvas.config(width=800,height=400)
canvas.config(yscrollcommand=vbar.set)

canvas.pack(side=LEFT,expand=True,fill=BOTH)

############################################################################### Polygone display canvas

 
############################################################################### Search Module Here
e = tk.Entry(displayframe)
e.insert(0, "Ajouter un mots cle (en minuscule)")
e.bind("<Button-1>", some_callback)
e.bind("<Return>", Enter_clearword_and_create_checkbutton)
e.pack()
bouton_lancer_la_recherche = Button(displayframe, text="Go", command = lancer_recherche)
bouton_lancer_la_recherche.pack()

bouton_vider = Button(displayframe, text = "Empty research", command = Empty_researche )
bouton_vider.pack()

bouton_see_directory = Button(displayframe, text = "See in its directory", command = see_in_directory)
bouton_see_directory.pack()
canvas_strings_container.pack(side=LEFT,expand=True,fill=BOTH)


root.mainloop()
#print(stringlist)
#print(pathlist)
#print(occurencelist)