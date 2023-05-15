import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time
 
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
 
offset = 20
imgSize = 300
 
wait_time = 5  # in seconds
start_time = time.time()

folder = "Data/E"
counter = 0

labels = ["E", "H", "L", "O"] #, "E", "F", "G", "H", "J", "W", "X"]
# Keep track of the last 5 labels output
last_labels = []
 
while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    if hands:
        hand_boxes = [hand['bbox'] for hand in hands]
        left = min([box[0] for box in hand_boxes])
        top = min([box[1] for box in hand_boxes])
        right = max([box[0]+box[2] for box in hand_boxes])
        bottom = max([box[1]+box[3] for box in hand_boxes])
 
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[top - offset:bottom + offset, left - offset:right + offset]
 
        if imgCrop.shape[0] == 0 or imgCrop.shape[1] == 0:
            continue
        
        imgCropShape = imgCrop.shape
 
        aspectRatio = (bottom-top) / (right-left)
 
        if aspectRatio > 1:
            k = imgSize / (bottom-top)
            wCal = math.ceil(k * (right-left))
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            #print(prediction, index)
 
        else:
            k = imgSize / (right-left)
            hCal = math.ceil(k * (bottom-top))
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
 
        cv2.rectangle(imgOutput, (left - offset, top - offset-50),
                      (left - offset+90, top - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (left, top -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        #print(labels[index])
        cv2.rectangle(imgOutput, (left-offset, top-offset),
                      (right+offset, bottom+offset), (255, 0, 255), 4)

        # Add the current label to the list of the last 5 labels
        last_labels.append(labels[index])
        
        # If the list has more than 5 labels, remove the oldest label
        if len(last_labels) > 5:
            last_labels.pop(0)

        # Check if 'S' key is pressed and write the last detected label to Speak.txt
        if time.time() - start_time >= wait_time:
            with open("Speak.txt", "a") as f:
                f.write(last_labels[-1])
            last_labels = []
            print("Alphabet added " + labels[index])
            start_time = time.time()
            
        if cv2.waitKey(1) & 0xFF == ord('a'):
            with open("Speak.txt", "a") as f:
                f.write(' ')
            last_labels = []
            print("Space added")
        
    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1)

from englisttohindi.englisttohindi import EngtoHindi

with open('Speak.txt', 'r') as file:
    contents = file.read()
    print(contents)
    
trans = EngtoHindi(contents)
new = trans.convert

with open('Speak.txt', 'a', encoding="utf-8") as file:
    file.write('\n')
    print(new)
    file.write(new)