# Aditya0113-Netflix-Movies-and-TV-Shows

Tools Used: Python, Pandas

🔧 Cleaning Steps Performed:
1. Loaded the dataset and inspected shape, columns, and missing values.
2. Removed duplicates using drop_duplicates().
3. Handled missing values:
   -> Filled director with 'Unknown'
   -> Filled cast with 'Not Available'
   -> Filled country with 'Unknown'
   -> Filled rating with 'Not Rated'
   -> Filled duration with 'Unknown'
   -> Filled date_added with 'January 1, 1900'

4. Converted date_added to proper datetime format (%B %d, %Y) using pd.to_datetime().
5. Standardized text data:
   -> Trimmed whitespace
   -> Converted columns like type, country, rating to title/upper case

6. Renamed all column headers to lowercase with underscores (e.g., date_added, show_id, etc.)
7. Saved cleaned data as netflix_cleaned.csv

📊 Final Dataset:
  -> Total rows: 8807
  -> Null values handled: ✅
  -> Duplicate rows removed: ✅
  -> Date format unified: ✅
  -> Data types fixed: ✅
  -> Column names standardized: ✅
