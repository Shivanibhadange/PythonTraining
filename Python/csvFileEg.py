'''
import pandas as pd
df=pd.read_csv('salaries.csv')

#head top 5 records
print(df.head())

import pandas as pd
df=pd.read_csv('salaries.csv')
#tail bottom 3
print(df.tail(3))

import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.dtypes)

import pandas as pd
df=pd.read_csv('salaries.csv')
print(df)
#no of rows and cols
print(df.shape)


import pandas as pd
df=pd.read_csv('salaries.csv')
print(df)

print(df[0:3]) #row 0 to 2
print(df[4:]) #row 4 onwards



import pandas as pd
df=pd.read_csv('salaries.csv')
#row 0 to 1 and col 0 to 2
print(df.iloc[0:2,0:3])



import pandas as pd
df=pd.read_csv('salaries.csv')
#conditional data
dt=df[(df['salary']>90000)]
print(dt)



import pandas as pd
df=pd.read_csv('salaries.csv')
#conditional data
dt=df[(df['salary']>90000) & (df['discipline']=='B')]
print(dt)

import pandas as pd
df=pd.read_csv('salaries.csv')
#Handling missing value
df['service'].fillna('0',inplace=True)
print(df)


import pandas as pd
df=pd.read_csv('salaries.csv')
#Handling missing value
#Replace by sum,max,min

df['service'].fillna(df['service'].sum(),inplace=True)
print(df)

import pandas as pd
df=pd.read_csv('salaries.csv')
#all null removed
dt=df.dropna()
print(dt)




import pandas as pd
df=pd.read_csv('salaries.csv')
df.insert(6,'test',df['service']+20)
print(df)



import pandas as pd
df=pd.read_csv('salaries.csv')
df1=pd.read_csv('salaries1.csv')

df2=df.append(df1)  #combine both file
print(df2)



#Related data from two csv file
import pandas as pd
df=pd.read_csv('Emp.csv')
df1=pd.read_csv('EmpGrade.csv')

print(pd.merge(df,df1,on='EmpNo'))



import pandas as pd
df=pd.read_csv('salaries.csv')
#salary in ascending order
print(df.sort_values('salary'))


import pandas as pd
df=pd.read_csv('salaries.csv')
#salary is in descending order
print(df.sort_values('salary',ascending=False))



import pandas as pd
df=pd.read_csv('salaries.csv')
#Group on base of rank and display sum of salary
dc=df.groupby(['rank'])
print(dc['salary'].sum())



#...............pivote---gives summarize data.................


import pandas as pd
df=pd.read_csv('StudentDataForPivot.csv')
print(pd.pivot_table(df,index=['Name','Subject'],
                     values='Score',aggfunc='sum'))



import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.plot(df['EmpCode'],df['Payment'],color='red',linestyle='--',linewidth=5)
plt.show()



import pandas as pd
df=pd.read_csv('EmpData.csv')
dfg=df.groupby('City')
total=dfg['Payment'].sum()
total.plot(kind='bar')



import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.hist(df['Payment'],bins=5)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
c=df.groupby(df['City'])
cp=['red','green','blue']
c.sum().plot(kind='pie',y='Payment')
'''

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.scatter(df['Payment'],df['NoOfHours'],marker='o')
plt.show()














