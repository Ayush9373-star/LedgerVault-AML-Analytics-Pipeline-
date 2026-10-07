# generate_data.py
import pandas as pd
import numpy as np

print("Generating 1,000,000 normal customer rows...")
# Create a standard 1-million-row base table instantly using fast random ranges
df_normal = pd.DataFrame({
    'transaction_id': [f'TXN-N-{i}' for i in range(1000000)],
    'account_id': [f'ACC-{np.random.randint(100, 999)}' for _ in range(1000000)],
    'transaction_type': 'DEPOSIT',
    'amount': np.round(np.random.uniform(500, 40000), 2),
    'channel': 'UPI-HDFC',
    'device_id': 'DEV-NORMAL'
})

print("Injecting the 210 smart fraud rows...")
# Create a small fraud block where 210 different account IDs share 1 bad phone ID
df_fraud = pd.DataFrame({
    'transaction_id': [f'TXN-AML-{i}' for i in range(210)],
    'account_id': [f'ACC-MULE-{i}' for i in range(210)], # 210 different accounts
    'transaction_type': 'DEPOSIT',
    'amount': np.round(np.random.uniform(45000, 50000), 2), # Smart range matching your logic
    'channel': 'UPI-MULE',
    'device_id': 'DEV-PHONE-9999' # The single phone linking them all!
})

# Glue the normal data and fraud data together into your single master file
df_final = pd.concat([df_normal, df_fraud], ignore_index=True)
df_final.to_csv("aml_raw_transactions.csv", index=False)
print("SUCCESS: 1,000,210 rows created cleanly!")
