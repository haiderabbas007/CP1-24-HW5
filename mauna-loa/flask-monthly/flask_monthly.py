"""
Module to load, process, and save CO₂ concentration data from the Mauna Loa Observatory.

This module performs the following tasks:
1. Loads a CO₂ data file from the Mauna Loa Observatory's flask sampling dataset.
2. Extracts relevant columns: Timestamp, Fractional Year, CO₂ concentration (ppm), and standard deviation (ppm).
3. Saves the processed data as a CSV, JSON, and Markdown file.

Dependencies:
    - pandas: for loading, processing, and saving the data.

File Structure:
    - Input file: 'mauna-loa/flask-monthly/flask_monthly.txt' (raw data file)
    - Output files:
        - CSV: 'mauna-loa/flask-monthly/flask_monthly.csv'
        - JSON: 'mauna-loa/flask-monthly/flask_monthly.json'
        - Markdown: 'mauna-loa/flask-monthly/flask_monthly.md'
"""

import pandas as pd

# Load the file, skipping the metadata rows and treating '-999.99' as NaN for missing values
df = pd.read_csv('mauna-loa/flask-monthly/flask_monthly.txt', delim_whitespace=True, skiprows=54, na_values="-999.99")

# Extract relevant columns
df_extracted = df[["Year", "Month", "Value"]]

# Rename the 'Value' column to 'CO2 (ppm)' in the extracted DataFrame
df_extracted.rename(columns={'Value': 'CO2 (ppm)'}, inplace=True)

# Output to CSV
df_extracted.to_csv('mauna-loa/flask-monthly/flask_monthly.csv', index=False)

# Convert to JSON and save it
df_extracted.to_json('mauna-loa/flask-monthly/flask_monthly.json', orient='records', date_format='iso')

# Convert to Markdown and save it
with open('mauna-loa/flask-monthly/flask_monthly.md', 'w') as md_file:
    md_file.write(df_extracted.to_markdown(index=False))