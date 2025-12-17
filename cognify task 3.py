import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("reviews.csv")

# Removing rows where coordinates are missing
df = df.dropna(subset=["Longitude", "Latitude"])

# 1. Scatter plot of restaurant locations
plt.figure(figsize=(8, 6))
plt.scatter(df["Longitude"], df["Latitude"], s=10)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Locations Based on GPS Coordinates")
plt.show()

# 2. Checking clusters or patterns by city
restaurant_counts = df["City"].value_counts()

print("Number of Restaurants in Each City:")
print(restaurant_counts)
print()

# Optional: Bar chart to show concentration of restaurants
plt.figure(figsize=(10, 6))
restaurant_counts.head(15).plot(kind="bar")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.title("Restaurant Concentration by City")
plt.show()

