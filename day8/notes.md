# data selection , indexing and filtering 
## selecting columns
-single column :
df["name]
returns a series
-multiple columns :
df[[ "name", "science_score]]
returns a dataframe
## loc 
-label-based indexing 
-uses row labels and columns names 
ex 
df.loc[2]
## iloc
- uses row and column num
- label-based indexing
ex-
df[df["math_score]>80 ]

## multiple condition
AND (&)
def[(df['math_score"]>75)& (df["science_score"]>75)]
or | 
de[(df["math_score"]>90)| (df["science_score]>90)] 


##key points 
[] select columns 
loc-labels
iloc - int position
filtering returns only matching row
use() around conditions with & or | 