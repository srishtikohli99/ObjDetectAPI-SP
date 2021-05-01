from django.conf import settings
import cv2
import numpy as np 
import os 
import time
import tensorflow
import tensorflow.keras as keras
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import model_from_json,Sequential
from keras.applications import ResNet50
from keras.layers import Dense
import json
from keras import backend as K
import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True

model = Sequential()
model.add(ResNet50(include_top = False, pooling = 'max', input_shape = (197,197,3)))
model.add(Dense(512, activation = 'tanh'))
model.add(Dense(256, activation = 'tanh'))
model.add(Dense(128, activation= 'tanh'))
model.add(Dense(64, activation= 'tanh'))
model.add(Dense(3, activation = "softmax"))
print("hello5")
dir_path = os.path.dirname(os.path.realpath(__file__))
dir2 = os.path.join(dir_path, "model.h5")
model.load_weights(dir2)
print("hello6")


def objectDetect():
	K.reset_uids()
	tb._SYMBOLIC_SCOPE.value = True
	print("called")
	dir = os.path.join(settings.MEDIA_ROOT, "hello.jpeg")
	img = load_img(dir, target_size=(197,197))
	x = img_to_array(img)
	x = x.reshape(1,197,197,3).astype('float')
	ans = model.predict(x)
	print(ans)
	f=0
	for i in range(3):
		if ans[0][i] >= 0.8:
			f=1
			return i+1
	if f ==0:
			return -1










