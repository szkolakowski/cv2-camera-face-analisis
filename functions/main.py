import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image

def edit_frame(frame, face):
	color = (255, 255, 0)
	frame = cv2.rectangle(frame, (0, 0), (768, 30), (20, 20, 20), -1)
	frame = cv2.rectangle(frame, (0, 545), (768, 680), (20, 20, 20), -1)
	if face is not None:
		cv2.rectangle(frame, (face.x, face.y), (face.x + face.width, face.y + face.height), color, 1)
		face = frame[face.y:face.y+face.height, face.x:face.x+face.width]
		face = cv2.resize(face, (160,160))
	return frame, face

def face_reshape(face):
	face = image.img_to_array(face)
	face = np.expand_dims(face, axis=0)
	face /= 255
	return face

# 98% accuracy
def check_gender(frame, face):
	genders = ['Female', 'Male']
	face = face_reshape(face)
	model = keras.models.load_model('models/gender.h5')
	prediction = model.predict(face)
	prediction = list(prediction[0])	
	gender = prediction.index(max(prediction))
	answer = genders[gender] + ' ' + str(round(prediction[gender]*100)) + '%'
	return answer

# 70-% accuracy
def check_age(frame, face):
	ages = ['1-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '41-45',
			'46-50', '51-55', '56-60', '61-65', '66-70', '71-75', '76-80', '81-85']
	face = face_reshape(face)
	model = keras.models.load_model('models/age.h5')
	prediction = model.predict(face)
	prediction = list(prediction[0])	
	age = prediction.index(max(prediction))
	answer = ages[age] + ' ' + str(round(prediction[age]*100)) + '%'
	return answer

# 85-% accuracy
def check_ethnicity(frame, face):
	ethnicities = ['asian', 'black', 'indian', 'others', 'white']
	face = face_reshape(face)
	model = keras.models.load_model('models/ethnicity.h5')
	prediction = model.predict(face)
	prediction = list(prediction[0])	
	ethnicity = prediction.index(max(prediction))
	answer = ethnicities[ethnicity] + ' ' + str(round(prediction[ethnicity]*100)) + '%'
	return answer

def write_frame(frame, found, gender, age, ethnicity):
	color = (255, 255, 0)
	weight = 1
	font_size = 0.5
	font = cv2.FONT_HERSHEY_DUPLEX
	gender_place = (30,20)
	age_place = (345,20)
	ethnicity_place = (600,20)
	error_place = (345, 565)
	frame = cv2.putText(frame, gender, gender_place, font, font_size, color, weight, cv2.LINE_AA)
	frame = cv2.putText(frame, age, age_place, font, font_size, color, weight, cv2.LINE_AA)
	frame = cv2.putText(frame, ethnicity, ethnicity_place, font, font_size, color, weight, cv2.LINE_AA)
	if found is False:
		frame = cv2.putText(frame, 'Face not found', error_place, font, font_size, color, weight, cv2.LINE_AA)

	return frame