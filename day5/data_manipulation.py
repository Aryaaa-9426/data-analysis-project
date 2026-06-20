import numpy as np
#stacking features 
array_a=np.array([ 1,2,3])
array_b=np.array([4,5,6])
v_stack = np.vstack((array_a,array_b))
print ("vertical stack (vstack):\n", v_stack)
# [[ 1 2 3]
#  [4 5 6]]
h_stack =np.hstack((array_a , array_b))
print("\n horizontal stack (hstack);\n" ,h_stack)
#[ 1 2 3 4 5 6]

# spliting datasets 
matrix =np.arange (1,9).reshape(4,2)
print ("\noriginal matrix;\n", matrix)
v_split =np.vsplit(matrix ,2)
print ("\nvertical split part 1;\n", v_split[0])
print("\n vertical split part2;\n",v_split[1])

# sorting 
arr=np.array([ 45, 12,89,5 ,23])
sorted_arrr=np.sort(arr)
print ("\noriginal array:", arr)
print ("sorted array;", sorted_arrr)