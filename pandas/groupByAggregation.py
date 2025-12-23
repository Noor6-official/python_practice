import numpy as np
import pandas as pd
data={

    'Category':['A','B','A','B','A','B','A','B'],
    'Store':['s1','s1','s2','s2','s1','s2','s3','s1'],
    'Sales':[100,200,120,181,100,200,300,150],
    'Quantity':[10,15,12,18,8,20,15,25],
    'Date':pd.date_range('2023-01-01',periods=8)
    
    }
df=pd.DataFrame(data)
print(df)
cat=df.groupby('Category')

for i, v in cat:
    print(i)
    print(v)

cat2=df.groupby('Category')['Sales'].sum()
print(cat2)




cat=df.groupby('Store')
for i, v in cat:
    print(i)
    print(v)

cat=df.groupby('Store')['Quantity'].sum()
print(cat)


cat=df.groupby(['Category','Store'])
for i, v in cat:
    print(i)
    print(v)

cat=df.groupby(['Category','Store'])['Sales'].sum()
print(cat)


#aggregation
mean=df['Sales'].max()
#mean median mode std min max count std
print(mean)


agg=df['Sales'].agg(['sum','median','max','min','std'])
print(agg)




