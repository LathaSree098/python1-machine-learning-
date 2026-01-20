import pandas as pd 
df=pd.DataFrame({'job position':['CEO','senior manager','junior manager','employee','assistant staff'],
                'years of experience':[5,4,3,'none',1],
                'salary':[10000,80000,'none',40000,20000]})
df.head()
print(df)