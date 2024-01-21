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


def initial_position():
    global current_pos
    current_pos = 0
    global current_dir
    current_dir = 'forward'


def set_servo_position(angle):
    ser.write(angle)


def set_motor_direction(dir):
    ser.write(dir)


def move_to_trash():
    global current_pos
    global current_dir
    if current_dir == 'backward':
        set_motor_direction(1) # 1 = forward
    if current_pos == 1:
        set_servo_position(0)
    current_pos = 0
    current_dir = 'forward'


def move_to_recycle():
    global current_pos
    global current_dir
    if current_dir == 'backward':
        set_motor_direction(1) # 1 = forward
    if current_pos ==0:
        set_servo_position(1)
    current_pos = 1
    current_dir = 'forward'


def move_back():
    global current_dir
    if current_dir == 'forward':
        set_motor_direction('backward')
    current_dir = 'backward'




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
    if index in(5):
        move_back()

    cv2.imshow("Image",img)
    cv2.waitKey(1)


