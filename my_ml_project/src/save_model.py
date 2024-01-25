# save_model.py
import joblib
from sklearn.linear_model import LinearRegression

# Load the trained model
model = LinearRegression()  # Initialize the model if necessary
model = joblib.load('my_trained_model.joblib')

# Save the model to a file in the src folder
model_filename = 'src/my_trained_model.joblib'
joblib.dump(model, model_filename)

print(f'Model saved locally: {model_filename}')



