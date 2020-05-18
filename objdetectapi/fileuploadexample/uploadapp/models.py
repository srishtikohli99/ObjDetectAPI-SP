
# Create your models here.
from django.db import models
from django.conf import settings
import os
import datetime
import time
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import cv2
import numpy as np 
import os 
import time
# import tensorflow
# import tensorflow.keras as keras
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# from keras.models import model_from_json,Sequential
# from keras.applications import ResNet50
# from keras.layers import Dense
# import json
# from keras import backend as K


    
class MyFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name,max_length=None):
        ''' name is the current file name '''
        #now = time.time()
        #stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        if self.exists("hello.jpeg"):
            os.remove(os.path.join(settings.MEDIA_ROOT, "hello.jpeg"))
        return "hello.jpeg"


class File(models.Model):
    file = models.ImageField(blank=False, null=False,storage= MyFileSystemStorage())
    #file.name="bye.jpeg"
    def __str__(self):
        return self.file.name

    # def objectDetect():
    #     K.reset_uids()
    #     model = Sequential()
    #     model.add(ResNet50(include_top = False, pooling = 'max', input_shape = (197,197,3)))
    #     model.add(Dense(512, activation = 'tanh'))
    #     model.add(Dense(128, activation= 'tanh'))
    #     model.add(Dense(64, activation= 'tanh'))
    #     model.add(Dense(3, activation = "softmax"))
    #     print("hello5")
    #     model.load_weights('model.h5')
    #     print("hello6")
    #     print("called")
    #     dir = os.path.join(settings.MEDIA_ROOT, "hello.jpeg")
    #     img = load_img(self.file, target_size=(197,197))
    #     x = img_to_array(img)
    #     x = x.reshape(1,197,197,3).astype('float')
    #     ans = model.predict(x)
    #     print(ans)
    #     f=0
    #     for i in range(3):
    #         if ans[0][i] >= 0.8:
    #             f=1
    #             return i+1
    #     if f ==0:
    #             return -1
