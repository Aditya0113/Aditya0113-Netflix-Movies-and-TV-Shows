import pandas as pd

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Display basic info
print("Initial Data Info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('January 1, 1900')   # Fill with default
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')

# Convert 'date_added' to datetime format
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')

# Standardize text columns
df['type'] = df['type'].str.strip().str.title()
df['country'] = df['country'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.upper()

# Rename columns (lowercase, replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Show cleaned dataset info
print("\nCleaned Data Info:")
print(df.info())

# Save cleaned dataset
df.to_csv('netflix_cleaned.csv', index=False)

print("\n✅ Data cleaning complete. File saved as 'netflix_cleaned.csv'")
