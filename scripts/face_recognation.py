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
import cv2
from vertical_layout import HorizontalImageBar

#fullscreen ui

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
    threading.Timer(2, scan).start()
    global bar
    img = ImageGrab.grab(bbox=(0, 0, bar.screenwidth, bar.screenheight)) #x, y, w, h
    
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    #cv2.imshow("frame", frame)
    
    allunkownfaces = face_recognition.face_encodings(frame)
    print("found : ",len(allunkownfaces), " faces")
    print("compairing against : ",len(first_image_list), " faces")
    foundObjs = []
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
            foundObjs.append(actorObj)
            
    bar.update_items(foundObjs)
"""    
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
    
if results2[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")
"""


db = []
first_image_list = []

loaddb()
print("db ready")
bar = HorizontalImageBar()
print("Ui ready")
scan()
#threading.Timer(5, scan).start()
bar.root.mainloop()

