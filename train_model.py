# train_model.py
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("US-energy-dataset.csv")

# Remove missing values
df.dropna(inplace=True)

# Create date field for future use, but exclude from training
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
df.drop(['Year', 'Month'], axis=1, inplace=True)

# Encode categorical 'Sector'
le = LabelEncoder()
df['Sector'] = le.fit_transform(df['Sector'])

# Split data
X = df.drop(['Total Renewable Energy', 'Date'], axis=1)  # <-- Drop Date
y = df['Total Renewable Energy']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
r2 = r2_score(y_test, preds)

print(f"Model trained. R²: {r2:.2f}, RMSE: {rmse:.2f}")

# Save model and label encoder
joblib.dump(model, 'total_renewable_model.pkl')
joblib.dump(le, 'sector_encoder.pkl')
