# Airline Customer Support System

## Steps to Follow

1. Create a new GitHub repository

2. Start a new GitHub Codespace whithin the GitHub repo

3. Install N8N

4. Create Virtual Environment

5. Activate Virtual Environment & Install LLM-Guard

6. Start Postgres Container

    `docker run -it -d -p 5432:5432 -e POSTGRES_PASSWORD=mypassword --name=postgrescont postgres:latest`

    Make the port 5432 Public.

7. Move into the Postgres Container and Create database and table

    `docker exec -it postgrescont psql -U postgres`

    `SELECT datname FROM pg_database WHERE datistemplate = false;`

    `CREATE DATABASE airlinedb;`

    `\c airlinedb;`

    ```sql
    CREATE TABLE IF NOT EXISTS flights (
        id BIGINT PRIMARY KEY,
        flight_no TEXT NOT NULL,
        airline_code TEXT NOT NULL,
        airline_name TEXT NOT NULL,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        departure_scheduled TIMESTAMP NOT NULL,
        arrival_scheduled TIMESTAMP NOT NULL,
        departure_date DATE GENERATED ALWAYS AS (departure_scheduled::date) STORED,
        departure_time TIME GENERATED ALWAYS AS (departure_scheduled::time) STORED,
        arrival_date   DATE GENERATED ALWAYS AS (arrival_scheduled::date) STORED,
        arrival_time   TIME GENERATED ALWAYS AS (arrival_scheduled::time) STORED,
        status TEXT NOT NULL CHECK (status IN ('On Time','Delayed','Cancelled')),
        delay_minutes INT DEFAULT 0,
        delay_reason TEXT DEFAULT '',
        terminal TEXT,
        gate TEXT,
        aircraft_type TEXT,
        seats_total INT,
        seats_booked INT,
        fare_inr INT
    );
    ```

8. Insert data into Postgres DB using Python script

9. Start N8N within your Virtual Environment



