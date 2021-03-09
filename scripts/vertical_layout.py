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
        
    root = tk.Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
        
    
    def __init__(self):
        super().__init__()

        self.initUI()


    def end_fullscreen(self, event=None):
        global root
        root.state = False
        root.attributes("-fullscreen", False)
        print("escape")
        return "break"
    
    def create_item(self, h_frame, image, name, coll):
        item = tk.Frame(h_frame)
        img = Image.open(image)
        img = img.resize((100,100),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label1 = Label(item, text=name, image=img)
        label1.image = img
        label1.pack()

        label = Label(item, text=name)
        label.pack()
        
        item.grid(row=0,column=coll)
        
        
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
        h_frame = tk.Frame(frame)
        
        
        #self.create_item(h_frame, "../db/Hesham_Maged.jpg", "Hisham Maged", 0)
        #self.create_item(h_frame, "../db/Shiko.jpg", "Shiko", 1)
        
        h_frame.pack(fill=tk.X)
        #closeButton = Button(frame, text="Close")
        #closeButton.pack(side=RIGHT, padx=5, pady=5)
        #okButton = Button(frame, text="OK")
        #okButton.pack(side=RIGHT)
        
        
