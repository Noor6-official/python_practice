import numpy as np
import pandas as pd
data1={

    'Id':[1,2,3,4,5],
    'Name':['John','Anna','peter','linda','bob'],
    'Department':['HR','IT','Finance','IT','HR']
    }

data2={
    'Id':[1,2,3,6,7],
    'salary':[60000,80000,65000,70000,90000],
    'bonus':[5000,10000,7000,8000,12000]

}
employees=pd.DataFrame(data1)
salary=pd.DataFrame(data2)
print(employees)
print(salary)
#merging 
merged=pd.merge(employees,salary, on='Id',how='inner')
print(merged)

merged=pd.merge(employees,salary, on='Id',how='outer')
print(merged)

merged=pd.merge(employees,salary, on='Id',how='left')
print(merged)
merged=pd.merge(employees,salary, on='Id',how='right')
print(merged)


#concatenation
df1=pd.DataFrame({
    'A': ['A0','A1','A2'],
    'B': ['B0','B1','B2'],
    'C': ['C0','C1','C2']

})
df2=pd.DataFrame({
    'A': ['A3','A4','A5'],
    'B': ['B3','B4','B5'],
    'C': ['C3','C4','C5']

})
print(df1)
print(df2)
con=pd.concat([df1,df2])
print(con)
con=pd.concat([df1,df2],axis=1)
print(con)




#joining two dataframes
df1=pd.DataFrame({
    'name':['Alice','Bob','Charlie']

},index=[1,2,3])
df2=pd.DataFrame({
    'score':[85,90,75]

},index=[2,3,4])
print(df1)
print(df2)

df=df1.join(df2,how='outer')
print(df)




