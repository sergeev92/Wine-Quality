# Wine Quality
The structure of the readme is as follows:
  - Introduction - contains some brief overview of work done and repository structure description
  - Prerequisites - lists soft, that needs to be installed in order to be able to run the code
  - Instructions - contains details related to launching and using the code as well some notes regarding current development process
  - Summary - contains some additional thoughts that were not taken place during current development process
  
## Introduction
This repository was created for sharing the results of the test task associated with ML engineer job position. The main goal was to develop the model which predicts wine quality. This goal was achieved by performing exploratory data analysis, applying data standardization algorithm and feature selection approaches, calibrating and comparing different models with their hyperparameters using grid search and multiple accuracy metrics. 

The structure of the repository is as follows:
  - Input Data folder - contains original input data
    - winequality-white.csv - file with original data
  - Test Data folder - contains standardized and reduced original data that was used for testing during model deveping
    - testData_qualityModel.csv - file with testing data for quality model
    - testData_qualityTypeModel.csv - file with testing data for quality type model
  - Calibrated Models - contains files with calibrated models that can be used separate as imported module
    - qualityModel.sav - file with calibrated quality model
    - qualityTypeModel.sav - file with calibrated quality type model
    - scaler.sav - file with calibrated scaler
  - functions.py - file with some supported functions used for displaying the results of prediction
  - CalibratedModels.ipynb - file with the examples of calibrated models usage
  - WineQuality.ipynb - main file containing all steps of model development process
  
## Prerequisites
In order to be able to run the code, it is necessary to have the following items installed:
  - Phyton 3
  - Jupyter Notebook

It is recommended to perform installation using Anaconda.

## Instructions
It is recommended to start with looking at WineQuality.ipynb with model developing process and then move to CalibratedModels.ipynb to use calibrated models.

First of all it is necessary to run Jupyter Notebook server and open WineQuality.ipynb. As was mentioned above, this file contains all steps of model development process as well as some comments related to the obtained results. In addition, after final model is choosen, this file save all required information to the separate files stored in Test Data and Calibrated Models folders. Given that these files are already presented in the repository, it is not necessary to re-run the whole file but it is possible only to review it.

It should be noted that there are two calibrated models - quality and quality type model. Quality model predicts quality in the format of integer numbers, whereas quality type model use groups of integer numbers to arrive at the format of "low quality", "medium quality" and "high quality". However, these quality types are also presented as integers where 1 corresponds to "low quality" and 3 - to "high quality". 

It should be also mentioned that input data contains few (or no) observations for extremely quality values, like 1, 2, 3 and 9. So, for such cases calibrated models may give worse results. 

After reviewing main file (or in case of ignoring it), it is recommended to open CalibratedModels.ipynb and try to use calibrated model. Currently, the code is written in such a way that it simply takes the same testing data (standardized and reduced), that was used during model development and apply the model for prediction. Thus, the results will be exactly the same as in the main file. 

However, this file can be used with arbitrary data as well. There were some processes of data standardization and feature selection  so the models are calibrated on standardized data and restricted set of features, in particular density and free sulfur dioxide are removed. So, in case of arbitrary data, it should be saved in .csv format like original input data. Then, before applying the model, the data should be standardized and reduced (file CalibratedModels.ipynb contains more detailed comments).

## Summary
Assuming this task, i.e. wine quality predictions, will continue, the following things can be made:
  - Check with experts whether extremely quality values, that are not presented in input data, exist at all, i.e. 1, 2 and 10
  - Check with experts how to correctly split quality values by quality types
  - Try to consider more hyperparameters near the area of best parameters that was chosen during current development process
  - Try to use RandomizedSearchCV instead of GridSearchCV
  - Try to use different (less obvious) combinations of independent variables or to reduce number of features
