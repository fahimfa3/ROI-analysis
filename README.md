## Project Overview
This project analyzes transactional retail data to identify high-value customers, revenue concentration, and purchasing patterns to support data-driven marketing and customer retention strategies. Using RFM (Recency, Frequency, Monetary) analysis, the project segments customers into behavioral groups and provides actionable business insights.

## Data Overview 
This project uses a publicly available dataset from the UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/352/online+retail

The dataset contains all transactions from a UK-based online retail company between December 1, 2010 and December 9, 2011 and includes the following information:

| Field | Description |
|-------|-------------|
| Customer ID | Unique customer identifier |
| Invoice Number | Transaction identifier |
| Product Code & Description | Item details |
| Quantity | Units purchased per item |
| Invoice Date | Transaction date |
| Unit Price | Price per unit |
| Customer Country | Geographic location |

Each row represents a single product within a transaction, meaning multiple rows may 
correspond to a single purchase. The dataset notes that a portion of customers are 
wholesalers, however, no explicit labels are provided. Customer types are therefore 
inferred from purchasing behavior rather than predefined categories.

## Project Goals
- Segment customers using RFM analysis  
- Identify high-value customer groups and revenue concentration patterns  
- Analyze purchasing behavior across segments to inform targeted marketing strategies  
- Generate actionable insights to support customer retention and business decision-making  

## Methodology
1. Data cleaning and preprocessing (handling missing Customer IDs, negative quantities, 
   and zero-price entries). 
2. Loading cleaned data into SQLite for aggregation of transaction-level data into 
   customer-level RFM metrics.
3. Exploratory data analysis to identify distributional skew and validate the need for 
   segmentation.
4. RFM scoring using quintile-based ranking across Recency, Frequency, and Monetary 
   dimensions.
5. Customer segmentation using composite RFM score thresholds.
6. Visualization and interpretation of segment-level behavioral differences.

## Key Insights
- High-value customers represent 29% of the customer base but generate 76% of total revenue.
- Low-value customers (39% of the base) account for just 7% of revenue, with many likely 
  being one-time buyers averaging 170 days since their last purchase.
- Mid-value customers show recent purchasing behavior (avg. 64 days) and moderate 
  frequency, representing the strongest conversion opportunity.
- Revenue and frequency distributions are heavily right-skewed, consistent with the 
  presence of wholesale buyers in the dataset.

## Tools Used
- Python (Pandas, NumPy)
- SQLite
- Data Visualization (Matplotlib / Seaborn)
- Jupyter Notebook

## Author
Farishtay Fahim
