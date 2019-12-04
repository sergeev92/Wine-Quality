# Wine-Quality
The structure of the readme is as follows:
  - Introduction - contains some brief overview of work done
  - Prerequisites - soft, that needs to be installed in order to be able to run the code
  - Instructions - contains details related to launching and using the code
  - Summary - contains some additional thoughts that were not directly reflected in the code
  
## Introduction
This repository was created for sharing the results of the test task associated with ML engineer job position.

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

## Summary
