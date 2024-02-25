# Import necessary libraries for analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('country_vaccinations.csv')

# Display the first few rows of the dataset
print(df.head())

# Get summary statistics of the dataset
print(df.describe())

# Calculate correlation matrix
corr_matrix = df.corr()
print(corr_matrix)

# Plot histogram of total vaccinations
plt.figure(figsize=(10, 6))
sns.histplot(df['total_vaccinations'], bins=20, kde=True, color='skyblue')
plt.title('Histogram of Total Vaccinations')
plt.xlabel('Total Vaccinations')
plt.ylabel('Frequency')
plt.show()

# Plot line graph of daily vaccinations over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='daily_vaccinations', data=df, marker='o', color='orange')
plt.title('Daily Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Daily Vaccinations')
plt.xticks(rotation=45)
plt.show()

# Plot heatmap of correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()