import cv2
import mediapipe as mp
import time
import numpy as np
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)

pTime = 0
x1=y1=x2=y2=0
mphands = mp.solutions.hands
hands = mphands.Hands(min_detection_confidence=.7,max_num_hands=2)
mpDrow = mp.solutions.drawing_utils
while True:
    success, img = cap.read()
    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    reasults = hands.process(imgRgb)
    openedF= 0
 
    if reasults.multi_hand_landmarks:
        for onehand in reasults.multi_hand_landmarks:
            listnode=[]
            
            for idno, lm in enumerate(onehand.landmark):               
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                listnode.append([idno,cx,cy])


            caredfinger=[4,8,12,16,20]
            
            for i in range(0,5):
                if(caredfinger[i]!=4):
                
                    if(listnode[caredfinger[i]][2]<listnode[caredfinger[i]-2][2]):
                        openedF=openedF+1
                else:
                    if(listnode[4][1]>listnode[3][1]):
                        openedF=openedF+1

            mpDrow.draw_landmarks(img, onehand, mphands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    print(fps)

    cv2.putText(img,"Finger Count"+str(int(openedF)), (10, 70),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 255, 0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)


   
