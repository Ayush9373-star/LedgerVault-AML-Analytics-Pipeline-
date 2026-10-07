import pandas as pd
from sqlalchemy import create_engine

# 1. Connect directly to your database
# CRITICAL: Put your real MySQL password here!
# Notice that there is nothing between root: and @localhost
# Change your connection engine line to this:
engine = create_engine("mysql+pymysql://root:ayush@localhost:3306/ledger_vault")



print("Scanning the database for threats...")

# 2. Run your exact SQL verification query
query = """
SELECT device_id, COUNT(DISTINCT account_id) AS total_mules 
FROM banking_transactions 
WHERE amount BETWEEN 45000 AND 50000 
GROUP BY device_id 
HAVING total_mules >= 5;
"""
df_alerts = pd.read_sql(query, engine)

# 3. Print the live alert instantly
if not df_alerts.empty:
    print("\n🚨 ALERT: CRITICAL FRAUD DETECTED!")
    print(df_alerts.to_string(index=False)) # This prints any new fraudster and their accounts automatically!
else:
    print("\nSystem clean. No fraud found.")
