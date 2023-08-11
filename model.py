# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('breast-cancer-wisconsin.csv')

X = dataset.iloc[:,2:11]
Y = dataset.iloc[:, -1]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=0)


#from imblearn.over_sampling import SMOTE 
#sm = SMOTE(random_state = 2) 
#X_train_res, Y_train_res = sm.fit_sample(X_train, Y_train.ravel())

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.


#from sklearn.ensemble import RandomForestClassifier
#regressor = RandomForestClassifier()
#regressor.fit(X_train,Y_train)
#Fitting model with trainig data

from sklearn.svm import SVC
regressor=SVC()
regressor.fit(X_train,Y_train)

#regressor=RandomForestClassifier()
#regressor.fit(X_train_res, Y_train_res)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[7,4,6,4,6,1,4,3,1]]))
print(model.predict([[5,1,1,1,2,1,3,1,1]]))