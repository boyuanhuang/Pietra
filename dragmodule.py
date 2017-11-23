# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 10:11:02 2017

@author: bo
"""

from tkinter import *
   
 
def recordPos(event):
    return event.x, event.y
     
def onLeftDrag(event):
    print( 'Got left mouse button drag:',
    showPosEvent(event))
def drag(event):
    global oval, canvas
    newx, newy = recordPos(event)
    widget_todrag = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    canvas.coords(widget_todrag, newx, newy)
    tkroot.after(50, drag(event))
    
tkroot = Tk()
canvas = Canvas(tkroot, width = 400, height = 300, bg = 'green')
canvas.pack()
x= 100
y=100
widget = Label(canvas, text='Hello bind world', width = 5, height =5)
widget.config(bg='red', font=labelfont)            
#widget.config(height=5, width=5) 
canvas.create_window( 50,100, window = widget )
widget.bind('<B1-Motion>', drag)   
  
                               
tkroot.title('Click Me')
tkroot.mainloop()

