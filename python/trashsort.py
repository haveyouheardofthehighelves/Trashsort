import cv2
import tensorflow
from cvzone.ClassificationModule import Classifier
import serial
import time

# 0 as trash bin position, 1 as recycle bin position
current_pos = 0


def writetoarduino(writeall):
    arr = bytes(writeall, 'utf-8')
    ser.write(arr)


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
    if current_pos == 0:
        set_servo_position(1)
    current_pos = 1


def write_LCD(str1, str2):
    writetoarduino(f'{str1}*')
    writetoarduino(f'{str2}#')


ser = serial.Serial("COM4", 9600, timeout=0)
cap = cv2.VideoCapture(0)
classifier = Classifier('converted_keras/keras_model.h5', 'converted_keras/labels.txt')
initial_position()
class_names = {}
with open('converted_keras/labels.txt', 'r') as file:
    for line in file:
        index, name = line.strip().split(' ')
        class_names[int(index)] = name

while True:
    _, img = cap.read()
    prediction, index = classifier.getPrediction(img)
    if index in (0, 1, 2):
        write_LCD(class_names[index], 't')
        move_to_trash()
    if index in (3, 4):
        write_LCD(class_names[index], 'r')
        move_to_recycle()
    print(ser.readline())
    cv2.imshow("Hello", img)
    cv2.waitKey(1)
