import cv2
import tensorflow
from cvzone.ClassificationModule import Classifier
import serial

# 0 as trash bin position, 1 as recycle bin position
current_pos = 0
current_dir = 'forward'


def writetoarduino(writeall):
    arr = bytes(writeall, 'utf-8')
    ser.write(arr)


def move_to_trash():
    global current_pos
    global current_dir
    if current_pos == 180:
        writetoarduino('!')
    if current_dir == 'backward':
    current_pos = 0
    current_dir = 'forward'


def move_to_recycle():
    global current_pos
    global current_dir
    if current_pos == 0:
        writetoarduino('!')
    if current_dir == 'backward':

    writetoarduino('%')
    current_pos = 180
    current_dir = 'forward'


def move_back():
    global current_dir
    if current_dir == 'forward':
        writetoarduino('%')
    current_dir = 'backward'


ser = serial.Serial("COM3", 9600, timeout=1)
cap = cv2.VideoCapture(0)
classifier = Classifier('converted_keras/keras_model.h5', 'converted_keras/labels.txt')

while True:
    if '.' in str(ser.readline()):
        _, img = cap.read()
        prediction, index = classifier.getPrediction(img)

        if index in (0, 1, 2):
            move_to_trash()
        if index in (3, 4):
            move_to_recycle()

        cv2.imshow("Image", img)
        cv2.waitKey(1)

