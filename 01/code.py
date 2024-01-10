# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
file_path = 'students-cgpa.csv'
data = pd.read_csv(file_path)

# Display the DataFrame for reference
print("Data from students-cgpa.csv:")
print(data)

# Extract enrollment numbers and CGPA from the DataFrame
enrollment_numbers = data['Enrollment Number']
cgpa = data['CGPA']

# Plotting a bar chart for CGPA
plt.bar(enrollment_numbers, cgpa, color='blue')
plt.xlabel('Enrollment Number')
plt.ylabel('CGPA')
plt.title('CGPA Distribution')
plt.show()
