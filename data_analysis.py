# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset Info
df = pd.read_csv('Global_Cybersecurity_Threats_2015-2024.csv')
print("\nDataset Information: ")
print(df.info())

# Dataset Describe
print("\nDescription of the Dataset:")
print(df.describe())

# Information about columns
print("\nColumns Present in the Dataset:")
print(df.columns)
print("\n Data types of the columns of the dataset: ")
print(df.dtypes)

#Total number of incidents
print("\nTotal number of incidents:", len(df))

# Number of Rows & Columns
print("\nNumber of Rows:", df.shape[0])
print("\nNumber of Columns:", df.shape[1])

#Incidents by year
print("\nIncidents by year:")
print(df['Year'].value_counts().sort_index())

#Reading Dataset
print("\n",df)


# Top 5 data
print("\nFirst 5 Rows of the Dataset:")
print(df.head())



# Top 7  most targeted industries
("\nTop 7 most targeted industries:")
print(df['Target Industry'].value_counts().head(7))


# Top 6 attack types
print("\nTop 6 attack types:")
print(df['Attack Type'].value_counts().head(6))



#Average financial loss by attack type (in Million $):
print("\nAverage financial loss by attack type (in Million $):")
print(df.groupby('Attack Type')['Financial Loss (in Million $)'].mean().sort_values(ascending=False))


#Most common attack sources
print("\nMost common attack sources:")
print(df['Attack Source'].value_counts())


# Dataset Duplicate Value Count
print("\nNumber of Duplicate Values:", df.duplicated().sum())




# Missing Values/Null Values Count
print("\nMissing Values in each Columns of the Dataset: ")
print(df.isnull().sum())


# Check Unique Values for each columns
print("\nUnique Values in each Columns of the Dataset: ")
print(df.nunique())



# Get top 6 attack vectors
top_vectors = df['Attack Type'].value_counts().head(6)

# Plot bar chart for top attack vectors
plt.figure(figsize=(12, 6))
top_vectors.plot(kind='bar')
plt.title('Top 6 Attack Types')
plt.xlabel('Attack Type')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Create a year-wise analysis of top 6 attack vectors
top_5_vectors = df['Attack Type'].value_counts().head(6).index
vector_by_year = df[df['Attack Type'].isin(top_5_vectors)].pivot_table(
index='Year',
columns='Attack Type',
aggfunc='size',
fill_value=0)

# Plot line chart for top 6 attack vectors over time
plt.figure(figsize=(12, 6))
vector_by_year.plot(marker='o')
plt.title('Top 6 Attack Types Trend Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()




# Create a pivot table for sector and year
attacks_by_sector_year = pd.crosstab(df['Target Industry'], df['Year'])

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(attacks_by_sector_year, cmap='YlOrRd', annot=True, fmt='d')
plt.title('Frequency of Cyber Attacks by Sector and Year')
plt.xlabel('Year')
plt.ylabel('Target Industry')
plt.tight_layout()
plt.show()


# Get total attacks by sector
total_by_sector = df['Target Industry'].value_counts()

# Plot bar chart for total attacks by sector
plt.figure(figsize=(12, 6))
total_by_sector.plot(kind='bar')
plt.title('Total Cyber Attacks by Industry Sector')
plt.xlabel('Target Industry')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()