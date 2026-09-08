import cv2

img = cv2.imread("sample2.png.png")

if img is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully!")

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    cv2.imwrite("GaussianBlur.jpg", gaussianImg)

    cv2.imshow("Original", img)
    cv2.imshow("Gaussian Blur", gaussianImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
