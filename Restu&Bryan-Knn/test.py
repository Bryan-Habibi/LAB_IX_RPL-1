import tkinter as tk
from tkinter import messagebox
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load clean_and_preprocess_data function from clean.py
from cleaning import clean_and_preprocess_data

# Train KNN classifier
def train_knn_classifier():
    # Load preprocessed data
    X_train, X_test, y_train, y_test = clean_and_preprocess_data("wine.csv")
    
    # Train KNN classifier
    k = 3  # K value
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    
    return knn_classifier

# Function to predict wine quality
def predict_quality(knn_classifier):
    try:
        # Get input values
        citric_acid = float(entry_citric_acid.get())
        residual_sugar = float(entry_residual_sugar.get())
        alcohol = float(entry_alcohol.get())
        
        # Preprocess input data
        input_data = [[citric_acid, residual_sugar, alcohol]]
        input_data_scaled = scaler.transform(input_data)
        
        # Predict
        prediction = knn_classifier.predict(input_data_scaled)
        
        # Show prediction
        messagebox.showinfo("Prediction", f"The predicted quality is: {prediction[0]}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for all input fields.")

# Create GUI
root = tk.Tk()
root.title("Wine Quality Prediction")

# Labels
label_citric_acid = tk.Label(root, text="Citric Acid:")
label_citric_acid.grid(row=0, column=0)
label_residual_sugar = tk.Label(root, text="Residual Sugar:")
label_residual_sugar.grid(row=1, column=0)
label_alcohol = tk.Label(root, text="Alcohol:")
label_alcohol.grid(row=2, column=0)

# Entry fields
entry_citric_acid = tk.Entry(root)
entry_citric_acid.grid(row=0, column=1)
entry_residual_sugar = tk.Entry(root)
entry_residual_sugar.grid(row=1, column=1)
entry_alcohol = tk.Entry(root)
entry_alcohol.grid(row=2, column=1)

# Load preprocessed data and scaler
X_train, X_test, y_train, y_test = clean_and_preprocess_data("wine.csv")
scaler = StandardScaler()
scaler.fit(X_train)

# Train KNN classifier
knn_classifier = train_knn_classifier()

# Button
button_predict = tk.Button(root, text="Predict", command=lambda: predict_quality(knn_classifier))
button_predict.grid(row=3, column=0, columnspan=2)

root.mainloop()
