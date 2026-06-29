import pandas as pd 
term1 = pd.read_csv("day13/students_term1.csv")
term2 = pd.read_csv("day13/students_term2.csv")

master_df = pd.concat([term1 , term2] , ignore_index=True)
print(master_df)
'''  Student_ID    Math    Science 
0          101      85         88
1          102      90         92
2          103      78         80
3          104      81         84
4          105      95         91
5          106      87         89'''

students = pd.DataFrame({
    "Student_ID" : [101,102,103,104],
    "name":["arya", "aditya", "simpee", "kunal"],
    "class": [ "cse","cse", "aiml", "ece"]
})

clubs = pd.DataFrame ({
    "Student_ID" : [ 101 , 103 ],
    "club_acitivity" : [ "coding club", "dance club"],
    "attendance_rate" : [95 , 88]
})

student_profile = pd.merge(
    students,
    clubs,
    on="Student_ID",
    how="left"
) 
print (student_profile)

'''Student_ID    name class club_acitivity  attendance_rate
0         101    arya   cse    coding club             95.0
1         102  aditya   cse            NaN              NaN
2         103  simpee  aiml     dance club             88.0
3         104   kunal   ece            NaN              NaN'''

master_df.to_csv("day13/students_term1_term2_combined.csv", index=False)
student_profile.to_csv("day13/student_profile.csv", index=False)