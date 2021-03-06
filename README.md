# StudentGradeSystemClassification

The student grade classification system classifies the final grade according to the results of students' family information, school information, personal information, previous exam grades, etc.

# Used Data

This data approach student achievement in secondary education of two Portuguese schools. The data attributes include student grades, demographic, social and school related features and it  was collected by using school reports and questionnaires. Two datasets are provided regarding the performance in two distinct subjects: Mathematics (mat) and Portuguese language (por).

In the given dataset, data is classified, the numerical final grades as a letter grades such as A, B, C. Decision tree algorithm is used.
Source of using the data: https://www.kaggle.com/dipam7/student-grade-prediction


The data that is used has 33 columns, a piece of the data is in the below.

![image](https://user-images.githubusercontent.com/50169967/110218354-bc695000-7eb9-11eb-9a53-c0c88bc066c6.png)

# Decision tree - Machine Learning

A decision tree is a graph that uses a branching method to illustrate every possible outcome of a decision.
A decision tree is a structure used to divide a data set containing a large number of records into smaller clusters by applying a set of decision rules. In other words, it is a structure used by dividing large amounts of records into very small groups of records by applying simple decision-making steps.


The machine is trained in a training set where all data is clear. It learns certain rules. The machine is exported to a data set that it has never seen before and some data is closed. The machine is tested through this cluster. The success of the machine learning algorithm is measured according to the result.

# Method and Approach 
1) The final grades of the students were classified as A, B, C, D and a new column was added.
2) Categorical data were translated into numerical data with Label Encoder.
3) Data were divided into 33% test, 66% train set.
4) With the Decision Tree algorithm, letter grades were classified according to the students' knowledge.
5) Some attributes are visualized according to letter grades:


![image](https://user-images.githubusercontent.com/50169967/110218469-3bf71f00-7eba-11eb-8836-8892620b4a17.png)

![image](https://user-images.githubusercontent.com/50169967/110218487-4c0efe80-7eba-11eb-8d02-5f39e13b1b95.png)

![image](https://user-images.githubusercontent.com/50169967/110218492-58935700-7eba-11eb-9c13-75c52f16ab1b.png)


