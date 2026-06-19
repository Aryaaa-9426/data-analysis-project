import numpy as np
# problem 1
matrix =np.array([[1, 2, 3], [4, 5, 6]])
print("orginal matrix")
print(matrix) 

#multiply by 5 
multiplied_matrix = matrix * 5
print("multiplied matrix")
print(multiplied_matrix)


# matrix of ones
ones=np.ones((2,3), dtype=int)
print("matrix of ones") 
print(ones)

#add the matrix of ones to the original matrix
added_matrix = matrix + ones
print("added matrix")
print(added_matrix)

final_matrix = multiplied_matrix + added_matrix
print("\nfinal matrix;")
print(final_matrix) 


#problem 2
print ("\nGlobal maximum")
#31
print(np.max( final_matrix))
print("\ncolumn sum;")
#[27 37 47]
print(np.sum(final_matrix, axis=0))
print("\nrow mean;")
#[11. 26.]
print(np.mean(final_matrix, axis=1)) 

#problem 3
random_array= np.random.randint(10,51,10)
#[15 42 28 33 19 26 30 12 40 22]
print("\nrandom array")
filtered_array = random_array[random_array > 25]


print ("\nvalues greater than 25")
print(filtered_array)
#[42 28 33 26 30 40]
