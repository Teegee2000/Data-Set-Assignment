# Import necessary libraries
import pandas as pd

# Load the dataset
url = 'https://www.kaggle.com/gpreda/covid-world-vaccination-progress/download'
df = pd.read_csv(url)

# Save the dataset as a CSV file
df.to_csv('country_vaccinations.csv', index=False) 