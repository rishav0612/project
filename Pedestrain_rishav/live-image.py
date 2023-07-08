import cv2
import imutils
from Human_Detection import Detector
cap = cv2.VideoCapture(0)

# Capture image from webcam
ret, frame = cap.read()

# Release webcam capture object
cap.release()
# Assign captured image to img variable
img = frame
img = imutils.resize(img, width=700)
img = Detector(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
