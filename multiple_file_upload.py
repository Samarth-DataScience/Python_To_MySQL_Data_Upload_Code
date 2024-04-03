import os
from sqlalchemy import create_engine
import pandas as pd

# Define the connection parameters
db_user = 'root'  # Replace 'root' with your MySQL username
db_pass = '123'  # Replace '123' with your MySQL password
db_host = 'localhost'
db_name = 'zomato'

# Create a connection to the MySQL database
engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}')

# Check if the connection was successful
if engine.connect():
    print("Connection to MySQL database established.")
else:
    print("Connection to MySQL database failed.")

# List of file paths
file_paths = [
    r"file_path",
    r"file_path",
    r"file_path",
    r"file_path",
    r"file_path",
    r"file_path",
    r"file_path"
]

# Loop through each file path
for file_path in file_paths:
    print(f"Processing file: {file_path}")
    # Extract table name from file path
    table_name = os.path.splitext(os.path.basename(file_path))[0]
    print(f"Table name: {table_name}")

    # Read the data from the CSV file into a pandas dataframe, delimiter value can vary (; , etc.)
    data = pd.read_csv(file_path, delimiter=',', encoding_errors='ignore')
    print("Data read successfully.")

    # Insert the data into a new table in the MySQL database
    data.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data uploaded to MySQL table: {table_name}")

# Close the database connection
engine.dispose()
print("Connection to MySQL database closed.")
