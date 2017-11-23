# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from filedialog import askdirectory
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


def donothing(event):
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def OnMouseWheel(event):
    zone_file.yview_scroll(-1*(event.delta/120), "units")
    
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
   print(fileadress)
   
def voir_Historiques():
    global Historique_container_path
    output_shortcuts.open_path(Historique_container_path)

    
def vider_historiques():
    global Historique_container_path
    shutil.rmtree(Historique_container_path)
    os.mkdir(Historique_container_path)
    
"""Searche module starts"""####################################################

def lancer_recherche():
    canvas.delete("all")
    global pathlist, occurencelist, stringlist
    strings = stringlist[0]
    if len(stringlist)>1 :
        for i in range(1, len(stringlist)):
            strings = strings + ' '+ stringlist[i]
    pathlist, occurencelist = output_shortcuts.render_files(strings, filename, rootpath, copymotherdirpath, Historique_container_path)  
    
    i=0
    for (ith_occsorted, ith_pathsorted) in sorted(zip(occurencelist, pathlist), reverse=True):
        occurencelist[i] = ith_occsorted
        pathlist[i] = ith_pathsorted
        i+=1  
        
    #render_clickable_result_list(pathlist)
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
    #print(resultdirpath)

def Enter_clearword_and_create_checkbutton(event):

    stringlist.append(e.get())
    
    e1 = Entry(canvas_orderboxs_container, width = 2)
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
        
    
    render_clickable_result_list(canvas, pathlist, occurencelist)
    
    canvas_strings_container.destroy()
    canvas_orderboxs_container.destroy()
    
    canvas_strings_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000)) 
    canvas_orderboxs_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
    
    canvas_strings_container.pack(side=LEFT,expand=True,fill=BOTH)    
    canvas_orderboxs_container.pack(side=LEFT,expand=True,fill=BOTH)
    
    for i in range(n):
        e_new = Entry(canvas_orderboxs_container, width = 2)
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
    global stringlist, pathlist, occurencelist, orderboxlist
    stringlist = []
    pathlist = []
    occurencelist = []
    orderboxlist = []
    canvas.delete("all")
    canvas_strings_container.destroy()
    canvas_orderboxs_container.destroy()
    
    canvas_strings_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
    canvas_orderboxs_container = tk.Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
    
    canvas_strings_container.pack(side=LEFT,expand=True,fill=BOTH)
    canvas_orderboxs_container.pack(side=LEFT,expand=True,fill=BOTH)
    

"""DataVis module"""####################################################

def display_this(event):
    global canvas, canvas_polygone
    overlapped_oval_list =canvas.find_overlapping(event.x-2, event.y-2, event.x+2, event.y+2)
    overlapped_oval_index_list = []
    to_display_pathlist = []
    local_occurencelist = []
    for oval in overlapped_oval_list:
        i = int(canvas.gettags(oval)[0])
        overlapped_oval_index_list.append(i)
        to_display_pathlist.append(pathlist[i])
        local_occurencelist.append(occurencelist[i])
    render_clickable_result_list(canvas_polygone, to_display_pathlist, local_occurencelist)
'''    
def maintain_display(event):
    global maintain_display_state
    if not canvas.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1) ==():
        maintain_display_state = True
    #print(maintain_display_state)
'''
 
def clearcanvas_polygone(event):
    canvas_polygone.delete("all")

    
def drawPlot():
    lancer_recherche()
    global canvas, occurencelist
    # draw x and y axes
    canvas.delete("all")
    canvas.create_line(100,350,600,350, width=2)
    canvas.create_line(100,350,100,50,  width=2)
    nblist = [0, 2,4,6,8,10,20,40,60]
    # markings on x axis
    for i in range(8):
        x = 100 + (i * 40)
        canvas.create_line(x,350,x,345, width=2)
        canvas.create_text(x,354, text='%d'% (nblist[i]), anchor=N)
    canvas.create_text(620,354, text=stringlist[0], anchor=E)
    
    # markings on y axis
    for i in range(1,8):
        y = 250 - (i * 40)
        canvas.create_line(100,y+100,105,y+100, width=2)
        canvas.create_text(96,y+100, text='%d'% (nblist[i]), anchor=E)
    canvas.create_text(96,-70+100, text=stringlist[1], anchor=E)
    
    for i in range(len(occurencelist)):
        ov = canvas.create_oval(100+(20*occurencelist[i][0])-6 , 350 - (20*occurencelist[i][1])-2, 100 + (20*occurencelist[i][0])+2, 350 - (20*occurencelist[i][1])+6, width=1, tags = str(i),outline='black', fill='SkyBlue2')
        #ovallist.append(ov)
        canvas.tag_bind(ov, '<Enter>',func=display_this )
        #canvas.tag_bind(ov, '<Leave>',func= hide_this )
        #canvas.tag_bind(ov, '<Button-1>',func= maintain_display )
