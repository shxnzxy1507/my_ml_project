# save_model.py
import joblib
import boto3
from sklearn.linear_model import LinearRegression

# Load the trained model
model = LinearRegression()  # Initialize the model if necessary
model = joblib.load('my_trained_model.joblib')

# Save the model to a file
model_filename = 'my_trained_model.joblib'
joblib.dump(model, model_filename)

# Upload the model to an AWS S3 bucket
bucket_name = 'jenkinsbucketalnafiprac'
s3_key = 'models/my_trained_model.joblib'  # Adjust the path and filename as needed

# AWS S3 credentials and region
aws_access_key_id = 'AKIAYZENMCSI3FMAMT4T'
aws_secret_access_key = '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'
aws_region = 'eu-north-1'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Upload the file
s3.upload_file(model_filename, bucket_name, s3_key)

print(f'Model uploaded to S3 bucket: {bucket_name}/{s3_key}')


