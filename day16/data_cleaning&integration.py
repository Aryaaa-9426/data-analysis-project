import pandas as pd
data = {
    "Transaction_ID": [101, 102, 103, 104, 105],
    "Customer_ID": [201, None, 203, 204, None],
    "Product_Category": ["Electronics", "Clothing", None, "Groceries", "Furniture"],
    "Purchase_Amount": [1200, None, 850, None, 1500]
}

df = pd.DataFrame(data)

print(df)
'''  Transaction_ID  Customer_ID Product_Category  Purchase_Amount
0             101        201.0      Electronics           1200.0
1             102          NaN         Clothing              NaN
2             103        203.0              NaN            850.0
3             104        204.0        Groceries              NaN
4             105          NaN        Furniture           1500.0
'''
print(df.isnull().sum()) 
''' 
Transaction_ID      0
Customer_ID         2
Product_Category    1
Purchase_Amount     2 '''

median_value = df["Purchase_Amount"].median()

df["Purchase_Amount"] = df["Purchase_Amount"].fillna(median_value)

print(df) 
'''   Transaction_ID  Customer_ID Product_Category  Purchase_Amount
0             101        201.0      Electronics           1200.0
1             102          NaN         Clothing           1200.0
2             103        203.0              NaN            850.0
3             104        204.0        Groceries           1200.0
4             105          NaN        Furniture           1500.0
''' 
df = df.dropna(subset=["Customer_ID"])

print(df) 
''' 
Transaction_ID  Customer_ID Product_Category  Purchase_Amount
0             101        201.0      Electronics           1200.0
2             103        203.0              NaN            850.0
3             104        204.0        Groceries           1200.0
''' 
# problem 2 

employee = {
    "Emp_ID": [1, 2, 3, 4, 5],
    "Name": ["Aryan", "Neha", "Rohit", "Priya", "Aman"],
    "Department": ["HR", "Sales", "IT", "Finance", "Sales"]
}

emp_df = pd.DataFrame(employee)
print(emp_df)

''' Emp_ID   Name Department
0       1  Aryan         HR
1       2   Neha      Sales
2       3  Rohit         IT
3       4  Priya    Finance
4       5   Aman      Sales ''' 

performance = {
    "Emp_ID": [1, 2, 4],
    "Sales_Closed": [15, 22, 10],
    "Satisfaction_Score": [4.5, 4.8, 4.2]
}

perf_df = pd.DataFrame(performance)
print(perf_df)
''' Emp_ID  Sales_Closed  Satisfaction_Score
0       1            15                 4.5
1       2            22                 4.8
2       4            10                 4.2 '''

merged_df = pd.merge(
    emp_df,
    perf_df,
    on="Emp_ID",
    how="left"
)

print(merged_df)

''' Emp_ID   Name Department  Sales_Closed  Satisfaction_Score
0       1  Aryan         HR          15.0                 4.5
1       2   Neha      Sales          22.0                 4.8
2       3  Rohit         IT           NaN                 NaN
3       4  Priya    Finance          10.0                 4.2
4       5   Aman      Sales           NaN                 NaN '''

print(
    merged_df[merged_df["Sales_Closed"].isna()]
)

merged_df["Sales_Closed"] = merged_df["Sales_Closed"].fillna(0)

print(merged_df) 

