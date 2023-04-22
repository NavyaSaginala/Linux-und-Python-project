import os
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Current working directory
print(os.getcwd())

file_path = '/Users/navyasrinivas/Desktop/Data compilation of hummingbird-pollinated plant species.xlsx'

# Reading Excel file into a DataFrame
df = pd.read_excel(file_path)
print(df.head())

# Extract nectar volume and corolla length columns
nectar_volume = df['Nectar_Volume']
corolla_length = df['Corolla_length']

# PGLS analysis
pgls_model = sm.GLSAR(nectar_volume, sm.add_constant(corolla_length), 1)
pgls_results = pgls_model.fit()
print(pgls_results.summary())

# Extracting parameters
intercept = pgls_results.params[0]
slope = pgls_results.params[1]

# Scatter plot of nectar volume vs corolla length
plt.scatter(corolla_length, nectar_volume, c='blue', marker='o', label='Nectar Volume')

# PGLS regression line
plt.plot(corolla_length, intercept + slope * corolla_length, color='red', label='PGLS Regression')

# Adding labels, title, legend
plt.xlabel('Corolla Length (mm)')
plt.ylabel('Nectar Volume (µl)')
plt.title('Relationship between Nectar Volume and Corolla Length in Hummingbird-Pollinated Plants')
plt.legend()

# Displaying the plot
plt.show()
