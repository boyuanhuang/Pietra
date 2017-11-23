# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from filedialog import askdirectory
import os, math,shutil

import output_shortcuts

########################################################################################################################
#FUNCTIONS
"""
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
"""

def donothing(event):
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()
   
'''   
def OnMouseWheel(event):
    zone_file.yview_scroll(-1*(event.delta/120), "units")
'''

def reorderlist(origin_list, wanted_order):
    outputlist = [0]*len(origin_list)
    for i in range(len(wanted_order)):
        outputlist[int(wanted_order[i])-1] = origin_list[i]
    return outputlist
    
"""Menu option """############################################################  

def openfile():
   global rootpath, filename
   fileadress = askdirectory(parent=root)
   (rootpath, filename) = os.path.split(fileadress)
   WLC_PTR_Local_text.set('You are now in '+fileadress)

   
def voir_Historiques():
    global Historique_container_path
    output_shortcuts.open_path(Historique_container_path)

    
def vider_historiques():
    global Historique_container_path
    shutil.rmtree(Historique_container_path)
    os.mkdir(Historique_container_path)
    
"""Searche module starts"""####################################################

def lancer_recherche():  
    global canvas, pathlist, occurencelist, stringlist, actual_stringlist_len    
    canvas.delete("all")    
    actual_stringlist_len = len(stringlist)
    strings = stringlist[0]
    if len(stringlist)>1 :
        for i in range(1, len(stringlist)):
            strings = strings + ' '+ stringlist[i]
    pathlist, occurencelist = output_shortcuts.render_files(strings, filename, rootpath, copymotherdirpath, Historique_container_path)  
    
    i=0
    sortedlist = sorted(zip(occurencelist, pathlist), reverse=True)
    for (ith_occsorted, ith_pathsorted) in sortedlist :
        occurencelist[i] = ith_occsorted
        pathlist[i] = ith_pathsorted
        i+=1  
    if len(stringlist) == 1 :
        render_clickable_result_list(canvas, pathlist, occurencelist)
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
    resultdirpath = output_shortcuts.render_dossier(strings, filename, rootpath, copymotherdirpath, Historique_container_path)
    output_shortcuts.open_path(resultdirpath)


def Enter_clearword_and_create_textbox(event):

    stringlist.append(e.get())
    
    e1 = tk.Entry(canvas_orderboxs_container, width = 2)
    orderboxlist.append(e1)
    e1.insert(0, len(stringlist))
    keyword = tk.Label(canvas_strings_container, text=e.get(), height = 1, bg = "white",anchor='w')
    e1.pack()
    keyword.pack()
    
    e.delete(0, "end")
    return

def change_order():
    global stringlist, occurencelist, canvas_strings_container, canvas, canvas_orderboxs_container
    n = len(stringlist)
    wanted_order = []
    for e in orderboxlist:
        wanted_order.append(e.get())

    stringlist = reorderlist(stringlist, wanted_order)
    for i in range(len(occurencelist)):
        occurencelist[i] = reorderlist(occurencelist[i], wanted_order)
        
    
    #render_clickable_result_list(canvas, pathlist, occurencelist)
    
    canvas_strings_container.destroy()
    canvas_orderboxs_container.destroy()
    
    canvas_strings_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000)) 
    canvas_orderboxs_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
    
    canvas_strings_container.pack(side=LEFT,expand=True,fill=BOTH)    
    canvas_orderboxs_container.pack(side=LEFT,expand=True,fill=BOTH)
    
    for i in range(n):
        e_new = tk.Entry(canvas_orderboxs_container, width = 2)
        e_new.insert(0, i+1)
        e_new.pack()
        orderboxlist[i] = e_new
        keyword = tk.Label(canvas_strings_container, text=stringlist[i], height = 1, bg = "white",anchor='w')
        keyword.pack()
        
    i=0
    for (ith_occsorted, ith_pathsorted) in sorted(zip(occurencelist, pathlist), reverse=True):
        occurencelist[i] = ith_occsorted
        pathlist[i] = ith_pathsorted
        i+=1        
    drawPlot()
    #render_clickable_result_list(pathlist)
    return   

