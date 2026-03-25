# 🏠 House Price Prediction using Linear Regression

## 📌 Overview

This project implements a Machine Learning model to predict house prices based on important features such as living area, number of bedrooms, and number of bathrooms.

---

## 🎯 Objective

To build a regression model that can estimate house prices using historical housing data.

---

## 📊 Dataset

* Source: Kaggle (House Prices Dataset)
* Features used:

  * GrLivArea (Living Area in square feet)
  * BedroomAbvGr (Number of bedrooms)
  * FullBath (Number of bathrooms)
* Target:

  * SalePrice (House price)

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---

## 🧠 Model Used

* Linear Regression
* Type: Supervised Learning (Regression)

---

## 🚀 Steps Involved

1. Loaded dataset using Pandas
2. Selected relevant features
3. Cleaned data by removing missing values
4. Split data into training and testing sets
5. Trained Linear Regression model
6. Evaluated model using Mean Absolute Error (MAE)
7. Predicted house prices using user input
8. Visualized results with a graph

---

## 📈 Output

* Model successfully predicts house prices
* Mean Absolute Error ≈ 36,000
* Graph shows actual vs predicted values

---

## 💡 Example

Input:

* Area: 2000 sqft
* Bedrooms: 3
* Bathrooms: 2

Output:

* Predicted Price ≈ 2.4 - 2.5 lakh (dataset scale)

---

## 📂 Project Structure

```id="7e8gac"
house-price-prediction/
│
├── main.py
├── train.csv
└── README.md
```

---

## 🎓 Learning Outcome

* Understanding of Linear Regression
* Data preprocessing techniques
* Model evaluation using MAE
* Basic data visualization

---

## 👤 Author

Bhagyashree Patil
