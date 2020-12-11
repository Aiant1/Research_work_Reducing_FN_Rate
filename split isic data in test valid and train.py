#!/usr/bin/env python
# coding: utf-8

# # Split isic2019 into train test and validation using "split split_isic2019.txt"

# In[30]:


import os
import sys
import numpy as np
import shutil
import scipy
import json
from PIL import Image, ImageFile
import itertools
import cv2
import keras
import glob
import h5py




# !pip install tensorflow==1.15


# In[31]:


path_="/nas/home/ellak-1000013/share/to_joul_2020-12-07/split_isic2019.txt"
catg=[]
nme=[]
mel_n_m=[]
with open("/nas/home/ellak-1000013/share/to_joul_2020-12-07/split_isic2019.txt", 'r') as in_file:
    for i in in_file:
        mel_non_mel=i.split(" ")[1].split("-")[0]
        name=i.split(" ")[-1].split("\n")[0]+".jpg"
        category=i.split(" ")[0]
        mel_n_m.append(mel_non_mel)
        nme.append(name)
        catg.append(category)
        
        


# In[ ]:


folder="/home/antika/antika_old/Ellak/isic2019/images"
# folder_testing="/home/antika/nipgboardprojects/nipgboardprojects/nipg-board-v3/skin_antika/train_test_valid"

train_folder="/home/antika/nipgboardprojects/nipgboardprojects/nipg-board-v3/skin_antika/train_test_valid/train_test_valid/train"

test_folder= "/home/antika/nipgboardprojects/nipgboardprojects/nipg-board-v3/skin_antika/train_test_valid/train_test_valid/test"
valid_folder="/home/antika/nipgboardprojects/nipgboardprojects/nipg-board-v3/skin_antika/train_test_valid/train_test_valid/valid"
lis=os.listdir(folder)
for f in lis:
    if f in nme:
        try:
            indx=nme.index(f)
#             print (indx)


            if catg[indx]=='train':

                if mel_n_m[indx]=="0":
                    modeified_name_with_label="Non-mel"+"_"+ f 

                elif mel_n_m[indx]=="1":

                    modeified_name_with_label="mel"+"_"+ f 
                Rename_images=os.path.join(train_folder,modeified_name_with_label)            
                shutil.copy(os.path.join(folder, f), Rename_images)


            if catg[indx]=='test':
                if mel_n_m[indx]=="0":

                    modeified_name_with_label="Non-mel"+"_"+ f 

                elif mel_n_m[indx]=="1":
                    modeified_name_with_label="mel"+"_"+ f 
                Rename_images=os.path.join(test_folder,modeified_name_with_label)            
                shutil.copy(os.path.join(folder, f), Rename_images)



            if catg[indx]=='valid':
                if mel_n_m[indx]=="0":
                    modeified_name_with_label="Non-mel"+"_"+ f 
                elif mel_n_m[indx]=="1":
                    modeified_name_with_label="mel"+"_"+ f 
                Rename_images=os.path.join(valid_folder,modeified_name_with_label)            
                shutil.copy(os.path.join(folder, f), Rename_images)
        except Exception as ex:
#             print(ex)
            print(f)
            pass
                            

            

            
            


# In[64]:


c_mel=0
c_non=0
for i in os.listdir(test_folder):
    if "Non-mel" in i.split("_"):
        c_non=c_non+1
    if "mel" in i.split("_"):
        c_mel=c_mel+1
        


# In[65]:


print (c_mel)


# In[66]:


print (c_non)


# In[115]:


import os
c=0
c1=0

folder= "/home/antika/nipgboardprojects/nipgboardprojects/nipg-board-v3/skin_antika/train_test_valid/train_test_valid/test"
new_folder="/home/antika/nipgboardprojects/nipgboardprojects/nipg-board-v3/skin_antika/train_test_valid/train_test_valid/balanced_mel_nonm/images"

lis=os.listdir(folder)

for f in lis:
    try:

        if "mel" in f.split("_"):
            print ("yes")

            shutil.copy(os.path.join(folder, f), new_folder)
            c1=c1+1
            if c1==250:
                break
    except Exception as ex:
    #             print(ex)
            print(f)
            pass


# In[116]:


import os
c=0

folder= "/home/antika/nipgboardprojects/nipgboardprojects/nipg-board-v3/skin_antika/train_test_valid/train_test_valid/test"
new_folder="/home/antika/nipgboardprojects/nipgboardprojects/nipg-board-v3/skin_antika/train_test_valid/train_test_valid/balanced_mel_nonm/images"

lis=os.listdir(folder)

for f in lis:
    try:

        if "Non-mel" in f.split("_"):
            print ("yes")

            shutil.copy(os.path.join(folder, f), new_folder)
            c=c+1
            if c==250:
                break
    except Exception as ex:
    #             print(ex)
            print(f)
            pass


# In[120]:


print (c)


# In[ ]:





# In[ ]:




