import cv2
img=cv2.imread("mountain.jpg")
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey.png",gry)
