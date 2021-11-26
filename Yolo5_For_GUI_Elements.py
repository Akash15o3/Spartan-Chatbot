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
import cv2
import shutil
#from sklearn.model_selection import train_test_split
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tqdm import tqdm
from PIL import Image, ImageDraw
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
matplotlib.use("TkAgg")
import shutil
import pandas as pd
from PIL import Image
import subprocess
from pathlib import Path

random.seed(108)
# path=str('/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/Main_Page_Images/Img3.JPG')
owd = os.getcwd()
def DetectYOLO(path,text):
    Class=["Delete","New","Download","Save Tree","Copy Save Tree","Node","Select tree"]
    Results_Path='/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/runs/detect/exp/labels'
    dir = '/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/runs/detect/'
    shutil.rmtree(dir)
    print("here 1")
    R = subprocess.call(f"python /Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/detect.py --weights /Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/weights/Data_Admin_With_Graph.pt --img 1024 --conf 0.5 --save-txt --save-crop --source {path}", shell= True)
    print("here 2", R)
    x = Path(path).stem
    Results = pd.read_csv(f"{Results_Path}/{x}.txt", names=["Class No", "X", "Y", "W","H"], sep=' ')
    Cls=[]
    for i in range(len(Results['Class No'])):
        Cls.append(Class[Results['Class No'][i]])
    Results['Class']=Cls
    res = str(Results['Class'])
    image_bounding_box_tcg(Results, path, text)
    print(res)
    return Results['Class']


def DetectYOLOTestCaseGroup(path, text):
    Class = ["Search Bar","Action","Output File Name","Context File Name","Input File Name","Input File Type","Upload Results","Execute Test Case","Product Sub Version","Product Version","Full Screen","Toggle","Refresh","New Group"]
    Results_Path='/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/runs/detect/exp/labels'
    dir = '/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/runs/detect/'
    shutil.rmtree(dir)
    print("here 1")
    R = subprocess.call(f"python /Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/yolov5/detect.py --weights /Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/weights/Test_Case_Group.pt --img 1024 --conf 0.5 --save-txt --save-crop --source {path}", shell= True)
    print("here 2 in TCG", R)
    x = Path(path).stem
    # Results_Path + '/Img3.txt'
    Results = pd.read_csv(f"{Results_Path}/{x}.txt", names=["Class No", "X", "Y", "W","H"], sep=' ')

    Cls=[]
    for i in range(len(Results['Class No'])):
        Cls.append(Class[Results['Class No'][i]])
    Results['Class'] = Cls
    res = str(Results['Class'])
    image_bounding_box_tcg(Results, path, text)
    print(res)
    return Results['Class']

def image_bounding_box_tcg(data, path, text):
    idx = 0
    # class_name_to_id_mapping = ["Search Bar", "Action", "Output File Name", "Context File Name", "Input File Name", "Input File Type",
    #          "Upload Results", "Execute Test Case", "Product Sub Version", "Product Version", "Full Screen", "Toggle",
    #          "Refresh", "New Group"]

    for i in range(0, len(data)):
        # print(i,class_name_to_id_mapping[i],text)
        if data["Class"][i] in text:
            print("SFMNSFSm", i)
            idx = i
            break
    print(data)

    im = plt.imread(path)

    # Create figure and axes
    fig, ax = plt.subplots()
    # Display the image
    ax.imshow(im)

    x,y,z= im.shape
    print("SHAPE SIZES",x,y)
    X = y * data["X"].values[idx]
    Y = x * data["Y"].values[idx]
    W = y * data["W"].values[idx]
    H = x * data["H"].values[idx]

    # Create a Rectangle patch
    rect = patches.Rectangle((X - W / 2, Y - H / 2), W, H, linewidth=1, edgecolor='k', facecolor='none')
    count = len(os.listdir('/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/static/bounding_images/'))
    print("Count",count)
    # Add the patch to the Axes
    im = ax.add_patch(rect)
    plt.savefig(f'/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/static/bounding_images/img{count+1}.jpeg')
    # plt.show()

def image_bounding_box_dawg(data, path, text):
    idx = 0
    # class_name_to_id_mapping = ["Search Bar", "Action", "Output File Name", "Context File Name", "Input File Name", "Input File Type",
    #          "Upload Results", "Execute Test Case", "Product Sub Version", "Product Version", "Full Screen", "Toggle",
    #          "Refresh", "New Group"]

    for i in range(0, len(data)):
        # print(i,class_name_to_id_mapping[i],text)
        if data["Class"][i] in text:
            print("SFMNSFSm", i)
            idx = i
            break
    print(data)

    im = plt.imread(path)

    # Create figure and axes
    fig, ax = plt.subplots()
    # Display the image
    ax.imshow(im)

    x,y,z= im.shape
    X = y * data["X"].values[idx]
    Y = x * data["Y"].values[idx]
    W = y * data["W"].values[idx]
    H = x * data["H"].values[idx]

    # Create a Rectangle patch
    rect = patches.Rectangle((X - W / 2, Y - H / 2), W, H, linewidth=1, edgecolor='r', facecolor='none')
    count = len(os.listdir('/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/static/bounding_images/'))
    print("Count",count)
    # Add the patch to the Axes
    im = ax.add_patch(rect)
    plt.savefig(f'/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/static/bounding_images/img{count+1}.jpeg')
    # plt.show()