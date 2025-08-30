import joblib
import pandas as pd

# Load the trained model
model = joblib.load('../house_price_model.pkl')

# Example input for prediction
example_data = {
    'crim': [0.1], 'zn': [18.0], 'indus': [2.31], 'chas': [0],
    'nox': [0.538], 'rm': [6.575], 'age': [65.2], 'dis': [4.09],
    'rad': [1], 'tax': [296], 'ptratio': [15.3], 'b': [396.9], 'lstat': [4.98]
}
input_df = pd.DataFrame(example_data)

# Predict
predicted_price = model.predict(input_df)
print("Predicted House Price:", predicted_price[0])
