import cv2
import tensorflow
from cvzone.ClassificationModule import Classifier
import serial
import time
import keyboard


# 0 as trash bin position, 1 as recycle bin position
current_pos = 0
current_dir = 'forward'


def writetoarduino(writeall):
    arr = bytes(writeall, 'utf-8')
    ser.write(arr)

def move_to_trash():
    writetoarduino('!')

def move_to_recycle():
    writetoarduino('%')

def move_back():
    writetoarduino('(')


ser = serial.Serial("COM3", 9600, timeout=1)
cap = cv2.VideoCapture(0)
classifier = Classifier('converted_keras/keras_model.h5', 'converted_keras/labels.txt')
while True:
    _, img = cap.read()
    prediction, index = classifier.getPrediction(img)
    if keyboard.is_pressed(' '):
        print("hello")
        if index in (0, 1, 2):
            move_to_trash()
        if index in (3, 4):
            move_to_recycle()
    cv2.imshow("Image", img)
    cv2.waitKey(1)