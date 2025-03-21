# snowflake_connection.py
from snowflake.snowpark.session import Session
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def create_session_object():
    """Creates a Snowflake session object using credentials from environment variables."""
    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": os.getenv("SNOWFLAKE_ROLE"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA"),
    }

    # Create the session object with the provided connection parameters
    session = Session.builder.configs(connection_parameters).create()
    return session
