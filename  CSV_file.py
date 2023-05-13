import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('people.csv')

# Plot a histogram of the ages
plt.hist(data['Age'], bins=range(20, 70, 5), edgecolor='black')
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
