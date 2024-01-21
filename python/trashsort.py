import cv2
import tensorflow
from cvzone.ClassificationModule import Classifier
import serial
# 0 as trash bin position, 1 as recycle bin position
current_pos = 0


def initial_position():
    global current_pos
    current_pos = 0


def set_servo_position(angle):
    ser.write(angle)


def move_to_trash():
    global current_pos
    if current_pos == 1:
        set_servo_position(0)
    current_pos = 0


def move_to_recycle():
    global current_pos
    if current_pos ==0:
        set_servo_position(1)
    current_pos = 1


ser = serial.Serial("COM3", 9600, timeout=1)
cap = cv2.VideoCapture(0)
classifier = Classifier('converted_keras/keras_model.h5', 'converted_keras/labels.txt')
initial_position()
while True:
    _, img = cap.read()
    prediction, index = classifier.getPrediction(img)
    if index in (0, 1, 2):
        move_to_trash()
    if index in(3, 4):
        move_to_recycle()

    cv2.imshow("Image",img)
    cv2.waitKey(1)


