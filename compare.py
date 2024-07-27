#pip install opencv-python deepface
# you will face problem so u need to install the following
# https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
# put it into C:\Users\urpcName\.deepface\weights\vgg_face_weights.h5
# then run the code

import threading

import cv2
from deepface import DeepFace
# capture first camera in case u have multiple w kda
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#window size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

reference_image = cv2.imread('img1.jpg')

def check_face(frame):
    global face_match
    try: 
        if DeepFace.verify(frame, reference_image.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False
        
    

while True:
    ret, frame = cap.read()
    #if there is a return do smth
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target = check_face , args=(frame.copy() , )).start()
            except ValueError:
                pass
        counter += 1
        cv2.putText(frame, "Q to Close", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        if face_match:                      # size    font                      scale  color  thickness
            cv2.putText(frame, "Face Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)    
        
        cv2.imshow("video", frame)
        
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()