#    for oval in ovalslist :
        
    # display window and wait for it to close

    

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
    #Largeur = 4*taille
    #Hauteur = 3*taille
    #center = (Largeur/2,-Hauteur/2)
    pointsout = get_outer_point_list(occu_list, center, taille)
    pointsin = get_inner_point_list(occu_list, center, taille)
    wordsposition = get_words_postion_list(occu_list, center, taille)
    #Canevas_poly = Canvas(root, width = Largeur, height =Hauteur, bg ='white')
    thiscanvas.create_polygon(pointsout, fill="white", outline="black", width=1)
    thiscanvas.create_polygon(pointsin,  fill="red", outline="black", width=1)
    for i in range(len(pointsout)):
        thiscanvas.create_line(center[0], -center[1], pointsout[i][0], pointsout[i][1], width = 1)
        thiscanvas.create_text(wordsposition[i][0], wordsposition[i][1], text = stringlist[i]+ ' : '
        +  str(occu_list[i]))
        
    #Canevas_poly.pack()
    return None  
'''    
def display_in_zone_polygone(event):
    global occurencelist
    thiscanvas.delete("all")
    occu_list = occurencelist[0]
    creat_polygon_occurence_display(thiscanvas,stringlist, occu_list)
    return'''
"""Polygone Creater ends"""####################################################

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
    render_clickable_result_list(canvas, pathlist, occurencelist)
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
############## Help 
#
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
############################################################################### Global Data
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

#maintain_display_state = False

stringlist = []
pathlist = []
occurencelist = []
orderboxlist = []


###############################################################################
displayframe=Frame(root,width=800,height=800)
displayframe.grid(row=0,column=0)

canvas=Canvas(displayframe,bg='#c6edf4',width=100,height=100,scrollregion=(0,0,100000,100000))

#canvas = ResizingCanvas(displayframe,width=850, height=400, bg="#FFFFFF",scrollregion=(0,0,50000,50000), highlightthickness=0)
canvas_strings_container = Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
canvas_orderboxs_container = Canvas(displayframe,bg='white',width=100,height=100,scrollregion=(0,0,50000,50000))
canvas_polygone =Canvas(displayframe,bg='yellow',width=100,height=500,scrollregion=(0,0,50000,50000))


#canvas_strings_container = ResizingCanvas(displayframe,width=100, height=100, bg="#FFFFFF",scrollregion=(0,0,50000,50000), highlightthickness=0)
vbar=Scrollbar(displayframe,orient=VERTICAL)
vbar.pack(side=RIGHT,expand=True, fill=Y)
vbar.config(command=canvas.yview)

vbar1=Scrollbar(displayframe,orient=VERTICAL)
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
e.bind("<Return>", Enter_clearword_and_create_checkbutton)
e.pack()
bouton_lancer_la_recherche = Button(displayframe, text="Go", command = drawPlot )
bouton_lancer_la_recherche.pack()

bouton_vider = Button(displayframe, text = "Empty research", command = Empty_researche )
bouton_vider.pack()

bouton_see_directory = Button(displayframe, text = "See in its directory", command = see_in_directory)
bouton_see_directory.pack()

canvas_strings_container.pack(side=LEFT,expand=True,fill=BOTH)
canvas_orderboxs_container.pack(side=LEFT,expand=True,fill=BOTH)


bouton_chg_odr = Button(displayframe, text = "Change order", command = change_order )
bouton_chg_odr.pack()

bouton_see_all_result = Button(displayframe, text = "See whole result list", command = see_all_results )
bouton_see_all_result.pack()

bouton_see_spot_plot = Button(displayframe, text = "Results spot-plot", command = drawPlot )
bouton_see_spot_plot.pack()
root.mainloop()
#print(stringlist)
#print(pathlist)
#print(occurencelist)
print(occurencelist)
print(stringlist)