##############################################################
#
#Author:Prathamesh Dhumal
#Date:18/7/21
#About: Diabetes Predictor application using Logistic Regression algorithm
#
##############################################################
#Import the Libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from warnings import simplefilter
simplefilter(action ='ignore',category =FutureWarning)
print("____________Diabetes Predictor using Logistic Regression_____________")
#Read the Dataset
diabetes = pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of diabetes data: {}".format(diabetes.shape))

#Split the dataset
X_train,X_test,y_train,y_test =train_test_split(diabetes.loc[:,diabetes.columns
!='Outcome'],diabetes['Outcome'],stratify = diabetes['Outcome'],random_state=66)

logreg = LogisticRegression().fit(X_train,y_train)

print('Accuracy on training set : {:.3f}'.format(logreg.score(X_train,y_train)*100))

print('Accuracy on test set : {:.3f}'.format(logreg.score(X_test,y_test)*100))

logreg001 = LogisticRegression(C =0.01).fit(X_train,y_train)

print('Accuracy on training set : {:.3f}'.format(logreg001.score(X_train,y_train)*100))

print('Accuracy on test set : {:.3f}'.format(logreg001.score(X_test,y_test)*100))
