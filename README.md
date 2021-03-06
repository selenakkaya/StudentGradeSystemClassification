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

-------------------------------------------------------------
-------------------------------------------------------------

# Fuzzy

The basis of fuzzy logic is based on fuzzy sets and subsets. In the classical approach, an entity is either an element of a cluster or not. Mathematically, when the entity is an element of the set, it takes the value of "1” or “0” when it is not an element of the set. Fuzzy logic is the extension of the classical set representation. In the fuzzy asset set, each asset has a degree of membership. The degree of membership of assets can be any value in the range (0, 1). For instance, It might be 0.78.
This paper focuses on Fuzzy Clustering:
Fuzzy clustering is a clustering method where data points can belong in more than one group (“cluster”). Clustering divides data points into groups based in similarity between items and looks to find patterns or similarity between items in a set; Items in clusters should be as similar as possible to each other and as dissimilar as possible to items in other groups. Computationally, it’s much easier to create fuzzy boundaries than it is to settle on one cluster for one point.


# Method and Approach 
1) The final grades of the students were classified as A, B, C, D and a new column was added.
2) Categorical data were translated into numerical data with Label Encoder.
3) Data were divided into 33% test, 66% train set.
4) 4 clusters has defined by using “fuzzycmeans”
5) The final grades of the students were classified as A, B, C, D and a new column was added.
6) Categorical data were translated into numerical data with Label Encoder.
7) Data were divided into 33% test, 66% train set.
8) 4 clusters has defined by using “fuzzycmeans”
9)Classified data is visualized

![image](https://user-images.githubusercontent.com/50169967/110218571-baec5780-7eba-11eb-846b-42c6b3c1d301.png)

