import pandas as pd
df= pd.read_csv("day14/students.csv")

print ("original Dataset : \n")
print (df) 
''' original Dataset : 

  Student_ID     name   math_score       city 
0        101     arya           85    lucknow 
1        102    rahul        delhi         NaN
2        103    priya           92     mumbai 
3               ankit           76     kanpur 
4        105                    88        pune
''' 
# checking missing values 
print ("\nMissing values:")
print (df.isnull().sum())
'''Missing values:
Student_ID      0
 name           0
 math_score     0
 city           1
dtype: int64'''

#duplicate rows 
print("\nDuplicate rows:")
print(df.duplicated()) 
'''Duplicate rows:
0    False
1    False
2    False
3    False
4    False
dtype: bool'''
 
df.columns=df.columns.str.strip()
print(df.columns)


df.columns =df.columns.str.strip()
df=df.dropna(subset=["Student_ID","name"])
print("\nAfterdropna():")
print(df)
'''
Afterdropna():
   Student_ID   name math_score      city
0       101.0   arya         85  lucknow 
1       102.0  rahul     delhi        NaN
2       103.0  priya         92   mumbai 
'''
print (df.dtypes)
df["math_score"]=pd.to_numeric(df["math_score"], errors="coerce")

mean_score =df["math_score"].mean()
df["math_score"] = df ["math_score"].fillna(mean_score)
print("\nafterfillna():")
print(df)
'''afterfillna():
   Student_ID   name  math_score      city
0       101.0   arya        85.0  lucknow 
1       102.0  rahul        88.5       NaN
2       103.0  priya        92.0   mumbai 
'''
df = df.drop_duplicates(subset=["Student_ID"], keep="first")

print("\ncleaned dataset:\n")
print(df)
''' cleaned dataset:

   Student_ID   name  math_score      city
0       101.0   arya        85.0  lucknow 
1       102.0  rahul        88.5       NaN
2       103.0  priya        92.0   mumbai ''' 

