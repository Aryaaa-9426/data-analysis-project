# data manipulation 
## topic covered
-stacking arrays using vstack and hstack 
-spliting arrays using vsplit
-sorting arrays using np.sort
# stacking arrays 
### vertical stack (vstack)
-combines array row -wise
-output shape increases in rows 
ex [1,2,3]
   [4,5,6]

   result [[ 1 2 3 ]
           [ 4 5 6 ]]
## horizontal stack (hstack) 
- combines array side by side 
-output becomes a single flat array

ex =[ 1 2 3 4 5 6]
## sorting arrays 
divide dataset into parts 
ex; training / validation 
v_split() -.> split matrix vertically 
split 
part 1 - [[1 2] , [3 4]]
part 2 -[[ 5 6 ] [7 8]]

## sorting 
np.sort() values are arranged in ascending order 
ex [ 45 , 12 , 89, 5 , 23]
sorted [ 5 , 12 , 23 , 45 , 89]