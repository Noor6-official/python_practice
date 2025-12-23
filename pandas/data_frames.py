import numpy as np
import pandas as pd
data={
    'name':['Noor','aqsa','qasim','suleman'],
    'age':[19,20,18,15],
    'city':['lahore','islamabad','karachi','lahore'],
    'salary':[65000,100000,90000,80000]
    }

df=pd.DataFrame(data)
print(df)
mylist=[
    ['Noor',19,'lahore',65000],
    ['aqsa',20,'islamabad',100000],
    ['qasim',18,'karachi',90000],
    ['suleman',15,'lahore',80000]
]
col=['name','age','city','salary']
df2=pd.DataFrame(mylist)
print(df2)
df2=pd.DataFrame(mylist,columns=col)
print(df2)

#accessing specific column
print(df2['name'])

print(df2[['name','city']])

#adding new column

df2['designation']=['doctor','engineer','doctor','engineer']
print(df2)

#deleting column
print(df2.drop('designation',axis=1))
print(df2)
df2.drop('designation',axis=1,inplace=True)
print(df2)

#deleting row
print(df2.drop([0,1],axis=0))
print(df2)
#df2.drop(2,axis=0,inplace=True)
print(df2)




#selecting rows
row=df2.loc[[0,1]]

print(row)
print(type(row))
row=df2.iloc[[0,1]]

#selecting subsets of rows and columns
row=df2.loc[[0,1]][['city','salary']]
print(row)
row=df2.loc[[2,3]][['name','age']]
print(row)
print(type(row))


#conditional selection

row=df2[df2['age']>18]
print(row)
print(type(row))
row=df2[(df2['age']>18)&(df2['city']=='lahore')]
print(row)