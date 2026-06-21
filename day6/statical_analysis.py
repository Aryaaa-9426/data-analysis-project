#problem 1
#student scores
import numpy as np 
scores =np.array([78,85,92,64,89,75,81])
print ("student scres;", scores)
# [ 78 85 92 64 89 75 81]
#mean
mean_score=np.mean(scores)
print ("mean score", mean_score)
# 80.571
#median 
median_score=np.median(scores)
print("median score", median_score)
# 81.0
#std deviation 
std_score=np.std(scores)
print ("std deviation ", std_score)
# 8.731
 # problem 2
highest_score =np.max(scores)
highest_index=np.argmax(scores)
print("highest score " , highest_score)
print("index of highest score", highest_index)
print (f"the top student is at index, {highest_index} with the score of{highest_score} ")
