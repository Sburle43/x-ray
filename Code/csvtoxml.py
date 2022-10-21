# -*- coding: utf-8 -*-
"""CSVtoXML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-mEkZ8qabU6uunhBZ5sdtd_lh5JnhblI
"""

from google.colab import drive
drive.mount('/content/drive')

target_folder = '/content/drive/MyDrive/DAEN690/XMLOutput'
image_src = '/content/drive/MyDrive/DAEN690/images'

#listing out all the files
!ls '/content/drive/MyDrive/DAEN690/'

#import the packages
import os
import pandas as pd #Data manipulation
import numpy as np #Data manipulation
import cv2 # For image size information
#read the train CSV file
df = pd.read_csv ('/content/drive/MyDrive/DAEN690/train2.csv')
print(df)

df.loc[df['image_id'] == '001d127bad87592efe45a5c7678f8b8d']

df.drop('class_name_old', axis=1, inplace=True)
df.drop('class_id_old', axis=1, inplace=True)
df.drop('rad_id', axis=1, inplace=True)

df.loc[df['image_id'] == '001d127bad87592efe45a5c7678f8b8d']

unique_df = df.drop_duplicates()
unique_df = unique_df.replace(np.nan, '', regex=True)

df2 = unique_df.sort_values(by=['image_id','class_name'],ignore_index=True)
#arr_images = df2['image_id'].unique()
df_images = pd.DataFrame(df2['image_id'].unique(), columns = ['image_id'])

df_images.sort_values(by=['image_id'], inplace=True)
df_images.reset_index(drop=True, inplace=True)

nxtImage = '001d127bad87592efe45a5c7678f8b8d'
nxtdf = df2.loc[df2['image_id'] == '001d127bad87592efe45a5c7678f8b8d']
nxtdf

def GetRowXMl(class_name, x_min, y_min, x_max, y_max):
  obj_xml = '<object> \n <name>{0}</name><pose>Frontal</pose><truncated>0</truncated><occluded>0</occluded><bndbox><xmin>{1}</xmin><ymin>{2}</ymin><xmax>{3}</xmax><ymax>{4}</ymax></bndbox><difficult>0</difficult></object>'.format(class_name, x_min,y_min,x_max, y_max)

  #obj_xml = '<object> \n <name>{0}</name><pose>Frontal</pose><truncated>0</truncated><occluded>0</occluded><bndbox></bndbox><difficult>0</difficult></object>'.format(class_name, x_min,y_min,y_max)

  return obj_xml

from numpy import NaN
GetRowXMl('lung_opacityc', 900, 587, 1205, 888)

#or index, row in df_images.iterrows():
#    print(row['image_id'])

image_ist = ['000ae00eb3942d27e0b97903dd563a6e', '000d68e42b71d3eac10ccc077aba07c1', '001d127bad87592efe45a5c7678f8b8d', '0005e8e3701dfb1dd93d53e2ff537b6e']

for index, row in df_images.iterrows():
    #print(row['image_id'])
    nxtdf = df2.loc[df2['image_id'] == row['image_id']]

    if (index%1000 == 0):
      print(index)

    if (row['image_id'] not in (image_ist)):
      continue

    print(row['image_id'])

for index, row in df_images.iterrows():
    #print(row['image_id'])
    nxtImage = row['image_id']
    nxtdf = df2.loc[df2['image_id'] == nxtImage]

    if (index%1000 == 0):
      print(index)

    if (row['image_id'] not in (image_ist)):
      continue

#df.loc[df['image_id'] == '001d127bad87592efe45a5c7678f8b8d']
#nxtImage = '001d127bad87592efe45a5c7678f8b8d'
#nxtdf = df.loc[df['image_id'] == '001d127bad87592efe45a5c7678f8b8d']
    nxtdf.reset_index(drop=True, inplace=True)
    nxtObj = ''
    im = cv2.imread(image_src + '/' + nxtImage + '.jpg')

    img_ht, img_wd, img_cl = im.shape
    #print(img_ht, img_wd, img_cl)

    xml1 = '<annotation><folder>annotations</folder><filename>{0}.jpg</filename>'.format(nxtImage)
    xml2 = '<source><database>Chest XRay Dataset</database><annotation>3</annotation><image>"{0}"</image>'.format(nxtImage)
    xml3 = '</source><size><width>{1}</width><height>{0}</height><depth>{2}</depth></size><segmented>0</segmented>'.format(img_ht, img_wd, img_cl)
    xml4 = ''
    for i in range(len(nxtdf)):
      xml4 = xml4 + GetRowXMl(nxtdf.iloc[i, 1], nxtdf.iloc[i, 3], nxtdf.iloc[i, 4], nxtdf.iloc[i, 5], nxtdf.iloc[i, 6])
    #xml4 = GetRowXMl('lung_opacityc', 900, 587, 1205, 888)
    xml5 = '</annotation>'

    xml = xml1 + xml2 + xml3 + xml4 + xml5
    #xml

    text_file = open(target_folder + '/' + nxtImage + '.xml', "w")
    n = text_file.write(xml)
    text_file.close()

text_file = open(target_folder + '/' + nxtImage + '.xml', "w")
n = text_file.write(xml)
text_file.close()

nxtdf.reset_index(drop=True, inplace=True)
nxtdf