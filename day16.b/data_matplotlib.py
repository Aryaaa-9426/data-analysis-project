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

## problem 2
import matplotlib.pyplot as plt

# Batch A
study_hours_A = [2, 3, 4, 5, 6]
exam_scores_A = [55, 60, 70, 80, 90]

# Batch B
study_hours_B = [2, 3, 4, 5, 6]
exam_scores_B = [50, 58, 65, 75, 85]

# Scatter Plot
plt.scatter(study_hours_A, exam_scores_A,
            color='blue',
            marker='s',
            label='Batch A')

plt.scatter(study_hours_B, exam_scores_B,
            color='green',
            marker='^',
            label='Batch B')

# Labels
plt.title("Student Performance Analyzer")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")

# Legend
plt.legend()

# Show Plot
plt.show()