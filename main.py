import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Get current file directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load dataset safely
file_path = os.path.join(current_dir, "train.csv")
df = pd.read_csv(file_path)

# Select required columns
df = df[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice']]

# Remove missing values
df = df.dropna()

# Features and target
X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = df['SalePrice']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

# USER INPUT
area = float(input("Enter area (sqft): "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))

sample = pd.DataFrame(
    [[area, bedrooms, bathrooms]],
    columns=['GrLivArea', 'BedroomAbvGr', 'FullBath']
)

predicted_price = model.predict(sample)
print("\nPredicted House Price:", predicted_price[0])

# Graph
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
