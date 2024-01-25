import os
import joblib
from sklearn.linear_model import LinearRegression

#print the current directory
print("Current working directory is:", os.getcwd())
# Load the trained model
model = LinearRegression()
model = joblib.load('my_trained_model.joblib')

# Save the model to an explicit path
model_filename = 'my_trained_model.joblib'
joblib.dump(model, model_filename)

print(f'Model saved locally: {model_filename}')






