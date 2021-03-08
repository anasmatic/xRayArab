# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:36:51 2021

@author: Omnia
"""

import cv2
import numpy as np
import dlib
from mss import mss
from PIL import Image

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
prdetector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
box = {'top': 0, 'left': 0, 'width': 800, 'height': 600}

sct = mss()

while True:
    frame = sct.grab(box)
    frame = np.array(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        cv2.rectangle(frame, (face.left(),face.top()),(face.right(),face.bottom()),(0,255,0),3)
    
    #cv2.imshow('screen', np.array(sct_img))

    #_, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
"""   
while True:
    cv2.rectangle(frame, (box.left,box.top),(box.width,face.height),(255,255,255),3)
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    for face in faces:
        cv2.rectangle(frame, (face.left(),face.top()),(face.right(),face.bottom()),(0,255,0),3)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break
"""