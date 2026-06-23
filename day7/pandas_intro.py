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

