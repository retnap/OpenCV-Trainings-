import cv2
import numpy as np 

path = "C:\\Users\\Selman\\Desktop\\Tasarim-1\\aircraft.jpg"
path1 = "c:\\Users\\Selman\\Desktop\\Tasarim-1\\aircraft1.jpg"

img1 = cv2.imread(path)
img1 = cv2.resize(img1, (640,550))

img2 = cv2.imread(path1)
img2 = cv2.resize(img2, (640,550))

img3 = cv2.medianBlur(img1, 7) #Median blur applied to img1

if img1.shape == img2.shape:
    print("Same Size")
else:
    print("Not Same")

# diff = difference
diff = cv2.subtract(img1, img3) # compares two images and reveals differences
b,g,r = cv2.split(diff) 

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0: #Looks for non-0 values ​​in b,g,r 
   print("Completely equal") 
else:
    print("Not completely equal")




cv2.imshow("Difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()