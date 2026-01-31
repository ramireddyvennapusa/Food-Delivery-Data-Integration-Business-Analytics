# Food Delivery Data Integration & Business Analytics

This repository contains a comprehensive data integration and business analytics project for a food delivery service. The project involves merging data from multiple sources (CSV, JSON, SQL), performing extensive data cleaning, and conducting business-oriented analysis.

## 🚀 Project Overview

The primary goal of this project was to integrate disparate datasets from a food delivery platform and answer key business questions to derive actionable insights.

### Data Sources
1.  **`orders.csv`**: Contains order details including order ID, user ID, restaurant ID, total amount, and order date.
2.  **`users.json`**: Contains user demographic data such as name, city, and membership status (Gold/Regular).
3.  **`restaurants.sql`**: A SQL file with INSERT statements containing restaurant names, cuisines, and ratings.

## 🛠️ Data Integration Process

The `create_final_dataset.py` script performs the following steps:
1.  **Loading**: Reads order data from CSV and user data from JSON.
2.  **Parsing**: Uses Regex to extract restaurant data directly from the SQL INSERT statements.
3.  **Merging**: Joins the datasets using `user_id` and `restaurant_id` as keys.
4.  **Cleaning**: Renames columns for clarity (e.g., `user_city`, `user_name`) and handles potential missing values.
5.  **Output**: Generates a consolidated `final_food_delivery_dataset.csv` containing 10,000 order records.

## 📊 Business Analytics & Insights

The analysis was performed using the `food_delivery_analysis.ipynb` notebook and summarized in `analysis_report.txt`. Key findings include:

*   **Top Revenue City (Gold Members)**: Chennai
*   **Highest Average Order Value Cuisine**: Mexican
*   **High-Value Users**: Identified 2,000+ distinct users who spent over ₹1000.
*   **Performance by Rating**: Restaurants in the 4.6–5.0 rating range generate the highest total revenue.
*   **Seasonal Trends**: Q3 (July–September) was identified as the highest revenue quarter.
*   **Membership Insights**: Gold members account for approximately 50% of total orders.

## 📂 Repository Structure

*   `data_integration.ipynb`: Initial exploration and integration logic.
*   `create_final_dataset.py`: Python script for automated data merging.
*   `food_delivery_analysis.ipynb`: Detailed data analysis and visualization.
*   `analysis_report.txt`: Summary of business questions and answers.
*   `final_food_delivery_dataset.csv`: The integrated final dataset.
*   `orders.csv`, `users.json`, `restaurants.sql`: Raw source files.

## 🔧 How to Run

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/ramireddyvennapusa/Food-Delivery-Data-Integration-Business-Analytics.git
    ```
2.  **Install dependencies**:
    ```bash
    pip install pandas
    ```
3.  **Generate the dataset**:
    ```bash
    python create_final_dataset.py
    ```
4.  **Explore the analysis**:
    Open `food_delivery_analysis.ipynb` in Jupyter Notebook or VS Code.

---
**Author**: Rami Reddy Vennapusa
**Date**: January 2026
