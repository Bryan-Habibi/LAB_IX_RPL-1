import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

def clean_and_preprocess_data(file_path):
    # Baca data dari file CSV
    df = pd.read_csv(file_path)
    
    selected_columns = ["citric acid", "residual sugar", "alcohol", "quality"]
    data = df[selected_columns]
    
    # Handling missing values (diamputasi)
    imputer = SimpleImputer(strategy='mean')
    data_imputed = imputer.fit_transform(data)
    
    # Split data into features and target
    X = data_imputed[:, :-1]  # Features
    y = data_imputed[:, -1]   # Target
    
    # Split dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scaling (pengubahan skala)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test
