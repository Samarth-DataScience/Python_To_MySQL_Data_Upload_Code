import os
from sqlalchemy import create_engine
import pandas as pd

# Define the connection parameters
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_host = 'localhost'
db_name = 'your_database_name'
table_name = 'desired_table_name'
file_path = 'file path and use '/' symbol for address'

# Create a connection to the MySQL database
engine = create_engine(f'mysql://{db_user}:{db_pass}@{db_host}/{db_name}')

# Check if the connection was successful
if engine.connect():
    print("Connection to MySQL database established.")
else:
    print("Connection to MySQL database failed.")

# Read the data from the CSV file into a pandas dataframe
data = pd.read_csv(file_path)

# Insert the data into a new table in the MySQL database
data.to_sql(table_name, engine, if_exists='replace', index=False)

# Close the database connection
engine.dispose()
