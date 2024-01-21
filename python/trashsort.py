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
    writetoarduino('-')


def move_back():
    writetoarduino('(')


def write_LCD(str1, str2):
    writetoarduino(f'{str1}*')
    writetoarduino(f'{str2}#')


ser = serial.Serial("COM3", 9600, timeout=1)
cap = cv2.VideoCapture(0)
classifier = Classifier('converted_keras/keras_model.h5', 'converted_keras/labels.txt')
class_names = {}
with open('converted_keras/labels.txt', 'r') as file:
    for line in file:
        index, name = line.strip().split(' ')
        class_names[int(index)] = name
while True:
    _, img = cap.read()
    prediction, index = classifier.getPrediction(img)
    print(prediction[index])
    if prediction[index] < .7:
        write_LCD('Unknown', 'Object')
    elif index in (2, 3, 4):
        write_LCD(class_names[index], f'Trash: {round(prediction[index] * 100, 2)}%')
    elif index in (1, 0):
        write_LCD(class_names[index], f'Recycle: {round(prediction[index] * 100, 2)}%')
    elif index == 5:
        write_LCD('no object', 'present')
    if keyboard.is_pressed(' '):
        if prediction[index] >= .7:
            if index in (2, 3, 4):
                move_to_trash()
            if index in (1, 0):
                move_to_recycle()
        else:
            move_back()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
