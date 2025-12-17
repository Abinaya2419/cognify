import pandas as pd

# Load the dataset
df = pd.read_csv("reviews.csv")

# 1. Identify restaurant chains
# A chain is a restaurant name that appears more than once
chain_counts = df["Restaurant Name"].value_counts()
chains = chain_counts[chain_counts > 1]

print("Restaurant Chains Found in the Dataset:")
print(chains)
print()

# 2. Analyze average rating of chains
chain_ratings = df.groupby("Restaurant Name")["Aggregate rating"].mean()
chain_ratings = chain_ratings.loc[chains.index].sort_values(ascending=False)

print("Average Ratings of Restaurant Chains:")
print(chain_ratings)
print()