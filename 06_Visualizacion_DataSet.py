#!/usr/bin/env python
# coding: utf-8

# # VISUALIZACION DEL DATASET
# En este Notebook se muestran algunos mecanismos más utilizados para la visualizacion del DataSet. Power BI y Looker studio 
# 
# ## DataSet 
# 
# ### Descripción 
# ISCX NSL-KDD 2009 dataset
# 
# Sorry, this data set is no longer available.
# 
# ISCX NSL-KDD is a suggested data set for solving some of the inherent KDD'99 data set problems mentioned in [1]. While this new version of the KDD dataset still presents some of the problems mentioned by McHugh and might not be a perfect representation of existing real networks, due to the lack of public datasets for network-based intrusion detection systems (IDS), we believe it can still be applied as an effective reference dataset to help researchers compare different methods of intrusion detection.
# 
# In addition, the number of records in NSL-KDD training and testing sets is reasonable. This advantage allows to execute the experiments in the entire set without the need to randomly select a small portion. Consequently, the results of the evaluations of different researches will be consistent and comparable.
# 
# Data files
# 
#     KDDTrain+. ARFF : The complete set of NSL-KDD trains with binary tags in ARFF format
#     KDDTrain+. TXT : The full set of NSL-KDD trains, including attack type tags and difficulty level in CSV format
#     KDDTrain+_20Percent.ARFF : a 20% subset of the KDDTrain+.arff file
#     KDDTrain+_20Percent.TXT : a 20% subset of the KDDTrain+.txt file
#     KDDTest+. ARFF : The complete NSL-KDD test set with binary tags in ARFF format
#     KDDTest+. TXT : The full set of NSL-KDD tests, including attack type tags and difficulty level in CSV format
#     KDDTest-21. ARFF : A subset of the KDDTest+.arff file that does not include records with a difficulty level of 21 out of 21
#     KDDTest-21. TXT : A subset of the KDDTest+.txt file that does not include records with a difficulty level of 21 of 21
# 
# Improvements to the KDD'99 dataset
# 
# The ISCX NSL-KDD data set has the following advantages over the original KDD data set:
# 
#     It does not include redundant records in the training set, so classifiers will not be biased to more frequent records.
#     There are no duplicate records in the proposed test sets; therefore, student performance is not biased by methods that have better detection rates in frequent records.
#     The number of records selected from each difficulty level group is inversely proportional to the percentage of records in the original KDD data set. As a result, the classification rates of the different machine learning methods vary over a wider range, which facilitates an accurate assessment of the different learning techniques.
#     The number of records in the training and testing sets is reasonable, allowing experiments to be performed in the entire set without the need to randomly select a small portion. Consequently, the results of the evaluations of different researches will be consistent and comparable.
# 
# Statistical observations
# 
# One of the most important shortcomings of the KDD dataset is the large number of redundant records, which causes learning algorithms to be skewed into frequent records, preventing them from learning infrequent records, which are usually more damaging to networks, such as U2R and R2L attacks. In addition, the presence of these repeated records in the test set will cause the evaluation results to be biased by methods with improved frequent record detection rates.
# 
# In addition, we analyze the difficulty level of the KDD data set records. Surprisingly, approximately 98% of the training set records and 86% of those in the test set were correctly classified with the 21 students.
# 
# To perform our experiments, we randomly created three smaller subsets of the KDD training set, each with fifty thousand information records. Each apprentice was trained with the training sets created. Subsequently, we used the 21 learned machines (7 learners, each trained three times) to label the records of the entire KDD training and test set, which provided us with 21 predicted labels for each record. In addition, we write down each record of the data set with a value #successfulPrediction , initialized to zero. Since the KDD dataset provides the correct label for each record, we compare the predicted label of each record, provided by a specific learner, with the actual label, increasing #successfulPrediction in one if there was a coincidence. Through this process, we calculated the number of learners who were able to correctly label that record. The highest value of #successfulPrediction It is 21, indicating that all learners were able to correctly predict the label of that record.
# Redundant record statistics in the KDD training set
# 
# Original records | Different records | Reduction rate
# 
#     Attacks: 3.925.650 | 262.178 | 93.32%
#     Normal: 972.781 | 812.814 | 16.44%
#     Total: 4.898.431 | 1.074.992 | 78.05%
# 
# Redundant record statistics in the KDD test set
# 
# Original records | Different records | Reduction rate
# 
#     Attacks: 250.436 | 29,378 | 88.26%
#     Normal: 60.591 | 47.911 | 20.92%
#     Total: 311.027 | 77.289 | 75.15%
# 
# License
# 
# You can redistribute, republish, and replicate the ISCX dataset NSL-KDD in any format. However, any use or redistribution of data should include an appointment of the data set NSL-KDD and of the article mentioned below.
# 
# References: [1] M. Tavallaee, E. Bagheri, W. Lu and A. Ghorbani, “ A detailed analysis of the KDD CUP 99 data set "," sent to the Second IEEE Symposium on Computational Intelligence for Security and Defense Applications (CISDA) , 2009.
# 
# [URL](https://www-unb-ca.translate.goog/cic/datasets/nsl.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)

# ## 1.-Lectura del DataSet

# In[4]:


# Lectura del DataSet mediante funciones de python 
with open ("datasets/datasets/NSL-KDD/KDDTrain+.txt")as train_set:
    df = train_set.readlines()
df 


# In[5]:


# Lectura del DataSet utiliando pandas
import pandas as pd
df = pd.read_csv("datasets/datasets/NSL-KDD/KDDTrain+.txt")
df


# In[6]:


# Mostrar los ficheros en el directorio del DataSet
import os 

os.listdir("datasets/datasets/NSL-KDD/")


#  An ARFF (Attribute-Relation File Format) file is an ASCII text file that describes a list of instances sharing a set of attributes. ARFF files were developed by the Machine Learning Project at the Department of Computer Science of The University of Waikato for use with the Weka machine learning software. This document descibes the version of ARFF used with Weka versions 3.2 to 3.3; this is an extension of the ARFF format as described in the data mining book written by Ian H. Witten and Eibe Frank (the new additions are string attributes, date attributes, and sparse instances).
# 
# This explanation was cobbled together by Gordon Paynter (gordon.paynter at ucr.edu) from the Weka 2.1 ARFF description, email from Len Trigg (lenbok at myrealbox.com) and Eibe Frank (eibe at cs.waikato.ac.nz), and some datasets. It has been edited by Richard Kirkby (rkirkby at cs.waikato.ac.nz). Contact Len if you're interested in seeing the ARFF 3 proposal. 
# 
# [ARFF Waikato](https://ml.cms.waikato.ac.nz/weka/arff.html)
# 

# In[7]:


# Instalar un nuevo pauete en el kernel de Notebook para parsear ficheros ARFF 
import sys 
get_ipython().system('{sys.executable} -m pip install liac-arff')


# In[8]:


# Lectura del DataSet que se encuentra en fromado .arff
import arff

with open("datasets/datasets/NSL-KDD/KDDTrain+.arff", 'r') as train_set:
    df = arff.load(train_set)
df.keys()


# In[9]:


df['data']


# In[10]:


df['attributes']


# In[12]:


# Parsear los atributos y obtener unicamente los nombres 
atributos = [attr[0] for attr in df["attributes"]]
atributos


# In[13]:


# Leer el DataFrame con pandas y facilitar su manipulacion
df = pd.DataFrame(df["data"], columns=atributos)
df


# In[ ]:




