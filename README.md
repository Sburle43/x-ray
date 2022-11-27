# Course: DAEN 690 Fall 2022
## Team: Team Xray
__Team Xray provides the detection of disease conditions in the Chest Xray.__

## Project Title: DETECTION OF CHEST X-RAY ABNORMALITIES USING DICOM IMAGES
## Organization: Accure, Inc.

## Problem Description
Existing methods of interpreting chest X-ray images classify them into a list of findings. There is currently no specification of their locations on the image which sometimes leads to inexplicable results. A solution for localizing findings on chest X-ray images is needed for providing doctors with more meaningful diagnostic assistance.

## Implementation Platform: Python on GMU Hopper Cluster Platform

## Project Duration: August 2022 - December 2022
## Overview
The dataset for this study was created by the Vingroup Big Data Institute (VinBigData) and was acquired via the Kaggle website(https://www.kaggle.com/competitions/vinbigdata-chest-xray-abnormalities-detection/overview).There are 18,000 Postero-anterior (PA) view CXR scans with localization of important features and classification of prevalent thoracic illnesses make up the dataset. The goal is to train object detection computer vision model to detect common thoracic lung diseases and localize the findings.
## Background
The dataset consists of 18,000 Postero-anterior (PA) view CXR scans that come with both the localization of critical findings and the classification of common thoracic diseases. Each finding is localized with a bounding box. The "Findings" and "Impressions" sections of a typical radiology report are represented, respectively, by the local and global labels. They divided the dataset into two parts: the training set of 15,000 scans and the test set of 3,000 scans. The annotation of each image in the test set was even handled and gained from the consensus of 5 radiologists, each image in the training set was individually labeled by 3 radiologists. We used a technique called binary classifier, a compact convolutional neural network, to remove outliers from the dataset (CNN). Upon closer inspection of the training dataset, we found that there is a significant distinction between the observations labeled "anomalies" and those with the label "14" (no finding). We have determined the imbalance and considered several well accepted techniques to mitigate the consequences of the oversampling. One strategy is to obtain or uncover data for the low-frequency classes. The team used SSD for lung abnormality detection and localization in Momentum platform. We experimented several different scenarios which ran for many hours consuming significant GPU resources. The model consumed TF Records for training and validation created from several steps beginning with input data and the model training iterations and tracking the error rates all along in pursuit of best fit model for CXR data.
## LungXray Conditions
The background of the disease conditions are shown in the bar chart with 15 classes including the 'No Finding' class.(https://github.com/Sburle43/x-ray/blob/main/Code/LungXRayBarChart.ipynb)
## Data Analysis
We downloaded the corresponding csv-formatted annotation file and DICOM-formatted images from Kaggle and uploaded the dataset to the Hopper Cluster server environment on GMU's supercomputer to extract the images from the compressed zip file. The images were converted to JPG format and saved into a different folder after being input into our Python code in our project space. We downloaded the files using our client computers, and then we transferred them to the Google Colab environment for further analysis. For training and testing, the images are separated into two folders. The value of the Standard Operating Procedure Instance UID provided by the DICOM tag was encoded to provide a unique identity for each image. Class IDs must not be zero for the following step, thus change class 0 in the annotation file to class 15. A CSV file named annotations train.csv contained the local annotations made by the radiologists on the training set. To make things simpler and reduce errors, we changed the class names in the annotations to lower case, and we removed spaces in favor of underscores. Put a code module in place to upload the annotation file and identify the distinct set of records defined as the combination of the image name, class, and object boundary, and to establish the image size in pixels for each training image.
## Code Repository
The implementation code consisted of the following steps which was repeated for every model scenario for which a new set of datafiles were required 
  1. Gather the DICOM files and extract JPG files from DICOM 
  2. Process the source Annotation file in csv to create XML files, one for every image 
  3. Merge the JPG and XML files to generate TF Record files which were input into the SSD Deep learning models executed in Momentum AI Platform

* Process of extraction of Image content from DICOM files to JPG
The purpose of this script is to convert all the DICOM images are converted into JPG format. The script uses two folder settings, one for DICOM input folder location and another for JPG output location. Each file from the input location is read and pydicom library method dcmread is called to get the pixel content which is then rescaled to 0 to 255 RGB scale. The pixel stream is then saved as JPG file and redirected to the output folder location.  (https://github.com/Sburle43/x-ray/blob/main/Code/convertdicomtojpg.py)

  Primary Input: DICOM files (Sample files included in the xray/Data/DICOM folder)
  Primary Output: JPG Files (Samples files included in the xray/Data/JPG folder)

* Convert CSV to XML:
The Kaggle annotation file was imported into Google Colab and used as input by our scripts, which used the csv annotation file to create an XML file for each image. The next step was to import the XML files and the JPG image files into another Python program to create the TF Records needed for the modeling stage. This dataset reads TFRecords as bytes directly from the files, just as they were written. There is no independent parsing or decoding performed by TFRecordDataset.  (https://github.com/Sburle43/x-ray/blob/main/Code/csvtoxml.py)

  Primary Input: csv Annotation file (Source Kaggle Link shared in the xray/Data/Annotation(XML) folder)
  Primary Output: JPG Files (Samples files shared in the xray/Data/Annotation(XML) folder)

* Merge XML Annotations with JPG Image files to generate TF Records:
This python script is where the XML Annotations are merged with the corresponding Image files in Google Colab development environment to generate TF Records. Placeholder settings include the main root folder, a folder location where all the images reside, a TF output folder to which the output TF Records would be sent upon execution. The function create_trainval_list can be invoked if all available image files should be included in the TF Record creation. If there's a selective list of images only (subset of full list), an alternate is available. A "trainval_Model8.txt" setting can be used to pass to the function create_tf. The create_tf function also takes two other paramters, the folder location where XML annotations are found, and a class dictionary file path. The class dictionary is a file with extension pbtxt that contains a list of all classes and class IDs. The main function calls the tf_create function once each to generate train and validation files under separate sub-folders under the tf_output folder after randomizing the input images and segmenting in 80/20 split. After executing this script, the resultant TF Record files in the in the train and val folders are uploaded into modeling platforms for executing deep learning models. (https//github.com/Sburle43/x-ray/blob/main/Code/tf_creation_model8.py)

  Primary Input: JPG Image Files (Sample Files shared in the xray/Data/JPG folder) + XML Annotation Files (Samples files shared in the xray/Data/Annotation(XML) folder)
  Primary Output: TF RECORD Files (Samples files shared in the xray/Data/TFRecord folder)
