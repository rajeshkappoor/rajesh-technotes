import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ---------------------------
# Step 1: Create Sample Dataset
# ---------------------------
data = {
    'model': ['Toyota', 'Honda', 'Ford', 'Toyota', 'BMW', 'Ford', 'Honda', 'BMW'],
    'year': [2015, 2016, 2014, 2018, 2019, 2013, 2017, 2020],
    'mileage': [50000, 40000, 60000, 30000, 20000, 70000, 35000, 15000],
    'price': [12000, 13000, 10000, 15000, 30000, 9000, 14000, 35000]
}

df = pd.DataFrame(data)
print("Sample Data:")
print(df.head())

# ---------------------------
# Step 2: Define Features & Target
# ---------------------------
X = df[['model', 'year', 'mileage']]  # features
y = df['price']  # target

# ---------------------------
# Step 3: Preprocessing
# ---------------------------
categorical_features = ['model']
numeric_features = ['year', 'mileage']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features),
        ('num', StandardScaler(), numeric_features)
    ]
)

# ---------------------------
# Step 4: Build Pipeline (Preprocessing + Model)
# ---------------------------
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# ---------------------------
# Step 5: Train-Test Split
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------
# Step 6: Train Model
# ---------------------------
# model.fit(X_train, y_train)
model.fit(X, y)
# ---------------------------
# Step 7: Evaluate Model
# ---------------------------
y_pred = model.predict(X_test)
print("\nPredictions:", y_pred)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# ---------------------------
# Step 8: Predict for New Data
# ---------------------------
new_car = pd.DataFrame({
    'model': ['Toyota'],
    'year': [2015],
    'mileage': [50000]
})

print("\nNew Car Data:", new_car)
predicted_price = model.predict(new_car)
print("\nPredicted Price for new car:", predicted_price[0])
