# main.py
from snowflake_connection import create_session_object
from snowflake.snowpark.functions import col

# Create a session object
session = create_session_object()

def create_dataframe(session):
    """Creates a dataframe and performs actions and transformations on it."""
    # Create a dataframe by referencing a table in Snowflake
    df_table = session.table("GAME_LOGS")

    #---------------------------------
    # **ACTIONS**
    #---------------------------------

    # Count rows in the dataframe
    count_result = df_table.count()  # This will execute and return the row count
    print(f"Row count: {count_result}")

    # Show first few rows
    df_table.show()

    # Collect the results as a list of Rows (executes the query)
    df_results = df_table.collect()
    print(f"Data collected: {df_results}")  # You can print or iterate over df_results

    #---------------------------------
    # **TRANSFORMATIONS**
    #---------------------------------

    # Filter rows where RAW_LOG > 6000000
    df_filtered = df_table.filter(col("RAW_LOG") > 6000000)

    # Show the filtered dataframe
    df_filtered.show()

    # Collect the filtered dataframe to a list of Rows
    df_filtered_persisted = df_filtered.collect()
    print(f"Filtered data: {df_filtered_persisted}")  # Ensure this prints the collected data

# Run the function to create the dataframe
create_dataframe(session)
