# IMDb Movie Success Analytics

## Project Overview

This project analyzes movie performance using the IMDb/TMDB Movie Dataset from Kaggle. The project follows a complete data analytics workflow, from raw data cleaning to SQL analysis, visualization, and machine learning.
The objective is to answer real business questions that can help movie studios and streaming platforms make data-driven decisions.

## Project Workflow

1. Collected raw IMDb/TMDB movie data.
2. Cleaned and transformed the dataset using Python and Pandas.
3. Loaded the cleaned dataset into a SQLite database.
4. Answered business questions using SQL.
5. Created visualizations using Python.
6. Built a machine learning model to predict movie success.

## Business Questions

### SQL Analysis

1. Which movie genres receive the highest audience ratings?
2. Which genres generate the highest average revenue?
3. Which movies generated the highest revenue?
4. Which movies achieved the highest Return on Investment (ROI)?
5. Do longer movies receive higher ratings?
6. How have movie ratings changed over time?
7. Which movies generated the highest audience engagement?
8. Which highly popular movies received poor ratings?

### Python Analysis

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Data visualization
- Revenue analysis
- Genre analysis
- Movie success prediction using Machine Learning

## Key Insights

This analysis uncovered several business insights from the IMDb/TMDB movie dataset:
- Audience ratings vary significantly across movie genres, helping identify genres that consistently receive stronger audience appreciation.
- Commercial success is not always associated with higher audience ratings. Some movies generated substantial revenue despite receiving average or below-average ratings.
- Return on Investment (ROI) provides a better measure of financial success than revenue alone by considering production budget alongside earnings.
- Movies with higher audience engagement (measured by vote count and popularity) are not always the highest-rated titles.
- Movie ratings have changed over time, highlighting trends in audience preferences across different release years.
- Runtime alone does not guarantee better audience ratings, indicating that storytelling and content quality are more important than movie length.
- The machine learning model demonstrates how historical movie attributes can be used to predict the likelihood of movie success.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SQLite
- SQL
- VS Code
- Git
- GitHub

## Project Structure

IMDb_Movie_Success_Analytics
│
├── Python/
│   ├── clean_movies_data.py
│   ├── create_clean_database.py
│   └── ...
│
├── SQL/
│   └── genre_ratings.sql
│
├── Outputs/
│   └── charts and visualizations
│
├── README.md
```

## Dataset
IMDb/TMDB Movie Dataset from Kaggle


## Author
Rubaiyat Tabassum
