# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 23:40:09 2022

@author: USER
"""

import pandas as pd
import pickle
df = pd.read_csv('cleaned_diabetic_data.csv')
X = df.drop('readmitted',axis=1)
y = df['readmitted']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
from sklearn.ensemble import RandomForestClassifier
rf_clf=RandomForestClassifier(n_estimators=500, n_jobs=-1, max_depth=30, random_state=42)
rf_clf.fit(X_train,y_train)
y_pred_rf =rf_clf.predict(X_test)
# Create the pickle file
pickle.dump(rf_clf, open('diabetes.pkl', 'wb'))