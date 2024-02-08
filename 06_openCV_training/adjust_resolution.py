import cv2 

windowName = "Live Video"
cv2.namedWindow(windowName)

cap = cv2.VideoCapture(0)

print("Widht: " + str(cap.get(3))) # width(3) length(4) of image in cap
print("Height: " + str(cap.get(4)))

cap.set(3, 1280)
cap.set(4, 720)

print("Widht:* " + str(cap.get(3))) 
print("Height:* " + str(cap.get(4)))

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow(windowName,frame)

    if cv2.waitKey(1) == 27 & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
