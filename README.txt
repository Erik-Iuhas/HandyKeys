Erik Iuhas 101076512 
HandyKeys Project Setup Requirements 
=====================================

Required Files: (Listing all the files provided in the project)
Inputs (Directory): This folder contains 16 images from the validation dataset to test the TinyHand Network in Google Colab
    - Outputs (Directory): Contains 8 examples to check if the network outputs the same results.
HandKeysApp (Directory):
    - handy_keys.py: Contains the kivy App which you could run to test the app.
    - TinyHand.py: Contains the Tensorflow model TinyHand which is utilized by handy_keys.py as a class.
    - tiny_hand_final.h5: Contains the weights for TinyHand model, you need this weight to test the model on Google Colab
HandyKeys_DEMO.mp4 (File): Contains a video demo of the app if you cannot install the required libraries to run Tensorflow and Kivy on your local computer.
HandyClassy.ipynb (File): Contains the notebook which you can run to test the training and testing of the model. RUN IN GOOGLE DRIVE. I did not make it to be tested locally.
HandyClassy.pdf (File): Contains the pdf version of my Notebook for easy access and review.
COMP4102_COURSE_PROJ_ERIK_IUHAS_REPORT.pdf (File): Contains the report for the course project.
Google Drive Link of Personally Made Dataset: https://drive.google.com/drive/folders/1Tj5QfndOj4xlEvG-CxJihrJdXRqfIokj?usp=sharing
    - Dataset folder contains both my training and validation set, if more images are required to test my model more images can be obtained throug the Google Drive


======= Instructions for Testing Model in the Notebook ============

For this project if you are looking to test the model trained in my Notebook,
I have provided the tiny_hand_final.h5 within the HandyKeysApp directory.

To test the model in the notebook follow these steps.
1. Go to Google Colab, select File, upload Notebook
3. Upload the tiny_hand_final.h5 file to the Google Drive as specified in "Load the Weight File (REQUIRED)"
3. Run the cell headings which have (REQUIRED) beside them.
    - Import Required Libraries (REQUIRED)
    - Build TinyHand Architecture (REQUIRED)
    - Load the Weight File (REQUIRED) 
    - Test TinyHand (REQUIRED): This section lets you upload and test the files provided in Inputs directory.
4. Run the cell Test TinyHand (REQUIRED) Cell as much as you need to test the files individually.
5 Compare the results to the Outputs directory which is in the Inputs directory.

======= Instructions for testing the training in the Notebook ==============

In the event you want to run my code and train a new neural network you could do so by downloading the Dataset provided in the
HandyKeys Google Drive link.

Steps to test the training in the notebook.
1. Go to Google Colab, select File, upload Notebook
2. Afterwards you would need to make a Directory/Folder in your own home Google Drive called "HandyKeys" and place the downloaded Dataset folder inside of it.
3. After doing so you are then able to use Google Colab to run Mount for Training and give Google Colab permission to access the Dataset folder.
    - Assuming you have set up the folders properly in your own Google Drive there should be no problems when mounting it to your Google Colab Session.
4. Run every cell except the two listed ones below. Make sure to AVOID running these cells, doing so would overwrite your trained models.
    a. Import TinyHand Weights (REQUIRED)
    b. Load the Weight File (REQUIRED)


======= Instructions for running the HandyKeys App ============

To run the HandyKeys app ensure that you have the following libraries installed in an annoconda environment.
1. Kivy: The following install command is for the Kivy version which is used in the HandyKeysApp.
    conda install -c conda-forge kivy
2. Tensorflow: The following install command is for the Tensorflow version which is used in the TinyHand.
    conda install tensorflow
3. OpenCV: The following install command is for the OpenCV version which is used in the TinyHand.
    conda install opencv

Following this you need to run the handy_keys.py file which is located in the HandyKeysApp directory.
Running: python handy_keys.py

If you do not have a webcam or if your webcam is at a different port you will be required to fiddle around with cv.VideoCapture(0) at line 31
This is because each webcam has a different port number.

After running the application you will see a window appear which will show the webcam feed along with the key label.

As I mentioned in the report the network is unlikely to preform well on other peopels hands, so I have provided a video demo of the app to demonstrate how the app works.
