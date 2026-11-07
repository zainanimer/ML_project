# Human Activity Recognition (HAR) Using Smartphone Sensor Data

## Project Overview
This project focuses on recognizing human daily activities, such as walking, walking upstairs, walking downstairs, sitting, standing, and lying down using motion sensor data (tri-axial accelerometer and gyroscope) from smartphones. 

By framing this as an IoT machine learning task, the system aims to analyze human motion patterns without requiring specialized wearable hardware. The data is processed in fixed 2.56-second sliding windows (128 samples per window at 50 Hz, optimized for FFT feature extraction) and classified using linear and kernel-based machine learning models. 

## Objectives & Research Question

### Objective
To build, evaluate, and compare candidate machine learning models under a strict validation scheme, and ultimately deploy the optimal model with an interactive web user interface.

### Research Question
Does a Support Vector Machine (SVM) achieve a significantly higher macro-F1 score than regularized logistic regression when classifying six daily activities from smartphone sensor features, and which activities are most often confused?

## Dataset & Preprocessing

* **Dataset:** [UCI Human Activity Recognition Using Smartphones Dataset](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones)
* **Samples:** 10,299 instances from 30 volunteers (aged 19–48) wearing a waist-mounted Samsung Galaxy S II.
* **Features:** 561 time- and frequency-domain features extracted from 3-axis linear acceleration and 3-axis angular velocity signals.

## Evaluation Metrics
Models are evaluated using:
* **Primary Metric:** Macro-averaged F1 score.
* **Secondary Metrics:** Overall Accuracy, Precision, Recall.