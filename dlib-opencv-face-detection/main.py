import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
imgbg = cv2.imread("bg.jpeg")

while True:
    success, img = cap.read()
    imgbg[100:100+480,180:180+640] = img
    # cv2.imshow("background",imgbg)
    cv2.imshow("image test", imgbg)
    cv2.waitKey(1)