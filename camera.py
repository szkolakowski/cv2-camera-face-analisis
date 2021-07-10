import cv2
import numpy as np
from functions import main as f
import tensorflow as tf
from tensorflow import keras

class face_frame:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

# face recognition
found = False
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# camera init
cam = cv2.VideoCapture(0)

# analisis values
gender = ''
age = ''
ethnicity = ''

# every camera frame
while True:
	face = None
	ret, frame = cam.read()
	# find faces
	frame = cv2.resize(frame, (0,0), fx=1.2, fy=1.2)
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
	for (x, y, width, height) in faces:
		face = face_frame(x, y, width, height)
	frame, face = f.edit_frame(frame, face)	

	# analyse face if one exists
	if face is not None and found is False:
		gender = f.check_gender(frame, face)
		age = f.check_age(frame, face)
		ethnicity = f.check_ethnicity(frame, face)
		found = True
	elif face is None and found:
		found = False

	# write analysed face parameters
	frame = f.write_frame(frame, found, gender, age, ethnicity)

	# show camera footage
	cv2.imshow('Face detection', frame)
	# binding quit key
	if cv2.waitKey(30) == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()