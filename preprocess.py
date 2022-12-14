# importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# loading dataset and storing in train variable
raw_training_dataset = pd.read_csv('dataset/filtered_city_data_val.csv')

# Fill the empty value in 
imputer = SimpleImputer(missing_values=np.nan,strategy='median')
x = raw_training_dataset.iloc[:,:-1].values
y = raw_training_dataset.iloc[:,-1].values

training_dataset = imputer.fit_transform(x) 
# separating class label and other attributes
# training_array = np.delete(training_dataset,obj=7, axis=1)
# output_array = training_dataset[:, -1]

x_train, x_test, y_train, y_test = train_test_split(training_dataset,y,test_size=0.2,random_state=42)