def Empty_researche():
    global canvas_strings_container, canvas_orderboxs_container
    global stringlist, pathlist, occurencelist, orderboxlist, maintain_display_state, actual_stringlist_len
    stringlist = []
    pathlist = []
    occurencelist = []
    orderboxlist = []
    maintain_display_state = False
    actual_stringlist_len = 0
    canvas.delete("all")
    canvas_strings_container.destroy()
    canvas_orderboxs_container.destroy()
    
    canvas_strings_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
    canvas_orderboxs_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
    
    canvas_strings_container.pack(side=LEFT,expand=True,fill=BOTH)
    canvas_orderboxs_container.pack(side=LEFT,expand=True,fill=BOTH)
    

"""DataVis canvas module"""####################################################

def display_this(event):
    if maintain_display_state == True:
        return
    global canvas, canvas_polygone
    if len(stringlist)==2:
        overlapped_oval_list =canvas.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1)
        overlapped_oval_index_list = []
        to_display_pathlist = []
        local_occurencelist = []
        for oval in overlapped_oval_list:
            i = int(canvas.gettags(oval)[0])
            overlapped_oval_index_list.append(i)
            to_display_pathlist.append(pathlist[i])
            local_occurencelist.append(occurencelist[i])
        render_clickable_result_list(canvas_polygone, to_display_pathlist, local_occurencelist)
    if len(stringlist) >= 3 :
        overlapped_pilar_list =canvas.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1)
        overlapped_pilar_index_list = []
        to_display_pathlist = []
        local_occurencelist = []
        for pilar in overlapped_pilar_list:
            i = int(canvas.gettags(pilar)[0])
            overlapped_pilar_index_list.append(i)
            to_display_pathlist.append(pathlist[i])
            local_occurencelist.append(occurencelist[i])
        render_clickable_result_list(canvas_polygone, to_display_pathlist, local_occurencelist)
        
        
def maintain_display_on(event):
    global maintain_display_state
    maintain_display_state = True
    
    global canvas, canvas_polygone
    if len(stringlist)==2:
        overlapped_oval_list =canvas.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1)
        overlapped_oval_index_list = []
        to_display_pathlist = []
        local_occurencelist = []
        for oval in overlapped_oval_list:
            i = int(canvas.gettags(oval)[0])
            overlapped_oval_index_list.append(i)
            to_display_pathlist.append(pathlist[i])
            local_occurencelist.append(occurencelist[i])
        render_clickable_result_list(canvas_polygone, to_display_pathlist, local_occurencelist)
    
    if len(stringlist) >= 3 :
        overlapped_pilar_list =canvas.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1)
        overlapped_pilar_index_list = []
        to_display_pathlist = []
        local_occurencelist = []
        for pilar in overlapped_pilar_list:
            i = int(canvas.gettags(pilar)[0])
            overlapped_pilar_index_list.append(i)
            to_display_pathlist.append(pathlist[i])
            local_occurencelist.append(occurencelist[i])
        render_clickable_result_list(canvas_polygone, to_display_pathlist, local_occurencelist)
 
def lockto2D():
    global lockto2D
    lockto2D = True
    drawPlot()

def unlocktoDefault():
    global lockto2D
    lockto2D = False
    drawPlot()
    
def clearcanvas_polygone(event):
    global maintain_display_state, canvas_polygone    
    if len(canvas.find_overlapping(event.x, event.y, event.x, event.y)) == 0:
        canvas_polygone.delete("all")
        maintain_display_state = False

def drawPlot():
    global stringlist
    if len(stringlist) == 1 :
       lancer_recherche()
       return
    if len(stringlist) == 2 or lockto2D:
        draw2DPlot()
        return
    if len(stringlist) > 2 :
        draw3DPlot()
    return

