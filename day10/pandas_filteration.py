import pandas as pd 
data ={
    "name":[ "alice" , "bob", "charlie","david" ,"eva"],
    "math": [92,78,88,95,81],
    "sci":[90,82,87,91,79]

} 
df=pd.DataFrame (data)
print("original dataset: ")
print (df)

print("\nstudents scoring above 85 in math AND science :")
high_achievers=df[(df["math"]>85)& (df["sci"]>85)]
print (high_achievers)

print("\nNames and math scores of alice and david:")
selected_students=df.loc[
    df["name"].isin(["alice", "david"]),
    ["name", "math" ]
] 
print (selected_students)