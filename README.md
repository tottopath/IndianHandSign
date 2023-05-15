# IndianHandSign
Hand Sign Detection for Indian Sign Language (ISL) 

This project is made by following the Video "Easy Hand Sign Detection | American Sign Language ASL | Computer Vision" by the YouTube Channel "Murtaza's Workshop - Robotics and AI". The original project was made for English Sign Language. In English Sign Language, only one hand is utilized.

This project is made for Indian Sign Language, which utilizing both the hands. The project was built on top of the above-mentioned tutorial with modifications and add-ons wherever required. This is just a demo project thus it only contains the letters "E", "H", "L" and "O" but can be extended to all the alphabets.

Explanation:
1. twohandDC.py: It is responsible for collecting images of one’s hands, single hand or two hands depending on the dataset, using OpenCV and the hand tracking module. Once the code is executed, it starts the desktop camera that detects hands and crops and resizes the hand regions of interest. It does this by assigning 21 points to the palm of each hand. Additionally, the script saves the combined hand image to a specified folder (specified in line 13 of the code) with a timestamp as the image filename.
2. Data: The data collected by using twohandDC.py will then be uploaded to Google Teachable Machine under Image Project (https://teachablemachine.withgoogle.com/train/image). The labels are added and images are uploaded. The data is trained and exported as Tensorflow keras. The keras files (keras_model.h5 and labels.txt) are then placed in the Model folder.
3. v11.py: It imports the necessary libraries, including OpenCV (cv2), a hand tracking module (HandDetector), and a classification module (Classifier). It initializes the camera capture and sets up the hand detection and classification modules. The script uses a pre-trained model to classify the hand gesture. The predicted gesture is displayed on the screen as well as in the terminal, and the gestures is appended to a file (Speak.txt) after every 5 seconds and ‘a’ can be used to add space between letters. Initially, the letters are in English, following the Indian Sign Language Gestures, but after the appending is completed, using the EngtoHindi library, Speak.txt is translated to Hindi (words and alphabets).


How to run:
•	Open the folder in Visual Studio
•	Run the v11.py file
•	Any signs recognized will be added to Speak.txt

How to add or make your own data:
•	Open twohandDC.py
•	In line 13. folder = "Data/Thanks" change it to whatever word you want, Data/xyz
•	Go to the Data folder and create the new folder xyz
Creating new model:
•	Data contains folders for each letter or gesture. Example: Hello, ILY, No, Thanks and Yes
•	Model contains the model developed using https://teachablemachine.withgoogle.com/train/image
![image](https://github.com/tottopath/IndianHandSign/assets/57607554/345c3769-65f5-44d1-a8b6-4567e9a8eb9c)
![image](https://github.com/tottopath/IndianHandSign/assets/57607554/61a6049b-1497-44aa-9e75-836ba9d1e5d6)
o	Once created, Download the Keras model 
![image](https://github.com/tottopath/IndianHandSign/assets/57607554/4bb78f8f-939b-4e62-b0b7-ea3efb8272a0)
o	Copy paste the models in Model folder
