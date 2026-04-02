import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/sumerafaisal/BI_proj_1/retail.db')

query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, conn)
print(tables)

query = """
SELECT 
    CustomerID,
    julianday('2011-12-10') - julianday(MAX(InvoiceDate)) AS recency,
    COUNT(DISTINCT InvoiceNo) AS frequency,
    SUM(TotalPrice) AS monetary
FROM transactions
GROUP BY CustomerID
"""

rfm_df = pd.read_sql(query, conn)
rfm_df.sort_values(by='monetary', ascending=False).head()
rfm_df.sort_values(by='recency', ascending=True).head()
rfm_df.sort_values(by='frequency', ascending=False).head()
print("Top by Monetary:")
print(rfm_df.sort_values(by='monetary', ascending=False).head())

print("\nTop by Recency:")
print(rfm_df.sort_values(by='recency', ascending=True).head())

print("\nTop by Frequency:")
print(rfm_df.sort_values(by='frequency', ascending=False).head())

rfm_df.sort_values(by='monetary', ascending=False).head()
print(rfm_df.describe())

print(rfm_df['CustomerID'].nunique())
print(len(rfm_df))