# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:24:46 2021

@author: Omnia
"""
import face_recognition

picture_of_me = face_recognition.load_image_file("../data/Known/Hesham Maged.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("../data/Unknown/h3.jpg")
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