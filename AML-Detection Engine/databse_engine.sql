
-- -- PROJECT: Dynamic AML & Structuring Detection Engine
-- step 1: create database and table for bank data
-- CREATE DATABASE  ledger_vault;
-- USE ledger_vault;

-- CREATE TABLE banking_transactions (
--     transaction_id VARCHAR(50),
--     account_id VARCHAR(50),
--     transaction_type VARCHAR(20),
--     amount DECIMAL(15,2),
--     channel VARCHAR(20),
--     device_id VARCHAR(50), -- MATCHES YOUR SIMPLE PYTHON COLUMN NAME
--     z_score DECIMAL(10,4)
-- );

-- step 2: unlock server speed settings and load csv file directly
USE ledger_vault;
-- SET GLOBAL local_infile = 1;

 LOAD DATA LOCAL INFILE 'C:/Users/VICTUS/OneDrive/AML-Detection Engine/aml_engine_final_output.csv'
 INTO TABLE banking_transactions
 FIELDS TERMINATED BY ',' 
 OPTIONALLY ENCLOSED BY '"'
 LINES TERMINATED BY '\n'
 IGNORE 1 ROWS;

-- -- step 3: run the multi-account verification check using the new safety range
SELECT 
    device_id AS phone_threat_id,
    COUNT(DISTINCT account_id) AS total_mule_accounts_used,
    COUNT(transaction_id) AS total_structuring_violations,
    ROUND(SUM(amount), 2) AS total_laundered_volume,
    GROUP_CONCAT(DISTINCT channel ORDER BY channel SEPARATOR ', ') AS targeted_banking_channels
FROM banking_transactions
WHERE amount BETWEEN 45000 AND 50000
GROUP BY device_id
HAVING total_structuring_violations >= 5
ORDER BY total_structuring_violations DESC;


