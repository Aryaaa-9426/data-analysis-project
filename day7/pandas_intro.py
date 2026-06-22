import pandas as pd
data={ 
    "name":["alice","bob","charlie","david"],
    "math_score":[ 78,85,92,64],
    "sci_score":[ 82,79,89,70],

}
df =pd.DataFrame(data)
# print the dataframe
print("class grade frame:\n")
print(df)
#first five frame 
print("\n first five row:")
print(df.head())
#info about the dataframe
print("\n DataFrame info:")
print(df.info())
#print("\n statistical summary:")
print(df.describe())

DataFrame Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex:4 entries,0 to 3
Data columns (total 3 columns):
name              object
math_score        int64
sci_score         int64
print ("\nStatical summary")
print (df.describe())