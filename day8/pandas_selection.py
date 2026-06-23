import pandas as pd 
# creating the dataframe 
data={
    "name":["alice","bob","charlie","david","eva" ],
    "math_score": [85,78,90,65,95],
    "science_score": [92,75,88,70,98]
    } 

df = pd.DataFrame(data)
print("original DataFrame;" )
print(df)
"""original DataFrame;
      name  math_score  science_score
0    alice          85             92
1      bob          78             75
2  charlie          90             88
3    david          65             70
4      eva          95             98"""

# indexing and slicing 
print("\n1.name and science_score columns:")
print(df[["name", "science_score"]])
print("\n2.third student (charlie) using iloc")
print(df.iloc[2])
"""1.name and science_score columns:
      name  science_score
0    alice             92
1      bob             75
2  charlie             88
3    david             70
4      eva             98

2.third student (charlie) using iloc
name             charlie
math_score            90
science_score         88
Name: 2, dtype: object
"""
# conditional filtering 
print("\n3. student with math score > 80;")
print (df[df["math_score"]> 80])
print ("\n4. students with math > 75 AND science >75:")
print(df[(df["math_score"]>75)
& (df["science_score"]>75)])