def draw2DPlot():
    global canvas, occurencelist, actual_stringlist_len
    global RtoGlistbright, origin_coord, axe_len
    if not actual_stringlist_len == len(stringlist):
        lancer_recherche()
    # draw x and y axes
    canvas.delete("all")
    canvas.create_line( origin_coord,origin_coord[0]+ axe_len*1.33, origin_coord[1], width=2) #axe x
    canvas.create_line( origin_coord,origin_coord[0],    origin_coord[1]-axe_len, width=2) #axe y
    nblist = [0, 2,4,6,8,10,12,14,16,18]
    ecart_x = 40
    ecart_y = 30
    # markings on x axis
    for i in range(10):
        x = origin_coord[0] + (i * ecart_x)
        canvas.create_line(x, origin_coord[1],x, origin_coord[1]-5, width=2)
        canvas.create_text(x, origin_coord[1]+4, text='%d'% (nblist[i]), anchor=N)
    canvas.create_line(origin_coord[0] + (10 * ecart_x), origin_coord[1],origin_coord[0] + (10 * ecart_x), origin_coord[1]-5, width=2)
    canvas.create_text(origin_coord[0] + (10 * ecart_x), origin_coord[1]+4, text= '>20', anchor=N)
    canvas.create_text(origin_coord[0] + (13.5 * ecart_x) , origin_coord[1], text= 'occurence de "'+ stringlist[0]+'"', anchor=E)
    
    # markings on y axis
    for i in range(1,10):
        y = origin_coord[1] - (i * ecart_y)
        canvas.create_line(origin_coord[0],y,origin_coord[0]+5,y, width=2)
        canvas.create_text(origin_coord[0]-4,y, text='%d'% (nblist[i]), anchor=E)
    canvas.create_line(origin_coord[0],origin_coord[1] - (10 * ecart_y),origin_coord[0]+5,origin_coord[1] - (10 * ecart_y), width=2)
    canvas.create_text(origin_coord[0]-4,origin_coord[1] - (10 * ecart_y), text='>20' , anchor=E)
    canvas.create_text(origin_coord[0]+axe_len*0.2, origin_coord[1] - 11*ecart_y, text='occurence de "'+ stringlist[1]+'"', anchor=E)
    
    for i in range(len(occurencelist)):
        ovcolor = ''
        try:
            ovcolor = RtoGlistbright[ min(occurencelist[i][2]//2, 10) ]
        except :
            ovcolor = 'skyblue'
        xleft = min(origin_coord[0]+  (0.5*ecart_x*20)-6, origin_coord[0]+  (0.5*ecart_x*occurencelist[i][0])-6)
        yup   = max(origin_coord[1] - (0.5*ecart_y*20)-2, origin_coord[1] - (0.5*ecart_y*occurencelist[i][1])-2)
        xright= min(origin_coord[0] + (0.5*ecart_x*20)+2, origin_coord[0] + (0.5*ecart_x*occurencelist[i][0])+2)
        ydown = max(origin_coord[1] - (0.5*ecart_y*20)+6, origin_coord[1] - (0.5*ecart_y*occurencelist[i][1])+6)
        ov = canvas.create_oval(xleft, yup, xright, ydown, width=1, tags = str(i),outline='black', fill = ovcolor)
        canvas.tag_bind(ov, '<Enter>',func=display_this )
        canvas.tag_bind(ov, '<Button-1>',func= maintain_display_on )


def draw3DPlot():
    global origin_coord, axe_len, theta, canvas
    
    canvas.delete("all")
    if not actual_stringlist_len == len(stringlist):
        lancer_recherche()
    #draw x,y,z axes
    axe_x = line( origin_coord, [1,0] , 1.4*axe_len)
    axe_z = line( origin_coord, [0,-1], axe_len)
    axe_y = line( origin_coord, [0,-1], axe_len)

    axe_y.canvas_rotate_line(canvas, theta, width =2)

    axe_x.display_line(canvas, width = 4)
    axe_y.display_line(canvas, width = 3)
    axe_z.display_line(canvas, width = 4)
    
    nblist = [0,2,4,6,8,10,12,14,16,18,20]
    ecart_x = 40
    ecart_y = 30
    ecart_z = 30
    
    for i in range(1,11):
        #mark axe x,y,z
        z = origin_coord[1] - (i * ecart_z)
        canvas.create_line(origin_coord[0],z,origin_coord[0]-5,z, width=1)
        canvas.create_text(origin_coord[0]-7,z, text='%d'% (nblist[i]), anchor=E)
        
        line([origin_coord[0]+axe_y.direction[0]*ecart_y*i-6, origin_coord[1]+axe_y.direction[1]*ecart_y*i],   axe_x.direction, axe_len*1.37).display_line(canvas, width= 1 )
        canvas.create_text(origin_coord[0]+axe_y.direction[0]*ecart_y*i-10, origin_coord[1]+axe_y.direction[1]*ecart_y*i, text='%d'% (nblist[i]), anchor=E)
        
        line([origin_coord[0]+axe_x.direction[0]*ecart_x*i,   origin_coord[1]+axe_x.direction[1]*ecart_x*i+3], axe_y.direction, axe_len*1.03).display_line(canvas, width= 1 )
        canvas.create_text(origin_coord[0]-ecart_x+i*ecart_x, origin_coord[1]+4, text='%d'% (nblist[i-1]), anchor=N)
         
    canvas.create_text(origin_coord[0]+10*ecart_x, origin_coord[1]+4, text='>20', anchor=N)
    canvas.create_text(origin_coord[0]+axe_y.direction[0]*ecart_y*12-70, origin_coord[1]+axe_y.direction[1]*ecart_y*10, text='>', anchor=E)    
    canvas.create_text(origin_coord[0]-7, origin_coord[1] - (10 * ecart_z), text='>20', anchor=E)
    
    canvas.create_text(origin_coord[0]+1.8*axe_len, origin_coord[1], text= 'occurence de "'+ stringlist[0]+'"', anchor=E)
    canvas.create_text(origin_coord[0]+axe_y.direction[0]*axe_len*1.2 + 30, origin_coord[1]+axe_y.direction[1]*axe_len*1.2, text='occurence de "'+ stringlist[1]+'"', anchor=E)
    canvas.create_text(origin_coord[0]+axe_len*0.2, -axe_len*1.1 + origin_coord[1], text= 'occurence de "'+ stringlist[2]+'"', anchor=E)
    
    # To display pilar from the back to the front 
    order = [i for i in range(len(occurencelist))]
    twolast = [[occu[1], occu[2]] for occu in occurencelist]
    
    
    display_order = [nb[1] for nb in sorted(zip(twolast, order), key = lambda x : x[0], reverse = True)]

    for i in display_order:
        makepilar(i, occurencelist[i], theta, canvas, origin_coord)


"""Pilar creater """#############################################################
class line:
    # origin, diretion, length, end 
    def __init__(self, origin, xylist, length):
        #self.name = name   # tag
        self.origin = origin        
        dirnorme = math.sqrt(xylist[0]*xylist[0]+xylist[1]*xylist[1])
        self.direction = [xylist[0]/dirnorme, xylist[1]/dirnorme]
        self.length = length
        self.end = [origin[0]+length*xylist[0], origin[1]+length*xylist[1]]

    def rotate(self, theta):  #theta in gradiant
        self.direction = [self.direction[0]*math.cos(theta) - self.direction[1]*math.sin(theta), self.direction[1]*math.cos(theta)+self.direction[0]*math.sin(theta)]
        self.end = [self.origin[0]+self.length*self.direction[0], self.origin[1]+self.length*self.direction[1]]
        return
        
    def deplacer(self, dx, dy):
        self.origin[0]+= dx
        self.origin[1]+= dy
        self.end = [self.origin[0]+self.length*self.direction[0], self.origin[1]+self.length*self.direction[1]]
    
    def lengthtimes(self, rapport):
        self.length *= rapport
        self.end = [self.origin[0]+self.length*self.direction[0], self.origin[1]+self.length*self.direction[1]]

    def delete_line(self, canvas):
        canvas.delete(canvas.find_overlapping(self.end[0], self.end[1], self.end[0], self.end[1]))
        
    def display_line(self, canvas, width):
        canvas.create_line(self.origin[0], self.origin[1], self.end[0], self.end[1], width = width )
        
    
    def canvas_rotate_line(self, canvas, theta, width):
        self.delete_line(canvas)
        self.rotate(theta)
        self.display_line(canvas, width)
        
    def canvas_deplacer_line(self, canvas, dx, dy, width):
        self.delete_line(canvas)
        self.deplacer(dx, dy)
        self.display_line(canvas, width) 

   
def makepilar(i, occu, theta, canvas, origin_coord):   #occu est une list d'occurence 

    global RtoGlistbright, RtoGlistdark, RtoGlistdim
    taille = 3 
    ecart_x = 40
    ecart_y = 30
    ecart_z = 30
    
    x = min(origin_coord[0] + 0.5*ecart_x*occu[0] + 0.5*ecart_y*occu[1]*math.cos(theta), origin_coord[0] + 0.5*ecart_x*20 + 0.5*ecart_y*20*math.cos(theta))
    y = max(origin_coord[1] - 0.5*ecart_y*occu[1]*math.sin(theta),origin_coord[1] - 0.5*ecart_y*20*math.sin(theta))
    z = min(0.5*ecart_z*occu[2], 0.5*ecart_z*20)

    facade = [x+taille, y+taille-z, x-taille, y+taille-z, x-taille, y +taille, x+taille, y +taille ]
    lateral =[x+taille, y+taille-z, 
              x+taille, y +taille, 
              x+taille*(1+1.5*math.sin(theta))  , y +taille*(1-1.5*math.cos(theta)), 
              x+taille*(1+1.5*math.sin(theta))  , y +taille*(1-1.5*math.cos(theta))-z  ]
    
    roof = [x+taille, y+taille-z, 
            x-taille, y+taille -z,
            x-taille*(1-1.5*math.sin(theta))  , y +taille*(1-1.5*math.cos(theta)) -z,
            x+taille*(1+1.5*math.sin(theta))  , y +taille*(1-1.5*math.cos(theta)) -z ] 
    
    facadecolor = '#006ce2'
    lateralcolor = '#2b90ff'
    roofcolor = '#66afff'
    try:
        k = min(occurencelist[i][3]//2, 10)
        facadecolor = RtoGlistdark[k]
        lateralcolor = RtoGlistdim[k]
        roofcolor = RtoGlistbright[k]
    except :
        pass
    facade_area  = canvas.create_polygon(facade,  width = 1, fill = facadecolor, outline = 'black', tags = i)
    lateral_area = canvas.create_polygon(lateral, width = 1, fill = lateralcolor,outline = 'black', tags = i)
    roof_area    = canvas.create_polygon(roof,    width = 1, fill = roofcolor,   outline = 'black', tags = i)
    canvas.tag_bind(facade_area, '<Enter>',func=display_this )
    canvas.tag_bind(lateral_area, '<Enter>',func=display_this )
    canvas.tag_bind(roof_area, '<Enter>',func=display_this )
    
    canvas.tag_bind(facade_area, '<Button-1>',func= maintain_display_on )
    canvas.tag_bind(lateral_area, '<Button-1>',func= maintain_display_on )
    canvas.tag_bind(roof_area, '<Button-1>',func= maintain_display_on )



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
    

def creat_polygon_occurence_display(thiscanvas, stringlist, occu_list, center):
    if len(stringlist) ==1 :
        thiscanvas.create_text(center[0], -center[1], text = stringlist[0]+ ' : '
        +  str(occu_list[0]))
        return
    if len(stringlist) ==2 :
        wordsposition = [[center[0], -center[1]-10], [center[0], -center[1]+10]]
        for i in range(2):
            thiscanvas.create_text(wordsposition[i][0], wordsposition[i][1], text = stringlist[i]+ ' : ' +  str(occu_list[i]) )
        return      
    taille = 50
    pointsout = get_outer_point_list(occu_list, center, taille)
    pointsin = get_inner_point_list(occu_list, center, taille)
    wordsposition = get_words_postion_list(occu_list, center, taille)
    
    thiscanvas.create_polygon(pointsout, fill="white", outline="black", width=1)
    thiscanvas.create_polygon(pointsin,  fill="red", outline="black", width=1)
    for i in range(len(pointsout)):
        thiscanvas.create_line(center[0], -center[1], pointsout[i][0], pointsout[i][1], width = 1)
        thiscanvas.create_text(wordsposition[i][0], wordsposition[i][1], text = stringlist[i]+ ' : '
        +  str(occu_list[i]))
        

    return None  


"""Clickable result list with icon"""##########################################
def populate1(thiscanvas, pathlist):
    ecart = 100 +10*len(stringlist)
    for i,path in enumerate(pathlist):
        t=os.path.basename(pathlist[i])
        for j in range(1):
            if t[-3:].lower() == 'pdf':
                label_nb = tk.Label(thiscanvas, image = pdfimg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                thiscanvas.create_window(50, 100+ecart*i, window=label_nb) 
                break
            if t[-4:].lower() == 'docx' or t[-4:].lower() == '.doc':
                label_nb = tk.Label(thiscanvas, image = docximg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                thiscanvas.create_window(50, 100+ecart*i,window=label_nb) 
                break
            if t[-4:].lower() == 'pptx':
                label_nb = tk.Label(thiscanvas, image = pptximg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                thiscanvas.create_window(50, 100+ecart*i,window=label_nb) 
                break
            if t[-4:].lower() == 'xlsx':
                label_nb = tk.Label(thiscanvas, image = exlsimg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                thiscanvas.create_window(50, 100+ecart*i,window=label_nb) 
                break
            if t[-3:].lower() == 'txt':
                label_nb = tk.Label(thiscanvas, image = txtimg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                thiscanvas.create_window(50, 100+ecart*i,window=label_nb) 
                break
            if t[-4:].lower() == 'html':
                label_nb = tk.Label(thiscanvas, image = htmlimg , width=46, height = 46, bg = "white")
                label_nb.img = pdfimg
                #label_nb.grid(row=i, column=0)
                thiscanvas.create_window(50, 100+ecart*i,window=label_nb) 
                break

        ith_label_clickabletxt = tk.Label(thiscanvas, text=t, height = 5, bg = "white",anchor='e')
        #ith_label_clickabletxt.grid(row=i, column=1, sticky = W)
        thiscanvas.create_window( 100+ 6*len(t)/2, 100+ecart*i, window=ith_label_clickabletxt)
        
        #ith_label_clickabletxt.bind("<Button-1>",display_in_zone_polygone)
        
        ith_label_clickabletxt.bind("<Double-Button-1>",lambda e,path=path: output_shortcuts.open_path(path))
       
def populate2(thiscanvas, pathlist, local_occurencelist):
    ecart = 100 +10*len(stringlist)
    for i,path in enumerate(pathlist):
        ith_center = (600, -100-ecart*i)        
        occu_list = local_occurencelist[i]
        creat_polygon_occurence_display(thiscanvas, stringlist, occu_list, ith_center)
       

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))
    return

    
def render_clickable_result_list(canvas, pathlist, local_occurencelist):
    canvas.delete("all")
    populate1(canvas, pathlist)
    populate2(canvas, pathlist, local_occurencelist)
    
    
def see_all_results():
    global pathlist, occurencelist
    all_res_window = tk.Toplevel(root)
    

    all_res_canvas = tk.Canvas(all_res_window, bg='white',width=400,height=400,scrollregion=(0,0,100000,100000))
    
    vbar2=tk.Scrollbar(all_res_window,orient=VERTICAL)
    vbar2.pack(side=RIGHT,expand=True, fill=Y)
    vbar2.config(command=all_res_canvas.yview)
    
    all_res_canvas.config(width=800,height=400)
    all_res_canvas.config(yscrollcommand=vbar2.set)
    all_res_canvas.pack(side=LEFT,expand=True,fill=BOTH)
    
    render_clickable_result_list(all_res_canvas, pathlist, occurencelist)
    return    
    
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
filemenu.add_command(label="Open", command=openfile)
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
#############  Display mode menu


Displaymodemenu = tk.Menu(menubar, tearoff=0)

Displaymodemenu.add_command(label="Default display mode", command= unlocktoDefault)
Displaymodemenu.add_separator()
Displaymodemenu.add_command(label="2D display", command= lockto2D)
menubar.add_cascade(label="Display mode", menu=Displaymodemenu)


############## Help 
#
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
############################################################################### Global Data & parameters
Historique_container_path = r'/home/bo/桌面/Historique de recherche'

rootpath = r'/home/bo/桌面'
#rootpath = r'/Users/uzik/anaconda/projetPietra'
copymotherdirpath = r'/home/bo/桌面/test' 
filename = 'final test'

pdfimg  = PhotoImage(file=r'/home/bo/桌面/projetPietra/format icon/pdf.gif')
docximg = PhotoImage(file=r'/home/bo/桌面/projetPietra/format icon/docxresize.gif')
exlsimg = PhotoImage(file=r'/home/bo/桌面/projetPietra/format icon/excelresize.gif')
pptximg = PhotoImage(file=r'/home/bo/桌面/projetPietra/format icon/pptresize.gif')
txtimg  = PhotoImage(file=r'/home/bo/桌面/projetPietra/format icon/txtresize.gif')
htmlimg = PhotoImage(file=r'/home/bo/桌面/projetPietra/format icon/htmlresize.gif')

RtoGlistbright = ['#FF0000', '#FF3300', '#ff6600', '#ff9900', '#FFCC00', '#FFFF00', '#ccff00', '#99ff00', '#66ff00', '#33ff00', '#00FF00']
#          [   1 Red    2Red(Orange)  4          6        8Gold     10Yellow      12         14         16         18       >20 Lime ] 
RtoGlistdim   = ['#c60000',  '#c63300',  '#c64f00','#dd8500','#dbaf00',  '#e0e000',  '#add800', '#7dd100','#56d800','#2bd800','#00c600']
RtoGlistdark = ['#870000' ,  '#a52100','#8c3700' ,'#ba7000','#b28e00',  '#c1c100',  '#8aad00', '#67ad00','#47b200','#22ad00','#00a000']

maintain_display_state = False
lockto2D = False


actual_stringlist_len = 0
origin_coord = [100, 350]
axe_len = 300
theta = math.pi/4

stringlist = []
pathlist = []
occurencelist = []
orderboxlist = []



###############################################################################
displayframe=tk.Frame(root,width=800,height=800)
displayframe.grid(row=0,column=0)

canvas = tk.Canvas(displayframe,bg='#c6edf4',width=100,height=100,scrollregion=(0,0,100000,100000))

#canvas = ResizingCanvas(displayframe,width=850, height=400, bg="#FFFFFF",scrollregion=(0,0,50000,50000), highlightthickness=0)
canvas_strings_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
canvas_orderboxs_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
canvas_polygone =tk.Canvas(displayframe,bg='#FFFFFF',width=100,height=500,scrollregion=(0,0,50000,50000))


#canvas_strings_container = ResizingCanvas(displayframe,width=100, height=100, bg="#FFFFFF",scrollregion=(0,0,50000,50000), highlightthickness=0)
vbar = tk.Scrollbar(displayframe,orient=VERTICAL)
vbar.pack(side=RIGHT,expand=True, fill=Y)
vbar.config(command=canvas.yview)

vbar1= tk.Scrollbar(displayframe,orient=VERTICAL)
vbar1.pack(side=RIGHT,expand=True, fill=Y)
vbar1.config(command=canvas_polygone.yview)

canvas.config(width=800,height=400)
canvas.config(yscrollcommand=vbar.set)

canvas_polygone.config(width=800,height=400)
canvas_polygone.config(yscrollcommand=vbar1.set)

canvas_polygone.pack(side=BOTTOM,expand=True,fill=BOTH)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

canvas.bind("<Button-1>", clearcanvas_polygone)

WLC_PTR_Local_text = tk.StringVar()
WLC_PTR_Local = tk.Label(displayframe, textvariable = WLC_PTR_Local_text ,anchor = 'ne').pack()
WLC_PTR_Local_text.set('You are now in '+ rootpath + '/'+ filename)

############################################################################### Polygone display canvas

 
############################################################################### Search Module Here
e = tk.Entry(displayframe, width = 35)
e.insert(0, "Add a keyword (en minuscule)")
e.bind("<Button-1>", some_callback)
e.bind("<Return>", Enter_clearword_and_create_textbox)
e.pack()
bouton_lancer_la_recherche = tk.Button(displayframe, text="Go", command = drawPlot )
bouton_lancer_la_recherche.pack()

bouton_vider = tk.Button(displayframe, text = "Empty research", command = Empty_researche )
bouton_vider.pack()

bouton_see_directory = tk.Button(displayframe, text = "See in its directory", command = see_in_directory)
bouton_see_directory.pack()

canvas_strings_container.pack(side=LEFT,expand=True,fill=BOTH)
canvas_orderboxs_container.pack(side=LEFT,expand=True,fill=BOTH)


bouton_chg_odr = tk.Button(displayframe, text = "Change order", command = change_order )
bouton_chg_odr.pack()

bouton_see_all_result = tk.Button(displayframe, text = "See whole result list", command = see_all_results )
bouton_see_all_result.pack()

root.mainloop()
#print(stringlist)
#print(pathlist)
#print(occurencelist)
#print(occurencelist)
#print(stringlist)