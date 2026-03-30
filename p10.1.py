import pandas as pd

# CSV file read karna
df = pd.read_csv("books.csv")

# a) Complete report
print("----- COMPLETE BOOK DATA -----")
print(df)

# b) Books of a given author
author_name = input("\nEnter author name: ")
print("\n----- BOOKS BY AUTHOR -----")
print(df[df['Author'] == author_name])

# c) Books of a given publisher
publisher_name = input("\nEnter publisher name: ")
print("\n----- BOOKS BY PUBLISHER -----")
print(df[df['Publisher'] == publisher_name])

# d) Cheapest book
print("\n----- CHEAPEST BOOK -----")
print(df[df['Price'] == df['Price'].min()])

# Costliest book
print("\n----- COSTLIEST BOOK -----")
print(df[df['Price'] == df['Price'].max()])

# e) Sort by year
print("\n----- SORTED BY YEAR -----")
print(df.sort_values(by='Year'))