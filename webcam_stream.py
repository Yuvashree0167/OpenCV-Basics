import cv2
# Start the webcam
vs = cv2.VideoCapture(0)
while True:
    # Read a frame from the webcam
    ret, img = vs.read()
    # Check if the frame was captured successfully
    if not ret:
        print("Failed to access the webcam.")
        break
    # Display the webcam video
    cv2.imshow("VideoStream", img)
    # Press 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
# Release the webcam
vs.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
