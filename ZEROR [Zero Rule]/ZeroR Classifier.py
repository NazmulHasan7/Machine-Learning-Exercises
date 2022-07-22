# -*- coding: utf-8 -*-
"""ZeroR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zLZtLoNs_UKbHsAYBRIY8Uzja3-B__Mv

#  ***ZeroR Classifier***
*ZeroR is the simplest classification method which 
relies on the target and ignores all predictors. ZeroR classifier simply predicts the majority category (class). Although there is no predictability power in ZeroR, it is useful for determining a baseline performance as a benchmark for other classification methods.*
"""

# importing libraries
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# to read & handle files
import pandas as pd

# reads the csv file containg the data
df = pd.read_csv('/content/Weather Dataset.csv')
print('Data: \n{}'.format(df))
print('Shape {}\n'.format(df.shape))

# prints first five instances of the dataframe
print('First Five Instances: \n{}'.format(df.head()))
# prints statistical description of the dataframe
print('Dataframe Description: \n{}'.format(df.describe()))

# dropping play column to separte the features
features = df.drop(columns = ['play'])
print('Attributes: \n{}\n'.format(features))

# set play as the target class
target = df['play']
print('Target Class: \n{}'.format(target))

# using ZeroR classifier
# most_frequent: the predict method always returns the most frequent class label in the observed y argument passed to fit. 
model = DummyClassifier(strategy = 'most_frequent', random_state = 0)

# fit() is used to train the model
model.fit(features, target)
# dataset is trained and a model is created

# predictions of the model
predictions = model.predict(features)
print('Predictions made by the ZeroR classifier')
print(predictions)

# accuracy of the prediction by the model
score = accuracy_score(target, predictions)
print('Accuracy score of the model: ')
print(score)

# confusion matrix
print(confusion_matrix(target, predictions))

# plotting confusion matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

conf_matrix = confusion_matrix(target, predictions)
# creating confusion matrix display object - alphabetical sorting order
conf_matrix_dis_object = ConfusionMatrixDisplay(conf_matrix, display_labels=['NO', 'YES'])
conf_matrix_dis_object.plot()

# using axes attribute 'ax_' to get the underlying axes
conf_matrix_dis_object.ax_.set(
    title = 'Confusion Matrix for ZeroR',
    xlabel = 'Predicted',
    ylabel = 'Actual'
)
plt.show()