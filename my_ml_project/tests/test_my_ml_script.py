import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.my_ml_script import my_ml_function

def test_my_ml_function():
    # Assuming my_ml_function takes input X and returns predictions
    X = [[1], [2], [3]]
    predictions = my_ml_function(X)

    # Add assertions to check if the function produces the expected results
    assert len(predictions) == len(X)



