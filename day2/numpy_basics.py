import numpy as np 
numbers=np.arange (1,21)
print(numbers)
#output: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]

mean=np.mean(numbers)
print ("Mean:", mean) 

#output: Mean: 10.5

median=np.median(numbers)
print ("Median:", median)
#output: Median: 10.5

std=np.std(numbers)
print ("Standard Deviation:", std)
#output: Standard Deviation: 5.76393202250021
#question 2
matrix =np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatrix:")
print(matrix)
print("Shape:", matrix.shape)
#output: 3 rows and 3 columns 
transpose=matrix.T
print("\nTranspose of the matrix:")
print(transpose)
#output: [[1 4 7]
#         [2 5 8]
#         [3 6 9]]

row_sums=np.sum(matrix, axis=1)
print("\nRow sums:", row_sums)

col_sums=np.sum(matrix, axis=0)
print("Column sums:", col_sums)
#output: Row sums: [ 6 15 24]
#        Column sums: [12 15 18]

array1=np.array([1, 2, 3])
array2=np.array([4, 5, 6])
print("\nArray 1:", array1)
print("Array 2:", array2)
addition =array1 + array2
print("\nAddition, array1 + array2:", addition)
#output: Addition, array1 + array2: [5 7 9] 
multiplication=array1*array2
print("Multiplication, array1 * array2:", multiplication)
#output: Multiplication, array1 * array2: [ 4 10 18]
