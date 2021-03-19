#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pydicom as di 
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
from os import listdir
PathDicom = "/Users/cobi321/Documents/Python/dicom/test"
DCMFiles = [] 
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():
            DCMFiles.append(os.path.join(dirName,filename))


# In[2]:


for k in DCMFiles:
    ds = di.dcmread(k)
    arr = ds.pixel_array
    print(arr)
    plt.imshow(arr, cmap = plt.cm.gray)
    plt.show()


# 
