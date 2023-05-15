import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

offset = 20
imgSize = 300

folder = "Data/O"
counter = 0

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if hands:
        imgWhite = np.ones((imgSize, imgSize * 2, 3), np.uint8) * 255
        handImgs = []
        for handIndex, hand in enumerate(hands):
            x, y, w, h = hand['bbox']

            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

            if imgCrop.shape[0] == 0 or imgCrop.shape[1] == 0:
                continue

            imgCropShape = imgCrop.shape

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[0:imgSize, handIndex * imgSize + wGap:handIndex * imgSize + wCal + wGap] = imgResize

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, handIndex * imgSize:handIndex * imgSize + imgSize] = imgResize

            handImgs.append(imgResize)

        if len(handImgs) == 2:
            # Resize and concatenate both hand images horizontally into a single image
            new_size = (500, 500)
            resized_img = imgCombined = cv2.resize(img, new_size)

            cv2.imshow("ImageWhite", imgCombined)

            counter += 1
            cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgCombined)
            print(counter)
            
        elif len(handImgs) == 1:
            # Resize and concatenate both hand images horizontally into a single image
            new_size = (500, 500)
            resized_img = imgCombined = cv2.resize(img, new_size)

            cv2.imshow("ImageWhite", imgCombined)

            counter += 1
            cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgCombined)
            print(counter)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
