import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [30, 32, 31, 33, 35, 34, 36]

# Line Plot
plt.plot(days, temperature,
         color='red',
         linestyle='--',
         marker='o')

# Title and Labels
plt.title("Weekly Temperature Trends")
plt.xlabel("Days")
plt.ylabel("Temperature in °C")

# Grid
plt.grid(True)

# Show Plot
plt.show() 