"""
Food Delivery Data Integration Script
Combines orders.csv, users.json, and restaurants.sql into final_food_delivery_dataset.csv
"""

import pandas as pd
import json
import re

print("=" * 60)
print("Food Delivery Data Integration")
print("=" * 60)

# Step 1: Load Orders CSV
print("\n[Step 1] Loading Orders CSV...")
orders_df = pd.read_csv('orders.csv')
print(f"   -> Orders loaded: {orders_df.shape[0]} records, {orders_df.shape[1]} columns")

# Step 2: Load Users JSON
print("\n[Step 2] Loading Users JSON...")
with open('users.json', 'r') as f:
    users_data = json.load(f)
users_df = pd.DataFrame(users_data)
print(f"   -> Users loaded: {users_df.shape[0]} records, {users_df.shape[1]} columns")

# Step 3: Parse Restaurants SQL
print("\n[Step 3] Loading Restaurants SQL...")

def parse_sql_file(filename):
    """Parse SQL file containing INSERT statements and extract data."""
    restaurants = []
    with open(filename, 'r') as f:
        content = f.read()
    
    # Pattern to match: INSERT INTO restaurants VALUES (id, 'name', 'cuisine', rating);
    pattern = r"INSERT INTO restaurants VALUES \((\d+),\s*'([^']+)',\s*'([^']+)',\s*([\d.]+)\)"
    matches = re.findall(pattern, content)
    
    for match in matches:
        restaurants.append({
            'restaurant_id': int(match[0]),
            'restaurant_name_sql': match[1],
            'cuisine': match[2],
            'rating': float(match[3])
        })
    return pd.DataFrame(restaurants)

restaurants_df = parse_sql_file('restaurants.sql')
print(f"   -> Restaurants loaded: {restaurants_df.shape[0]} records, {restaurants_df.shape[1]} columns")

# Step 4: Merge Data
print("\n[Step 4] Merging Datasets...")
print("   - Joining orders with users on 'user_id'...")
merged_df = orders_df.merge(users_df, on='user_id', how='left')
print(f"   -> After user merge: {merged_df.shape[0]} records")

print("   - Joining with restaurants on 'restaurant_id'...")
final_df = merged_df.merge(restaurants_df, on='restaurant_id', how='left')
print(f"   -> After restaurant merge: {final_df.shape[0]} records")

# Rename columns for clarity
final_df = final_df.rename(columns={
    'name': 'user_name',
    'city': 'user_city'
})

# Step 5: Save Final Dataset
print("\n[Step 5] Saving Final Dataset...")
output_file = 'final_food_delivery_dataset.csv'
final_df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("SUCCESS! FINAL DATASET CREATED!")
print("=" * 60)
print(f"\nOutput File: {output_file}")
print(f"Total Records: {len(final_df)}")
print(f"Total Columns: {len(final_df.columns)}")
print(f"\nColumns in Final Dataset:")
for i, col in enumerate(final_df.columns, 1):
    print(f"   {i}. {col}")

print("\nFirst 5 rows:")
print(final_df.head().to_string())

print("\n" + "=" * 60)
print("Data integration complete!")
print("=" * 60)
