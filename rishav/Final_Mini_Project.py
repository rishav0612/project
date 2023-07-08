
import random
from keras.models import load_model
import cv2
import numpy as np
from keras.utils import img_to_array
import webbrowser

fase01 = cv2.CascadeClassifier('./abc.xml')
classifier = load_model('./Emotion_Detection.h5')

class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', ]

# for capturing video
cap = cv2.VideoCapture(0)

while True:

    # Grab a single frame of video
    ret, frame = cap.read()
    labels = []

    # convert captured image into gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detectMultiScale == detect face from image, returns the coordinates of faces to variable face
    faces = fase01.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:          # (x,y,w,h are co-ordinates of faces)

        # rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            # converting image into an array
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi) #inside the array the images are stored as values
            roi = np.expand_dims(roi, axis=0) # add extra dimensions to roi and axis will be 0 , h , w or new parameter will be always 0

           

            preds = classifier.predict(roi)[0]
            
            label = class_labels[preds.argmax()]  #select highest probability and insert inside label function
            
            label_position = (x, y) # now it will tell the position

            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) # it tell the emotion in the rectangle box

        else:
            cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        

    cv2.imshow('Emotion Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if labels == "Happy":
            url = 'https://www.youtube.com/watch?v=mH_LFkWxpI0'
            webbrowser.open_new(url)
            break
        elif labels == "Sad":
            url = 'https://www.youtube.com/watch?v=6z1U-kJ3xJE'
            webbrowser.open_new(url)
            break
        elif labels == "Neutral":
            url = 'https://www.youtube.com/watch?v=6z1U-kJ3xJE'
            webbrowser.open_new(url)
            break
        elif labels == "Angry":
            url = 'https://www.youtube.com/watch?v=6z1U-kJ3xJE'
            webbrowser.open_new(url)
            break
        else:
            lines = open(r"C:\Users\RISHAV KUMAR\Desktop\rishav\url.txt").read().splitlines()
            url =random.choice(lines)
            webbrowser.open_new(url)
            break


cap.release()
cv2.destroyAllWindows()
