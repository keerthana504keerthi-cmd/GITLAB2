import csv
import random
from datetime import datetime, timedelta

# 1. Define the specific products with metadata and base prices
products = [
    {"id": "P001", "name": "Samsung LED TV", "category": "Electronics", "base_price": 45000},
    {"id": "P002", "name": "LG Washing Machine", "category": "Home Appliances", "base_price": 28000},
    {"id": "P003", "name": "Galaxy Mobile", "category": "Electronics", "base_price": 65000},
    {"id": "P004", "name": "HP Laptop", "category": "Computers", "base_price": 55000},
    {"id": "P005", "name": "Timex Smart Watch", "category": "Wearables", "base_price": 12000}
]

# 2. Setup the date ranges (3 years ending May 31, 2026)
end_date = datetime(2026, 5, 31)
start_date = end_date - timedelta(days=3 * 365)  # Approximately 3 years back

csv_filename = "daily_sales_records.csv"

# 3. Open file and generate structured data
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write CSV Header
    writer.writerow([
        "Date", 
        "Transaction_ID", 
        "Product_ID", 
        "Product_Name", 
        "Category", 
        "Quantity_Sold", 
        "Unit_Price", 
        "Total_Sales"
    ])
    
    current_date = start_date
    tx_counter = 100001
    
    # Loop through every day in the 3-year range
    while current_date <= end_date:
        # Determine a realistic number of sales orders per day (e.g., between 2 to 8 items sold)
        num_transactions = random.randint(2, 8)
        
        # Pick random items from our 5 products to sell on this day
        day_sales = random.choices(products, k=num_transactions)
        
        for prod in day_sales:
            qty = random.randint(1, 3) # Random quantity sold per order
            
            # Apply a minor price variance (+/- 5%) to simulate dynamic pricing/discounts
            price_variance = random.uniform(0.95, 1.05)
            unit_price = round(prod["base_price"] * price_variance, 2)
            total_sales = round(qty * unit_price, 2)
            
            # Write row to CSV
            writer.writerow([
                current_date.strftime("%Y-%m-%d"),
                f"TXN{tx_counter}",
                prod["id"],
                prod["name"],
                prod["category"],
                qty,
                unit_price,
                total_sales
            ])
            tx_counter += 1
            
        # Move to the next day
        current_date += timedelta(days=1)

print(f"Dataset successfully created: '{csv_filename}' containing 3 years of daily sales history.")
