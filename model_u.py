from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import numpy as np
import sklearn
import pickle


def label_encoding(target):
    le = LabelEncoder().fit(target)
    le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    print(le_name_mapping)
    return le.transform(target), le_name_mapping


### Split the Data set into Train andtest
def split(X, y, test_size=0.3, shuffle=True):
    return train_test_split(X, y, test_size=test_size, stratify=y,shuffle=shuffle)

def scale(x):
    z_scaler = sklearn.preprocessing.StandardScaler()
    return z_scaler.fit(x)


### Test performance with accuracy score
def preformance(predicted, ytest):
    return accuracy_score(ytest, predicted)

data_df = pd.read_csv("dataformodel.csv")
predictors = data_df.iloc[:, 0:20].values
scaler = scale(predictors)

def model_emo_creation():
    clf = RandomForestClassifier(random_state=42)
    X = scaler.transform(predictors)
    label2 = data_df['Emotion_label']
    yemo, mapping = label_encoding(label2)
    Xemo_train, Xemo_test, yemo_train, yemo_test = split(X, yemo)
    model = RandomForestClassifier(max_depth=13, max_features = 'auto', n_estimators= 90)
    model.fit(Xemo_train,yemo_train)
    yemo_pred = model.predict(Xemo_test)
    print(preformance(yemo_pred,yemo_test))
    pickle.dump(model,open('modelu.pkl','wb'))

def model_gender_creation():
    clf = RandomForestClassifier(random_state=42)
    X = scaler.transform(predictors)
    label2 = data_df['Gender_label']
    yg, mapping = label_encoding(label2)
    Xg_train, Xg_test, yg_train, yg_test = split(X, yg)
    model = RandomForestClassifier(max_depth=13, max_features='auto', n_estimators=80)
    model.fit(Xg_train, yg_train)
    yg_pred = model.predict(Xg_test)
    print(f'gender performance is {preformance(yg_pred, yg_test)}')
    pickle.dump(model, open('modelg.pkl', 'wb'))





if __name__ == '__main__':
    model_emo_creation()
    model_gender_creation()
