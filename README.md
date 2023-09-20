## AIES Tutorial For Traditional ML Explainability 

## Introduction 

This repository is the code associated with the AMS AIES manuscript titled: "An Introductory Machine Learning Explainability Tutorial for Atmospheric Sciences," written by Flora, M, Potvin, C, McGovern, A, and Handler, S. Find the paper here and provide any comments via email to the corresponding author. If you have any issues with the code (bugs or other questions), please leave an issue associated with this repo.

This paper and repo cover a general approach to explaining and understanding traditional supervised machine learning methods (e.g., the sklearn models). Topics in the paper include interpretability versus explainability, local versus global explainability, and feature importance versus feature relevance. We demonstrate explainability using Shapley-based methods as they have been found to unify many pre-existing explainability methods ([Lundberg et al. 2016](https://papers.nips.cc/paper_files/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html), Covert et al. 2020[a](https://arxiv.org/abs/2004.00668),[b](https://arxiv.org/abs/2011.14878)).


## Motivation 
Machine learning algorithms (ML) are increasingly common in the atmospheric sciences (Chase et al. 2023). A key advantage of ML models is their ability to leverage multiple input features and learn useful multivariate relationships for prediction, calibration, and post-processing. However, many ML models are considered "black boxes" in that the end-user cannot readily understand the internal workings of the model ([McGovern et al. 2019](https://journals.ametsoc.org/view/journals/bams/100/11/bams-d-18-0195.1.xml)). ML systems in low-risk situations may not need to be understood, but in high-risk situations--like severe weather forecasting--decision-makers want to know why a model came to its prediction. As part of building trust of human forecasters in ML predictions, it is essential to explain the "why" of an ML model's prediction in understandable terms and to create real-time visualizations of these methods. Moreover, understanding a model's inner workings can identify strengths and weaknesses and possibly lead to improvements in the model. 

To accelerate the adoption of machine learning explainability within meteorology, we created this repository with a code tutorial for the topics discussed in this paper. We have also created the [scikit-explain](https://github.com/monte-flora/scikit-explain) python package, which computes and visualizes several explainability methods (including methods not discussed in this paper). All three datasets and ML models used in this study are available at https://doi.org/10.5281/zenodo.8184201. Code for easily downloading these data is available under [src/tutorial_notebooks](https://github.com/monte-flora/explain_tutorial/blob/main/src/tutorial_notebooks/Notebook00_Download_Data_and_Models.ipynb). 



## Getting Started 

This paper strives to provide a comprehensive understanding of model explainability, even for those who may be new to the concept. While we assume familiarity with ML methods and terminology, we recommend [Chase et al. repo](https://github.com/ai2es/WAF_ML_Tutorial_Part1) for novice readers. These resources offer a great introduction to ML for operational meteorology and provide open-source code to help apply the methods. The process for setting up a Python environment in that github repo should also include all the necessary packages (including scikit-explain) to begin using the tutorial notebooks in this repo. 

## Use Google Colab 

   This is the recommended and the quickest way to get started and only requires a (free) google account. Google Colab is a cloud instance of python that is run from your favorite web browser (although works best in Chrome). If you wish to use these notebooks, navigate to the directory named ```src/tutorial_notebooks```. 
   
   Once in that directory, select the notebook you would like to run. There will be a button that looks like this once it loads: 

   ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)

   Click that button and it will take you to Google Colab where you can run the notebook. Please note it does not save things by default, so if you would like to save your own copy, you will need to go to File -> save a copy in drive

   <img src="images/save2drive.png" width="200" height="275" class="center" />


   Google colab is awesome for those who do not know how to install python, or just dont have the RAM/HDD locally to do things. You can think of it this way. This notebook is just providing the instructions (i.e., code) to do what you want it to. Meanwhile the data and physical computer are on some Google machine somewhere, which will execute the code in the notebook. By default this google owned machine will have 12 GB of RAM and about 100 GB of HDD (i.e. storage). 






