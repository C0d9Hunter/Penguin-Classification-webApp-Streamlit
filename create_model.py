import pandas as pd
import numpy as np 
from sklearn.ensemble import RandomForestClassifier
import pickle


penguins = pd.read_csv("penguins_cleaned.csv")

df = penguins.copy()
target = "species"
encode = ['sex','island']

for col in encode:
    dummy = pd.get_dummies(df[col],prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]

#mapper le nom des classe
target_mapper = {
    'Adelie':0,
    'Chinstrap':1,
    'Gentoo':2
}

#funtion to encode target
def target_encode(val):
    return target_mapper[val]

df['species']=df['species'].apply(target_encode)

#separation of X and Y
X = df.drop('species',axis=1)
Y = df['species']

#Random Forest Classification
clf = RandomForestClassifier()
clf.fit(X,Y)

pickle.dump(clf, open("Penguins-RandomForest.model","wb"))
