import cv2

img = cv2.imread("C:\\Users\\Selman\\Desktop\\Tasarim-1\\starwars.jpg")

blury_img = cv2.medianBlur(img, 7)

laplacian = cv2.Laplacian(blury_img, cv2.CV_64F).var()

if laplacian < 500:
    print("Blury image")

cv2.imshow("img", img)
cv2.imshow("blury", blury_img)

cv2.waitKey(0)
cv2.destroyAllWindows()