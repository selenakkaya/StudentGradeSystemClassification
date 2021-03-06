
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
 

# data loading
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


x = data.iloc[:,0:32] #independant value
y = data.iloc[:,33:].values #dependant value



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


#Data were divided into 33% test, 66% train set. 
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(x_train) #learn x train and tranform
X_test = sc.transform(x_test) #not learn for x test, use what you have learned


#With the Decision Tree algorithm, letter grades were classified according to the students' information.
#Decision Tree
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion = 'entropy')
dtc.fit(X_train,y_train)
y_pred = dtc.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print('DTC')
print(cm)


#Some attributes are visualized according to letter grades:

#Absences values with respect to letter grades
print("Does absentisim affect on grade?")
plt.scatter(data["grades"],data["absences"], color='k', s=25, marker="o")
plt.show()

#Travel time values with respect to letter grades
b = sns.swarmplot(x='grades', y='traveltime', data=data)
b.axes.set_title('Grades vs Travel Time', fontsize = 30)
b.set_xlabel('grades', fontsize = 20)
b.set_ylabel('traveltime', fontsize = 20)
plt.show()
#Age values with respect to age
b = sns.swarmplot(x='grades', y='age',hue='sex', data=data)
b.axes.set_title('Does age affect grade?', fontsize = 30)
b.set_xlabel('grades', fontsize = 20)
b.set_ylabel('age', fontsize = 20)
plt.show()
#Family relationship with respect to letter grades
b = sns.swarmplot(x='grades', y='famrel', data=data)
b.axes.set_title('Grades vs Family Relationship', fontsize = 30)
b.set_xlabel('grades', fontsize = 20)
b.set_ylabel('famrel', fontsize = 20)
plt.show()


