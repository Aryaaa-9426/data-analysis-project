import pandas as pd 
employee ={
    "Employee_ID":[101,102,103,104,105,106],
    "name":["arya","rahul","priya","ankit","sita","ram"],
    "department":["IT","HR","IT","Finance","HR","IT"],
    "current_salary":[50000,60000,70000,80000,90000,100000],
    "performance_score": [5,3,4,5,2,4]
} 
df = pd.DataFrame(employee)
print (df)
'''  Employee_ID   name department  current_salary  performance_score
0          101   arya         IT           50000                  5
1          102  rahul         HR           60000                  3
2          103  priya         IT           70000                  4
3          104  ankit    Finance           80000                  5
4          105   sita         HR           90000                  2
5          106    ram         IT          100000                  4'''

high_performers = df[df["performance_score"] > 4]
print(high_performers)
''' 
   Employee_ID   name department  current_salary  performance_score
0          101   arya         IT           50000                  5
3          104  ankit    Finance           80000                  5'''

high_performers["bonus_amount"] = high_performers["current_salary"] * 0.10
print(high_performers) 

high_performers["total_compensation"] = (high_performers["current_salary"] + high_performers["bonus_amount"])
print(high_performers)
'''    Employee_ID   name  ... bonus_amount  total_compensation
0          101   arya  ...       5000.0             55000.0
3          104  ankit  ...       8000.0             88000.0''' 

#grouping the data by department and calculating the average salary
summary = df.groupby("department").agg(total_staff=("Employee_ID", "count"), average_score=("performance_score", "mean"))
print(summary)