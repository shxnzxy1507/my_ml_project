# save_model.py
import joblib
from sklearn.linear_model import LinearRegression

# Load the trained model
model = LinearRegression()  # Initialize the model if necessary
model = joblib.load('my_trained_model.joblib')

# Save the model to a file in the src folder within the my_ml_project directory
model_filename = 'my_trained_model.joblib'
model_filepath = f'my_ml_project/src/{model_filename}'
joblib.dump(model, model_filepath)

print(f'Model saved locally: {model_filepath}')




