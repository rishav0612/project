import cv2
from Human_Detection import Detector

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Loop through frames from webcam
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret:
        # Write the frame to output file
        out.write(frame)
        frame = Detector(frame)
    
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
        # Press 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when done
cap.release()
out.release()

cv2.destroyAllWindows()   