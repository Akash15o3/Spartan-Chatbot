# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#git clone https://github.com/ultralytics/yolov5
#pip install -U -r yolov5/requirements.txt
import torch
import os 
import random
import shutil
#from sklearn.model_selection import train_test_split
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tqdm import tqdm
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import shutil
import pandas as pd
from PIL import Image
import subprocess

random.seed(108)
# path=str('/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/Main_Page_Images/Img3.JPG')
owd = os.getcwd()
def DetectYOLO(path):
    Class=["Delete","New","Download","Save Tree","Copy Save Tree","Node","Select tree"]
    Results_Path='/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/runs/detect/exp/labels'
    # os.chdir("/Users/aaggarwal/Desktop/college project/Spartan-Chatbot/yolov5")
    dir = '/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/runs/detect/'
    shutil.rmtree(dir)
    print("here 1")
    R = subprocess.call(f"python /Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/detect.py --weights /Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/weights/Data_Admin_With_Graph.pt --img 1024 --conf 0.2 --save-txt --save-crop --source {path}", shell= True)
    print("here 2", R)
    Results = pd.read_csv(Results_Path+'/Img4.txt', names=["Class No", "X", "Y", "W","H"], sep=' ')
    Cls=[]
    for i in range(len(Results['Class No'])):
        Cls.append(Class[Results['Class No'][i]])
    Results['Class']=Cls
    # print(type(Results["Class"]))
    # print(Results['Class'])
    res = str(Results['Class'])
    print(res)
    # im = Image.open('/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/Main_Page_Images/Img3.JPG')
    # plt.imshow(im)
    return str(Results['Class'])
    os.chdir(owd) 
    
# Results=DetectYOLO(path)
# os.chdir(owd)    

# for i in range(len(Results['Class No'])):
#     im = Image.open('C:/Users/tusar/yolov5/runs/detect/exp/crops/'+Results['Class'][i]+'/img3.jpg')
#     plt.figure()
#     plt.imshow(im)
    


    
