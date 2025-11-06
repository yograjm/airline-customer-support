import pandas as pd
import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'host': 'localhost',         # your database host ip address
    'port': '5432',              # default PostgreSQL port
    'user': 'postgres',          # a user within Postgres
    'password': 'mypassword',    # password to access DB
    'dbname': 'airlinedb',       # Database name
}


# Read the CSV file
data = pd.read_csv('Flights_Schedule.csv')


# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Read existing data from the table
#        query = "SELECT * FROM titanic;"  # SQL query to select all data from the table
#        cursor.execute(query)


    # Fetch all results
#    rows = cursor.fetchall()
    # Get column names from the cursor
#    column_names = [desc[0] for desc in cursor.description]
    # Create a DataFrame from the fetched data
#    df = pd.DataFrame(rows, columns=column_names)
#    print(f"Existing rows in db: {len(df)}")
    # Display the DataFrame
    #print(df)

    # Next Row to add to db
#    curr_rows = len(df)
#    if curr_rows >= len(data):
#        curr_rows = curr_rows - len(data)
    # Insert data into the passengers table
    #row_to_add = data.iloc[[curr_rows], :]     # add row one-by-one
    #row_to_add = data.iloc[curr_rows:]        # add all rows at once
    # print(row_to_add)
    #count = 0
    for index, row in data.iterrows():
        cursor.execute(
            sql.SQL("""
                INSERT INTO flights (
                    id, flight_no, airline_code, airline_name,
                    origin, destination, departure_scheduled, arrival_scheduled,
                    status, delay_minutes, delay_reason,
                    terminal, gate, aircraft_type,
                    seats_total, seats_booked, fare_inr
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """),
            (
                row["id"],
                row["flight_no"],
                row["airline_code"],
                row["airline_name"],
                row["origin"],
                row["destination"],
                row["departure_scheduled"],
                row["arrival_scheduled"],
                row["status"],
                row["delay_minutes"],
                row["delay_reason"],
                row["terminal"],
                row["gate"],
                row["aircraft_type"],
                row["seats_total"],
                row["seats_booked"],
                row["fare_inr"]
            )
        )

    # Commit the transaction
    conn.commit()
    print(f"\nData inserted successfully.\n")


except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()

