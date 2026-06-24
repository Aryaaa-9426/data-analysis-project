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