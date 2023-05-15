# IndianHandSign
Hand Sign Detection for Indian Sign Language (ISL) 

This project is made by following the Video "Easy Hand Sign Detection | American Sign Language ASL | Computer Vision" by the YouTube Channel "Murtaza's Workshop - Robotics and AI". The original project was made for English Sign Language. In English Sign Language, only one hand is utilized.

This project is made for Indian Sign Language, which utilizing both the hands. The project was built on top of the above-mentioned tutorial with modifications and add-ons wherever required. 

Explanation:
1. twohandDC.py: It is responsible for collecting images of one’s hands, single hand or two hands depending on the dataset, using OpenCV and the hand tracking module. Once the code is executed, it starts the desktop camera that detects hands and crops and resizes the hand regions of interest. It does this by assigning 21 points to the palm of each hand. Additionally, the script saves the combined hand image to a specified folder (specified in line 13 of the code) with a timestamp as the image filename.
2. Data: The data collected by using twohandDC.py will then be uploaded to Google Teachable Machine under Image Project (https://teachablemachine.withgoogle.com/train/image). The labels are added and images are uploaded. The data is trained and exported as Tensorflow keras. The keras files (keras_model.h5 and labels.txt) are then placed in the Model folder.
3. v11.py: It imports the necessary libraries, including OpenCV (cv2), a hand tracking module (HandDetector), and a classification module (Classifier). It initializes the camera capture and sets up the hand detection and classification modules. The script uses a pre-trained model to classify the hand gesture. The predicted gesture is displayed on the screen as well as in the terminal, and the gestures is appended to a file (Speak.txt) after every 5 seconds and ‘a’ can be used to add space between letters. Initially, the letters are in English, following the Indian Sign Language Gestures, but after the appending is completed, using the EngtoHindi library, Speak.txt is translated to Hindi (words and alphabets).

