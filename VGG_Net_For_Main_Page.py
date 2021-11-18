
# from tensorflow.keras.layers import Input, Lambda, Dense, Flatten,Dropout
# from tensorflow.keras.models import Model
# from tensorflow.keras.applications.vgg19 import VGG19
# from tensorflow.keras.applications.vgg19 import preprocess_input
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.models import Sequential
# import numpy as np
# import pandas as pd
# import os
# import cv2
# import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
import os
import cv2
from keras.models import load_model

# path = '/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/Main_Page_Images/Img4.JPG'

def Find_the_Main_Page(path):
    img_arr=cv2.imread(path)
    img = image.load_img(path,target_size=(224,224))
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    saved_model = load_model('/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/weights/VGG_Net.h5')
    output = saved_model.predict(img)
    print(output)
    Result=output[0]
    max=np.max(Result)
    I=np.where(Result==max)
    Class=['Data_Administration_With_Graph', 'Test_Case_Group', 'Input_Image_Modulation', 'Main_Page', 'Contact', 'Data_Administration']
    print('You are in ' + Class[I[0][0]] + ' Tab')
    return ('You are in ' + Class[I[0][0]] + ' Tab. ')

# Find_the_Main_Page(path)