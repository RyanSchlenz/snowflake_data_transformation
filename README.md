Snowflake Data Access and Transformation

This project establishes a connection to Snowflake using the Snowpark library and performs data access and transformation tasks. It uses environment variables for credentials, ensuring secure handling of sensitive data. The project fetches data from Snowflake, performs actions like counting rows and filtering data, and applies transformations to create meaningful outputs.

Files in this repository:
snowflake_connection.py - Contains the logic for creating a connection session to Snowflake using credentials stored in environment variables.

main.py - Defines the process for accessing and transforming data from Snowflake, including counting rows, displaying data, filtering results, and printing the transformed data.

Requirements:
Python 3.7+

snowflake-snowpark-python library

python-dotenv for loading environment variables from a .env file

Installation:
Clone this repository:

git clone https://github.com/RyanSchlenz/snowflake_data_transformation.git
cd snowflake-data-access

Install dependencies:
pip install -r requirements.txt
Set up a .env file with your Snowflake credentials:

SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ROLE=your_role
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema

Usage:
Run the main.py script to execute the data access and transformation process:

python main.py

Example Output:

Row count: 100000
+------------+------------+-------------+
| GAME_ID    | PLAYER_ID  | RAW_LOG     |
+------------+------------+-------------+
| 12345      | 6789       | 8000000     |
| 54321      | 9876       | 5000000     |
+------------+------------+-------------+

Filtered data:
[Row(GAME_ID='12345', PLAYER_ID='6789', RAW_LOG=8000000)]
