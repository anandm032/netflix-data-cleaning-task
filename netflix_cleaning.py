import pandas as pd
df = pd.read_csv("netflix_titles.csv") 
print("Dataset Shape:", df.shape)
print("\nColumn Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())


# Fill missing values
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Provided")
df['country'] = df['country'].fillna("Unknown")

df = df.dropna(subset=['date_added', 'duration'])

most_common_rating = df['rating'].mode()[0]
df['rating'] = df['rating'].fillna(most_common_rating)
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# Check for duplicate rows
print("Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates After Dropping:", df.duplicated().sum())


df.to_csv('netflix_titles_cleaned.csv', index=False)
print("✅ Cleaned data saved as 'netflix_titles_cleaned.csv'")


