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
"""original dataset: 
      name  math  sci
0    alice    92   90
1      bob    78   82
2  charlie    88   87
3    david    95   91
4      eva    81   79

students scoring above 85 in math AND science :
      name  math  sci
0    alice    92   90
2  charlie    88   87
3    david    95   91

Names and math scores of alice and david:
    name  math
0  alice    92
3  david    95
"""