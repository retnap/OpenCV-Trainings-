import cv2
import numpy as np 

image_path = "C:\\Users\\Selman\\Desktop\\Tasarim-1\\starwars.jpg"
template_path = "C:\\Users\\Selman\\Desktop\\Tasarim-1\\starwars2.jpg"

img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
w,h = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

location = np.where(result >= 0.7)

for point in zip(*location[::-1]): #gets the height and width
    cv2.rectangle(img, point, (point[0] + w,point[1] +h), (0,255,0), 3)



cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
