data cleaning?
-it is a process of identifying and fixing incorrect ,incomplete ,duplicate, or missing data in a dataset .clean data helps produce accurate analysis 

missing values in pandas 
-nan (not a number) -mising value in pandas 
ex: import pandas as pd
import numpy as np 
data={
    "name" ; ["arya" , np.nan , "riya"],
    "marks " ; [85,90,np.nan]

} 
df=pd.DataFrame (data)

# isnull()
returns true where values are missing 
df.isnull()
# isna()
same as isnull()
df.isna()
# count missing value 
df.isnull().sum

## droping missing values 
remove rows- df.dropna ()
-removes row containing at least one missing value 
## remove column 
-df.dropna(axis=1)

# filling missing values 
df.fillna(0)
fill with mean 
df["marks" ] =df["marks" ].fillna(df["marks"].mean())

fill with median 
df["marks"]=df["marks"].fillna(df["marks"].median ())

fill with mode 
df["marks"]=df["marks"].fillna (df["marks"].mode()[0])

