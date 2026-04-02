## Project Overview
This project analyzes transactional retail data to identify high-value customers, revenue concentration, and purchasing patterns to support data-driven marketing and customer retention strategies. Using customer segmentation techniques, the analysis aims to uncover behavioral differences across customer groups and provide actionable business insights.

## Data Overview 
This project uses a publicly available dataset from the UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/352/online+retail

The dataset contains all transactions from a UK-based online retail company between December 1, 2010 and December 9, 2011.

The dataset includes:
- Customer ID
- Invoice Number
- Product Code and Description
- Quantity per transaction
- Invoice Date
- Unit Price
- Customer Country

Each row represents a single product within a transaction, meaning multiple rows may correspond to a single purchase.

The dataset notes that a portion of customers are wholesalers; however, no explicit labels are provided. As a result, customer types are inferred based on purchasing behavior (e.g., high frequency and high monetary value), rather than predefined categories.

## Project Goals
- Segment customers using RFM (Recency, Frequency, Monetary) analysis  
- Identify high-value customer groups and revenue concentration patterns  
- Analyze purchasing behavior across segments to inform targeted marketing strategies  
- Generate actionable insights to support customer retention and business decision-making  

## Methodology
- Data cleaning and preprocessing (handling missing Customer IDs, cancellations, and anomalies)  
- Aggregation of transaction-level data to customer-level metrics  
- Calculation of Recency, Frequency, and Monetary (RFM) values  
- Customer segmentation using RFM scoring  
- Exploratory data analysis to identify trends and behavioral patterns 

## Key Insights (Preliminary)
- A small percentage of customers contribute a disproportionate share of total revenue 
- High-frequency customers tend to have significantly higher lifetime value  
- Distinct behavioral differences exist between high-value and low-value customer segments  

## Tools Used
- Python (Pandas, NumPy)
- Data Visualization (Matplotlib / Seaborn)
- Jupyter Notebook

## Author
Farishtay Fahim