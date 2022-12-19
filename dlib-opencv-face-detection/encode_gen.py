import cv2
import face_recognition
import pickle
import os

pics = ".\\faces\\"
picslist = os.listdir(pics)
imglist = []
pplname = []

for path in picslist:
    imglist.append(cv2.imread(os.path.join(pics,path)))
    pplname.append(os.path.splitext(path)[0])
print(pplname)

def findEncodings(imglist):
    encodelist = []
    for img in imglist:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
        return encodelist

knownFaces = findEncodings(imglist)
print("encoding complete")