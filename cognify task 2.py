import pandas as pd

# Load dataset
df = pd.read_csv("reviews.csv")

# 1. Finding the most common cuisine combinations
cuisine_counts = df["Cuisines"].value_counts().head(10)
print("Most Common Cuisine Combinations:")
print(cuisine_counts)
print()

# 2. Checking if some cuisine combinations have higher ratings
avg_rating_by_cuisine = df.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)

print("Cuisine Combinations with Highest Average Ratings:")
print(avg_rating_by_cuisine.head(10))
print()

print("Cuisine Combinations with Lowest Average Ratings:")
print(avg_rating_by_cuisine.tail(10))

