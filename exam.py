import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

# Load Dataset
file_path = "Smart_Farming_Crop_Yield_2024.csv"
df = pd.read_csv(file_path)

# Display initial info
print("Initial Dataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Handle Missing Values
print("\nMissing Values Before:")
print(df.isnull().sum())

# Fill or drop missing values
df.fillna(method='ffill', inplace=True)

print("\nMissing Values After:")
print(df.isnull().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Convert datatypes if needed
# Example: convert 'Year' to int
if df['Year'].dtype != 'int64':
    df['Year'] = df['Year'].astype(int)

# Organize data: Group by State and Crop, mean Yield
grouped = df.groupby(['State', 'Crop'])['Yield (kg/ha)'].mean().reset_index()
print("\nAverage Yield per Crop by State:")
print(grouped)

# ========== Data Visualization ==========

# Set style
sns.set(style='whitegrid')

# 1. Crop Yield Distribution
plt.figure(figsize=(12, 6))
sns.histplot(df['Yield (kg/ha)'], kde=True, color='skyblue')
plt.title('Distribution of Crop Yield')
plt.xlabel('Yield (kg/ha)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('yield_distribution.png')
plt.close()

# 2. Yield by State (Top 10)
top_states = df.groupby('State')['Yield (kg/ha)'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='viridis')
plt.title('Top 10 States by Average Crop Yield')
plt.xlabel('Average Yield (kg/ha)')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('top_states_yield.png')
plt.close()

# 3. Yield by Crop Type
plt.figure(figsize=(12, 6))
sns.boxplot(x='Crop', y='Yield (kg/ha)', data=df)
plt.xticks(rotation=45)
plt.title('Crop Yield Variation by Crop Type')
plt.tight_layout()
plt.savefig('crop_yield_variation.png')
plt.close()

# 4. Yield over Time
plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Yield (kg/ha)', data=df, marker='o', hue='Season')
plt.title('Yield Trend Over the Years by Season')
plt.tight_layout()
plt.savefig('yield_trend_by_season.png')
plt.close()

print("\nVisualizations saved as PNG files.")

s
