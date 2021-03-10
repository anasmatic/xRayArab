# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:23:34 2021

@author: Omnia
"""
import tkinter as tk
#from tkinter import RIGHT, BOTH, RAISED, X
from tkinter.ttk import Frame, Button, Label
from PIL import Image, ImageTk

class HorizontalImageBar():
    
    items = {}
    root = tk.Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    h_frame = None
    coll = 0
    
    def __init__(self):
        super().__init__()

        self.initUI()


    def end_fullscreen(self, event=None):
        global root
        root.state = False
        root.attributes("-fullscreen", False)
        print("escape")
        return "break"
    
    def update_items(self, found_actors):
        #actor_ids = [found_actors['id'] for x in found_actors]
        #print(actor_ids)
        #for _id in actor_ids:
        #    if not _id in self.items.keys():
        #        items[]
                
        for actor in found_actors:
            if(not actor['id'] in self.items):
                self.create_item(actor['id'],"../db/"+actor['photos'][0],actor['name']['ar'])
        
    def create_item(self, _id, image, name):
        
        item = tk.Frame(self.h_frame)
        
        img = Image.open(image)
        img = img.resize((100,100),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img, master=item)
        
        label1 = Label(item, text=name, image=img)
        label1.image = img
        label1.pack()

        label = Label(item, text=name)
        label.pack()
        
        item.grid(row=0,column=self.coll)
        self.coll+=1
        self.items[_id] = item
        
        
    def initUI(self):
        
        global root
        global screenwidth 
        global screenheight 
        
        self.root.withdraw()
        
        top = tk.Toplevel(self.root)
        top.protocol("WM_DELETE_WINDOW", self.root.destroy)
        top.title('XRay Arab')
        top.geometry("{0}x{1}+0+0".format(self.screenwidth, self.screenheight))

        top.state = False
        top.attributes("-fullscreen", True)
        top.wm_attributes("-transparentcolor", top["bg"])
                
        
        """
        #root.bind("<Escape>", end_fullscreen)
        """
        frame = tk.Frame(top, relief= tk.RAISED, borderwidth=1)
        frame.pack(fill=tk.BOTH, expand=True)

        #root.pack(fill=tk.BOTH, expand=True)
        self.h_frame = tk.Frame(frame)
        self.h_frame.pack(fill=tk.X)
        
        """
        self.create_item("","../db/Hesham_Maged.jpg", "Hesham Maged")
        self.coll+=1
        self.create_item("","../db/Shiko.jpg", "Shiko")
        """
        #closeButton = Button(frame, text="Close")
        #closeButton.pack(side=RIGHT, padx=5, pady=5)
        #okButton = Button(frame, text="OK")
        #okButton.pack(side=RIGHT)
        
        
