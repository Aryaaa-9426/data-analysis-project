import pandas as pd 

df = pd.read_csv("day12/student_dataset1.csv")
print ("first 5 rows")
print (df.head())
''' first 5 rows
   Unnamed: 0  Gender EthnicGroup  ... MathScore ReadingScore WritingScore
0           0  female     group B  ...        72           72           74
1           1  female     group C  ...        69           90           88
2           2  female     group B  ...        90           95           93
3           3    male     group A  ...        47           57           44
4           4    male     group C  ...        76           78           75

[5 rows x 9 columns]'''
#problem 1
multi_group = df.groupby(["EthnicGroup","Gender"])[["MathScore","ReadingScore"]].mean()
print ("\n Average MathScore and ReadingScores")
print (multi_group) 
'''Average MathScore and ReadingScores
                    MathScore  ReadingScore
EthnicGroup Gender                         
group A     female  60.872483     70.682047
            male    65.396744     63.149957
group B     female  61.197018     71.081536
            male    66.267105     63.958882
group C     female  62.357128     72.061216
            male    67.413554     65.239028
group D     female  65.297973     74.165874
            male    70.322888     66.973678
group E     female  73.006464     77.715143
            male    78.006126     71.199340
'''
# pivot table
pivot = pd.pivot_table(
    df, 
    index="EthnicGroup",
    columns="Gender",
    values="MathScore",
    aggfunc="max"
)
print ("\nPivot Table")
print(pivot)
'''Pivot Table
Gender       female  male
EthnicGroup              
group A          98   100
group B         100   100
group C         100   100
group D         100   100
group E         100   100
'''

# save result 
multi_group.to_csv("multi_group_output.csv")
pivot.to_csv("pivot_table_output.csv")