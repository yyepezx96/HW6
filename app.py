# app.py
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the value of the environment variable
my_var = os.getenv("MY_ENV_VAR")

# Print the value (you should see 'example_value' if you've set it in the .env file)
print(my_var)

import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example log messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

