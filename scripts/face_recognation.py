# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:24:46 2021

@author: Omnia
"""
from PIL import ImageGrab
import face_recognition
import pandas as pd
import numpy as np
import threading
import tkinter
import json
import mss
import cv2

#fullscreen ui
root = tkinter.Tk()

def end_fullscreen(self, event=None):
        global root
        root.state = False
        root.attributes("-fullscreen", False)
        print("escape")
        return "break"
    
root.title('XRay Arab')
#root.geometry("1000x1000")
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(
            screenwidth, screenheight))
root.state = False
root.attributes("-fullscreen", True)
root.wm_attributes("-transparentcolor", root["bg"])
root.bind("<Escape>", end_fullscreen)
#end

box = {'top': 0, 'left': 0, 'width': screenwidth, 'height': screenheight}

db = []
first_image_list = []
def loaddb():
    global db
    db = pd.read_json(r"../db/actors.json");
    for actor in db['actor']:
        for photo in actor['photos']:
            picture = face_recognition.load_image_file("../db/"+photo)
            face_encoding = face_recognition.face_encodings(picture)[0]
            first_image_list.append(face_encoding);
            break

#face detection logic
def scan():
    print("scan")
    #threading.Timer(5, scan).start()

    img = ImageGrab.grab(bbox=(0, 0, screenwidth, screenheight)) #x, y, w, h
    #take screen shot
    #with mss.mss() as sct:
    #    frame = np.array(sct.grab(box))
    #frame = np.array(frame)
    
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    #rgb_frame = frame[:, :, ::-1]
    
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("frame", frame)
    
    allunkownfaces = face_recognition.face_encodings(frame)
    print("found : ",len(allunkownfaces), " faces")
    print("compairing against : ",len(first_image_list), " faces")
    
    for unknownface in allunkownfaces:
        results = face_recognition.compare_faces(first_image_list, unknownface)
        print("results: ",results)
        index = np.nonzero(results)
        print("found at :",index)
        if(len(index[0]) > 0):
            index = index[0][0]
            print("get result at :",index)
            actorObj = db['actor'][index]
            print("====================================")
            print("name :", actorObj['name']['ar'])
            print("====================================")
    
picture_of_me = face_recognition.load_image_file("../Known/Hesham Maged.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("../Unknown/h3.jpg")
encoding = face_recognition.face_encodings(unknown_picture)
print(len(encoding))
unknown_face_encoding1 = face_recognition.face_encodings(unknown_picture)[0]
#unknown_face_encoding2 = face_recognition.face_encodings(unknown_picture)[1]
# Now we can see the two face encodings are of the same person with `compare_faces`!

results1 = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding1)
#results2 = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding2)

if results1[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")
"""    
if results2[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")
"""
loaddb()
#scan()
threading.Timer(5, scan).start()
root.mainloop()

