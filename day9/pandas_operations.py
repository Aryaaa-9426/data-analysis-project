import pandas as pd
import numpy as np
data={
    "name": [ "arya " , "riya" , np.nan, "aman", "neha"],
    "math": [ 85, np.nan,78,92,np.nan],
    "science":[90,88,np.nan,95,80]
} 
df = pd.DataFrame(data)
print("original DataFrame")
print(df)

#prob 2
print("\n missing values in each column;")
print(df.isnull().sum())

#prob 3
#drop rows where is missing 
df=df.dropna(subset=["name"])

#fill math missing 
math_mean=df["math"].mean()
df["math"]=df["math"].fillna(math_mean)

#fill math missing values with mean 
math_mean=df["math"].mean()
df["math"]=df["math"].fillna(math_mean)

#fill sci missing values with mean
science_mean =df["science"].mean()
df["science"]=df["science"].fillna(science_mean)

print("\nCleaned Dataframe")
print(df) 


"""original DataFrame
    name  math  science
0  arya   85.0     90.0
1   riya   NaN     88.0
2    NaN  78.0      NaN
3   aman  92.0     95.0
4   neha   NaN     80.0

 missing values in each column;
name       1
math       2
science    1
dtype: int64

Cleaned Dataframe
    name  math  science
0  arya   85.0     90.0
1   riya  88.5     88.0
3   aman  92.0     95.0
4   neha  88.5     80.0 """