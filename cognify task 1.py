import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("reviews.csv")

# 1. Distribution of aggregate ratings
rating_counts = df["Aggregate rating"].value_counts().sort_index()
print("Distribution of Ratings:")
print(rating_counts)
print()

# 2. Most common rating range
most_common_rating = rating_counts.idxmax()
print("Most Common Rating:", most_common_rating)
print()

# 3. Average number of votes
average_votes = df["Votes"].mean()
print("Average Number of Votes:", average_votes)
print()
