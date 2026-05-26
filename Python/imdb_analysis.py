import pandas as pd

df = pd.read_csv(r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv", low_memory=False)

print(df.head())
print(df.columns)
print(df.info())


import pandas as pd

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Show first 5 rows
print(df.head())

# Show all column names
print(df.columns)

# Check missing values
print(df.isnull().sum())

# Show data types
print(df.info())

import pandas as pd

df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep only useful columns
df = df[
    [
        "title",
        "genres",
        "release_date",
        "runtime",
        "budget",
        "revenue",
        "popularity",
        "vote_average",
        "vote_count",
        "original_language",
        "status"
    ]
]

# Convert number columns
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Convert date column
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

# Create release year column
df["release_year"] = df["release_date"].dt.year

# Show cleaned info
print(df.head())
print(df.info())
print(df.isnull().sum())

# Which movies have the highest ratings?
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep useful columns
df = df[
    [
        "title",
        "genres",
        "release_date",
        "runtime",
        "budget",
        "revenue",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]

# Convert columns to numeric
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Remove movies with very low vote counts
df = df[df["vote_count"] > 100]

# Top 10 highest rated movies
top_movies = df.sort_values(
    by="vote_average",
    ascending=False
)[["title", "vote_average", "vote_count"]].head(10)

# Print result
print(top_movies)

# Create chart
plt.figure(figsize=(10,6))

plt.barh(
    top_movies["title"],
    top_movies["vote_average"]
)

plt.xlabel("Average Rating")
plt.ylabel("Movie Title")
plt.title("Top 10 Highest Rated Movies")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()

# Which movies are the most popular?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep useful columns
df = df[
    [
        "title",
        "genres",
        "release_date",
        "runtime",
        "budget",
        "revenue",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]

# Convert columns to numeric
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Remove movies with very low vote counts
df = df[df["vote_count"] > 100]

# Top 10 most popular movies
top_popular = df.sort_values(
    by="popularity",
    ascending=False
)[["title", "popularity", "vote_average"]].head(10)

# Print results
print(top_popular)

# Create chart
plt.figure(figsize=(10,6))

plt.barh(
    top_popular["title"],
    top_popular["popularity"]
)

plt.xlabel("Popularity Score")
plt.ylabel("Movie Title")
plt.title("Top 10 Most Popular Movies")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()

# Do longer movies receive higher ratings?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep useful columns
df = df[
    [
        "title",
        "genres",
        "release_date",
        "runtime",
        "budget",
        "revenue",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]

# Convert columns to numeric
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Remove movies with very low vote counts
df = df[df["vote_count"] > 100]

# Runtime vs Rating Analysis

# Remove missing runtime values
runtime_df = df.dropna(subset=["runtime", "vote_average"])

# Print correlation
correlation = runtime_df["runtime"].corr(runtime_df["vote_average"])

print("Correlation between runtime and rating:")
print(correlation)

# Create scatter plot
plt.figure(figsize=(10,6))

plt.scatter(
    runtime_df["runtime"],
    runtime_df["vote_average"],
    alpha=0.5
)

plt.xlabel("Runtime (Minutes)")
plt.ylabel("IMDb Rating")
plt.title("Runtime vs Movie Rating")

plt.tight_layout()

plt.show()

# Which genres generate the highest revenue?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep useful columns
df = df[
    [
        "title",
        "genres",
        "release_date",
        "runtime",
        "budget",
        "revenue",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]

# Convert columns to numeric
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Remove movies with very low vote counts
df = df[df["vote_count"] > 100]

# Clean genres column
df["genres"] = df["genres"].str.extract(r"'name': '([^']+)'")

# Remove movies with missing genres or revenue
genre_revenue = df.dropna(subset=["genres", "revenue"])

# Group by genre
genre_revenue = genre_revenue.groupby("genres")["revenue"].mean()

# Top 10 genres by average revenue
top_genres = genre_revenue.sort_values(
    ascending=False
).head(10)

# Print results
print(top_genres)

# Create chart
plt.figure(figsize=(10,6))

plt.barh(
    top_genres.index,
    top_genres.values
)

plt.xlabel("Average Revenue")
plt.ylabel("Genre")
plt.title("Top Genres by Average Revenue")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()

# Which genres receive the highest ratings?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep useful columns
df = df[
    [
        "title",
        "genres",
        "release_date",
        "runtime",
        "budget",
        "revenue",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]

# Convert columns to numeric
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Clean genres column
df["genres"] = df["genres"].str.extract(r"'name': '([^']+)'")

# Remove missing genre/rating values
genre_rating = df.dropna(subset=["genres", "vote_average", "vote_count"])

# Keep only movies with enough votes
genre_rating = genre_rating[genre_rating["vote_count"] > 100]

# Calculate average rating by genre
genre_rating_result = genre_rating.groupby("genres")["vote_average"].mean()

# Get top 10 highest rated genres
top_rated_genres = genre_rating_result.sort_values(ascending=False).head(10)

# Print result
print("Top 10 Genres by Average Movie Rating:")
print(top_rated_genres)

# Create chart
plt.figure(figsize=(10, 6))

plt.barh(
    top_rated_genres.index,
    top_rated_genres.values
)

plt.xlabel("Average Rating")
plt.ylabel("Genre")
plt.title("Top Genres by Average Movie Ratings")

plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()

# How Have Movie Ratings Changed Over Time?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep useful columns
df = df[
    [
        "title",
        "genres",
        "release_date",
        "runtime",
        "budget",
        "revenue",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]

# Convert columns to numeric
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Convert release date
df["release_date"] = pd.to_datetime(
    df["release_date"],
    errors="coerce"
)

# Extract release year
df["release_year"] = df["release_date"].dt.year

# Remove missing values
year_rating = df.dropna(subset=["release_year", "vote_average"])

# Remove movies with very low votes
year_rating = year_rating[year_rating["vote_count"] > 100]

# Calculate average rating by year
year_rating_result = year_rating.groupby("release_year")["vote_average"].mean()

# Print result
print("Average Movie Ratings by Year:")
print(year_rating_result)

# Create line chart
plt.figure(figsize=(12,6))

plt.plot(
    year_rating_result.index,
    year_rating_result.values
)

plt.xlabel("Release Year")
plt.ylabel("Average Rating")
plt.title("Average Movie Ratings Over Time")

plt.tight_layout()

plt.show()

# Which movies generated the highest revenue?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep useful columns
df = df[
    [
        "title",
        "genres",
        "release_date",
        "runtime",
        "budget",
        "revenue",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]

# Convert columns to numeric
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Remove missing revenue values
revenue_df = df.dropna(subset=["title", "revenue"])

# Remove movies with zero revenue
revenue_df = revenue_df[revenue_df["revenue"] > 0]

# Top 10 highest revenue movies
top_revenue_movies = revenue_df.sort_values(
    by="revenue",
    ascending=False
)[["title", "revenue", "vote_average"]].head(10)

# Print results
print("Top 10 Highest Revenue Movies:")
print(top_revenue_movies)

# Create chart
plt.figure(figsize=(10,6))

plt.barh(
    top_revenue_movies["title"],
    top_revenue_movies["revenue"]
)

plt.xlabel("Revenue")
plt.ylabel("Movie Title")
plt.title("Top 10 Highest Revenue Movies")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()

# Can We Predict Movie Success Using Machine Learning?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv(
    r"C:\Users\fahim\OneDrive\Desktop\IMDb_Movie_Success_Analytics\data\movies_metadata.csv",
    low_memory=False
)

# Keep only important columns
df = df[
    [
        "runtime",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]

# Convert to numbers
df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce")

# Remove missing values
df = df.dropna()

# Use smaller sample for faster training
df = df.sample(5000, random_state=42)

# Create target variable
df["successful"] = df["vote_average"].apply(
    lambda x: 1 if x >= 7 else 0
)

# Features
X = df[
    [
        "runtime",
        "popularity",
        "vote_count"
    ]
]

# Target
y = df["successful"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:")
print(accuracy)
