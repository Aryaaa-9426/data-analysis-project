 boolean indexing (filtring)
 single - df [df["age"]>18]
 multiple - df[(df["age"]>20)&(df["scores"]>80)]
.loc[]accessor 
this returns the name and math columns for students scoring above 80 in mmaths
df.loc[df["math"]>80, ["name", "math"]]
.iloc- used for position based selection 
df.iloc[0:5 , 0:2]
this returns first 5 rows and first 2 columns 
isin()method -checks whether the value exist in a given list 
df[df["name].isin(["alice","david"])]
returns row contating alice or david 

between () method 
used to filter values within range 
df[df["math"].between(80,90)]
- returns rows where math scores are between 80 and 90 
