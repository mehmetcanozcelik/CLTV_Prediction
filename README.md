﻿# CLTV (Customer Lifetime Value) Calculation & Prediction

Customer Lifetime Value calculation and prediction analyis by an existing customer dataset with Python. There are 2 different flows, in the first one CLTV calculations are placed by existing values, in the second one Expected Number of Transactions and Expected Profits are predicted for periods by fitting BG&NBD and Gamma&Gamma Sub Model. After predicting those values, CLTV predictions are also placed for all customers.


## Notes for Calculations

**CLTV:** (Customer Value / Churn Rate) x Profit Margin

**Profit Margin:** Profit Margin is ignored in this scenario, if it's used for real time scenario it should not be ignored.

**Customer Value:**  Average Order Value x Purchase Frequency

**Purchase Frequency:** Total Transaction (for grouped by customers) / Total Number of Customers

**Repeat Rate:** Total Number of Customers who has more than 1 Order / Total Number of Customers

**Churn Rate:** 1 - Repeat Rate
