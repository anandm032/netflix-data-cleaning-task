# netflix-data-cleaning-task
 Overview

This task involved working with a raw Netflix Movies and TV Shows dataset and preparing it for analysis. The goal was to identify and fix common data issues such as missing values, inconsistent formats, and potential duplicates. I used Python (Pandas) to perform all cleaning operations and created a cleaned version of the dataset that is analysis-ready

 What I Did
Handling Missing Values

Director: Filled 2,634 missing entries with "Unknown" to retain the records.
Cast: Replaced 825 missing values with "Not Provided".
Country: Filled 831 missing values with "Unknown" to ensure uniformity.
Date Added: Dropped 10 records where this column was missing since date info is important for analysis.
Duration: Dropped 3 rows that had no duration information.
Rating: Replaced 4 missing values with the most frequent rating.

### Duplicates
No duplicate rows were found in the dataset, so no action was needed.

### Formatting and Standardization
Renamed all column headers to lowercase with underscores (e.g., release_year, date_added) for consistency.
Converted the 'date_added' column to proper datetime format to enable time-based filtering and analysis.

## Files in This Repository

 `netflix_cleaning.py` – Python script used for data cleaning
 `netflix_titles_cleaned.csv` – Final cleaned version of the dataset
  `README.md` – Summary and explanation of the project

## What I Learned

This project gave me hands-on experience in cleaning real-world data. I practiced identifying and addressing missing data, standardizing formats, and preparing a dataset for deeper analysis. It reinforced the importance of data preprocessing as a critical step in any data science or analytics workflow
