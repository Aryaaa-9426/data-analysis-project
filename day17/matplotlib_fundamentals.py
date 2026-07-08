import matplotlib.pyplot as plt
#first plot

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x, y)

plt.show()

#customizing the plot
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x, y)

plt.title("Simple Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid()

plt.show()

#practice problem 1
#student marks
import matplotlib.pyplot as plt

tests = [1,2,3,4,5]
marks = [70,75,80,85,90]

plt.plot(tests, marks)

plt.title("Student Marks Over 5 Tests")
plt.xlabel("Test Number")
plt.ylabel("Marks")
plt.grid()

plt.show()

#problem 2 
#monthly expenses
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
expenses = [15000,17000,16000,18000,17500,19000]

plt.plot(months, expenses)

plt.title("Monthly Expenses")
plt.xlabel("Months")
plt.ylabel("Expenses (₹)")
plt.grid()

plt.show() 

#problem 3
#temperature over a week
import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temperature = [32,34,35,33,36,37,34]

plt.plot(days, temperature)

plt.title("Daily Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid()

plt.show()



