import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="RetailPurchaseDB"
)
print("Database Connected Successfully!")
cursor = db.cursor()

# SQL Query
query = """
SELECT
    ph.Customer_ID,
    ph.Previous_Purchases,
    ph.Purchase_Frequency,
    ph.Average_Spending,
    p.Discount,
    p.Purchase_Amount
FROM Purchase_History ph
JOIN Purchase p
ON ph.Customer_ID = p.Customer_ID
"""
cursor.execute(query)

records = cursor.fetchall()
columns = [
    "Customer_ID",
    "Previous_Purchases",
    "Purchase_Frequency",
    "Average_Spending",
    "Discount",
    "Purchase_Amount"
]
df = pd.DataFrame(records, columns=columns)

print("\nData Used for ML:")
print(df)

# Input variables
X = df[[
        "Previous_Purchases",
        "Purchase_Frequency",
        "Average_Spending",
        "Discount"
    ]]

y = df["Purchase_Amount"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)
print("\nModel Training Completed!")

# Coefficients
print("\nModel Coefficients:")

print("Previous Purchases:",
      round(model.coef_[0], 2))

print("Purchase Frequency:",
      round(model.coef_[1], 2))

print("Average Spending:",
      round(model.coef_[2], 2))

print("Discount:",
      round(model.coef_[3], 2))

# Predict existing data
y_pred = model.predict(X)

# New Customer Prediction
new_customer = pd.DataFrame({
    "Previous_Purchases": [6],
    "Purchase_Frequency": [4],
    "Average_Spending": [7000],
    "Discount": [10]
})

prediction = model.predict(new_customer)

print("\nNew Customer Details:")
print("Previous Purchases: 6")
print("Purchase Frequency: 4")
print("Average Spending: 7000")
print("Discount: 10%")
print("\nPredicted Purchase Amount:",
      round(prediction[0], 2))

# Graph
plt.figure(figsize=(8, 5))
plt.plot(
    range(1, len(y) + 1),y,marker='o',label='Actual Purchase')
plt.plot(
    range(1, len(y_pred) + 1),y_pred,marker='x',linestyle='--',label='Predicted Purchase')
plt.xlabel("Customer Number")
plt.ylabel("Purchase Amount")
plt.title("Retail Purchase Prediction")
plt.legend()
plt.grid(True)

plt.show()
cursor.close()
db.close()
