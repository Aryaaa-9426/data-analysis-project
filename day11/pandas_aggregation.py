import pandas as pd
df = pd.read_csv("day11/student_dataset.csv")
print (" first 5 rows :")
print(df.head())
 
# class performance 
class_performance = df.groupby("EthnicGroup")[["MathScore","ReadingScore"]].mean()
print("\n class performance (average marks):")
print(class_performance) 

# gender aggregation 
gender_summary = df.groupby("Gender").agg({
    "MathScore": ["count", "max"],
    "ReadingScore": ["min"]
})
print("\n gender summary :")
print (gender_summary)