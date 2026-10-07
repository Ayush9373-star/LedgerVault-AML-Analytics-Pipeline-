# 🛡️ LedgerVault: Enterprise Risk Intelligence & AML Monitor

Welcome to **LedgerVault**, an end-to-end financial crime analytics pipeline and data product that I engineered from the ground up. This system is designed to parse massive transaction arrays, calculate behavioral anomalies, and expose coordinated structuring attacks and mule account networks natively without any machine learning dependencies.

---

## 📊 Live System Telemetry Desk
Below is the live operational dashboard interface I built for banking compliance teams to investigate active threats:

![LedgerVault Dashboard Telemetry](Ledgervault_AML_Engine.png)

---

## 🛠️ Systems Architecture & Toolkit Stack
I established a connected three-tier data engineering architecture to ensure seamless data flow:

1. **The Ingestion & Analytics Layer (Python):** Developed scripts using `pandas` and `numpy` to profile heavily right-skewed transaction amounts and compute dynamic statistical Z-score weights across **1,00,210 active records**.
2. **The Data Warehouse Layer (MySQL Server):** Created a local relational database instance (`localhost:3306`) optimized with specialized schema tables and high-speed `LOAD DATA LOCAL INFILE` bulk extraction buffers.
3. **The Intelligence Presentation Layer (Power BI):** Engineered an executive dark-themed monitoring canvas running custom DAX formulas to display risk capital exposures in real-time.

---

## 💡 Core Strategic Insights & Fraud Interception
By running analytical window aggregations, my pipeline successfully detected these critical financial patterns:
- **Total Ledger Footprint Scanned:** 1,00,210 live banking rows.
- **Capital Under Active Fraud Threat:** **9.89M** in exposure caught inside the high-risk statistical corridor (Z ≥ 3.0).
- **Suspect Hardware Footprint Target:** Isolated a high-velocity physical device (**`DEV-PHONE-9999`**) controlling **210 distinct mule accounts** within a compressed structuring window.

---

## 🔢 Enterprise DAX Logic Implemented
To power the summary metric cards dynamically, I wrote and configured these precise formulas inside the BI model:
- **Total Fraud Volume Accumulation:**
  ```dax
  Total_Fraud_Volume = CALCULATE(SUM('ledger_vault banking_transactions'[amount]), 'ledger_vault banking_transactions'[z_score] >= 3.0)
  ```
- **High-Risk Device Alert Counter:**
  ```dax
  High_Risk_Device_Count = CALCULATE(DISTINCTCOUNT('ledger_vault banking_transactions'[device_id]), 'ledger_vault banking_transactions'[amount] >= 45000 && 'ledger_vault banking_transactions'[amount] <= 50000)
  ```

---

## 🏃‍♂️ How to Run the Pipeline Local Instance
1. Initialize the database schema configurations using the `databse_engine.sql` script inside MySQL Workbench.
2. Trigger the automated data processing pipeline via `pipeline_trigger.py` to calculate raw scores.
3. Open `Ledgervault_AML_Engine.pbix` inside Power BI Desktop, enter credentials for your root database port, and click **Refresh** to sync the visual layers instantly.
