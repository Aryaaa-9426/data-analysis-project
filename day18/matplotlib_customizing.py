#problem 1
#customize a line plot
import matplotlib.pyplot as plt

tests = [1,2,3,4,5]
marks = [72,78,85,80,90]

plt.plot(
    tests,
    marks,
    color="green",
    linestyle="--",
    linewidth=3,
    marker="o",
    markersize=8
)

plt.title("Student Marks")
plt.xlabel("Test Number")
plt.ylabel("Marks")
plt.grid()

plt.show()

#problem 2
#plot multiple lines 
import matplotlib.pyplot as plt

subjects = ["English","Math","Science","Computer","History"]

student1 = [80,90,85,95,88]
student2 = [75,85,80,92,84]

plt.plot(
    subjects,
    student1,
    color="blue",
    marker="o",
    linestyle="-",
    linewidth=2,
    label="Student A"
)

plt.plot(
    subjects,
    student2,
    color="red",
    marker="s",
    linestyle="--",
    linewidth=2,
    label="Student B"
)

plt.title("Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid()

plt.legend()

plt.show() 

#problem 3 
#challenge 
import matplotlib.pyplot as plt

months = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

sales = [
    12000,15000,14000,18000,
    20000,22000,21000,23000,
    25000,26000,28000,30000
]

plt.figure(figsize=(10,5))

plt.plot(
    months,
    sales,
    color="purple",
    marker="o",
    linewidth=3,
    label="Monthly Sales"
)

plt.title("Monthly Sales of a Shop")
plt.xlabel("Months")
plt.ylabel("Sales (₹)")
plt.grid()

plt.legend()

plt.show() 

