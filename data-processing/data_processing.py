#%%
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from sklearn.impute import SimpleImputer # used for handling missing data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling



df = pd.read_csv("C:\\Users\\aakash\\Documents\\GIT_WS\\ML\\data-processing\\adult_income.csv")



#look at the outcome variable #salary
print(df['salary'].value_counts())

#assign outcome as 0 if salary is <=50k and 1 if salary is >50k
df['salary']= [0 if  '<=50K' in x else 1 for x in df['salary']]


#Assign x as dataframe of features and y as corresponding outputs salary
x=df.drop('salary',1)
y=df.salary

#basic data cleaning --
"""
  Delaing with data types:
  1> Numeric        : income,age
  2>Oridnal         : Size X<XL<XXL  
  3>Categorical     : sex,nationality

  Models can only handle numerical values

  Must convert categorical and ordinal features into numeric values
  1> Create dummy features
  2>Transform categorical features into a set of dummy features , each representing unique values
  3>In the set of dummy features 1 indicates the obervation belongs to that category

  Ex : make three fetures(colums) X XL and XXL and 1,0,0 signifies obervation is X

  
"""










