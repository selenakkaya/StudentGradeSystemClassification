import numpy as np
import logging

import sys
sys.path.append('..')


from fuzzycmeans import FCM
import pandas as pd


#4 clusters has defined by using “fuzzycmeans” 
fcm = FCM(n_clusters=4)
fcm.set_logger(tostdout=True, level=logging.DEBUG)


sys.path.append('..')

data = pd.read_csv('student-mat.csv')
#The final grades of the students were classified as A, B, C, D and a new column was added. 
def define_grade(df):
    grades=[]
   
    for row in df['G3']:
        if row >= 15:
            grades.append('A')
        elif row >= 10:
            grades.append('B')
        elif row >= 5:
            grades.append('C')
        else:
            grades.append('D')
    df['grades'] = grades
    return df  
data = define_grade(data)
data.head()
print(data.columns)

x = data.iloc[:,0:32] #independant value
y = data.iloc[:,33:].values #dependant value

print(x)
print(y)
#Categorical data were translated into numerical data with Label Encoder. 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x['school'] = le.fit_transform(x['school'])

le = LabelEncoder()
x['sex'] = le.fit_transform(x['sex'])

le = LabelEncoder()
x['address'] = le.fit_transform(x['address'])

le = LabelEncoder()
x['famsize'] = le.fit_transform(x['famsize'])

le = LabelEncoder()
x['Pstatus'] = le.fit_transform(x['Pstatus'])

le = LabelEncoder()
x['Mjob'] = le.fit_transform(x['Mjob'])

le = LabelEncoder()
x['Fjob'] = le.fit_transform(x['Fjob'])

le = LabelEncoder()
x['reason'] = le.fit_transform(x['reason'])

le = LabelEncoder()
x['guardian'] = le.fit_transform(x['guardian'])

le = LabelEncoder()
x['failures'] = le.fit_transform(x['failures'])

le = LabelEncoder()
x['schoolsup'] = le.fit_transform(x['schoolsup'])

le = LabelEncoder()
x['famsup'] = le.fit_transform(x['famsup'])

le = LabelEncoder()
x['paid'] = le.fit_transform(x['paid'])

le = LabelEncoder()
x['activities'] = le.fit_transform(x['activities'])

le = LabelEncoder()
x['nursery'] = le.fit_transform(x['nursery'])

le = LabelEncoder()
x['higher'] = le.fit_transform(x['higher'])

le = LabelEncoder()
x['internet'] = le.fit_transform(x['internet'])

le = LabelEncoder()
x['romantic'] = le.fit_transform(x['romantic'])

print(x)

#Data were divided into 33% test, 66% train set. 
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

#All the test and train clusters has converted to array.
x_train_array=np.asarray(x_train)
y_train_array=np.asarray(y_train)
x_test_array=np.asarray(x_test)
y_test=np.asarray(y_test)

print(y_test)


#Classified A,B,C,D letter grades has converted to numeric values
y_train_array_=[]
for i in y_train_array:
    if i=="A":
        y_train_array_.append(0)
        
    elif i=="B":
        y_train_array_.append(1)
        
    elif i=="C":
        y_train_array_.append(2)
        
    elif i=="D":
        y_train_array_.append(3)

y_test_=[]
for i in y_test:
    if i=="A":
        y_test_.append(0)
        
    elif i=="B":
        y_test_.append(1)
        
    elif i=="C":
        y_test_.append(2)
        
    elif i=="D":
        y_test_.append(3)
        
print(y_test_)
#Students data has classified while using FuzzyCMeans (fcm).
fcm.fit(x_train_array, y_train_array_)
predicted_membership = fcm.predict(x_test_array)
print ("\n\ntesting data")
print (x_test_array)
print ("predicted membership")
print (predicted_membership)
print ("\n\n")


#Classified data is visualized.
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(40,40))
ax = fig.add_subplot(111, projection='3d')


sp = ax.scatter(predicted_membership[:,0],predicted_membership[:,1],predicted_membership[:,2], s=20, c=predicted_membership[:,3],linewidths=16)
plt.colorbar(sp)
