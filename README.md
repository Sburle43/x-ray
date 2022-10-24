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
## Data Analysis:
We downloaded the corresponding csv-formatted annotation file and DICOM-formatted images from Kaggle and uploaded the dataset to the Hopper Cluster server environment on GMU's supercomputer to extract the images from the compressed zip file. The images were converted to JPG format and saved into a different folder after being input into our Python code in our project space. We downloaded the files using our client computers, and then we transferred them to the Google Colab environment for further analysis. For training and testing, the images are separated into two folders.
* Process of DICOM images to JPG
