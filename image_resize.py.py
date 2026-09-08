import cv2
import imutils

img = cv2.imread(r"C:\Users\R.Yuvashree\OneDrive\Dokumen\python\sample2.png")

if img is None:
    print("Error: Image not found!")
else:
    resizedImg = imutils.resize(img, width=500)
    cv2.imwrite("resizedImage.jpg", resizedImg)
    print("Image resized successfully!")
