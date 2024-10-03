import os

# Define the path to the static files
STATIC_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')

# Ensure the static directory exists
os.makedirs(STATIC_PATH, exist_ok=True)
