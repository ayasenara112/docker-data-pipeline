# Containerized Data Pipeline using Docker

## Overview
This project demonstrates a simple yet practical end-to-end data pipeline built using Docker, Python, and PostgreSQL.

The pipeline extracts data from a CSV file, performs data cleaning and transformation, and loads the processed data into a PostgreSQL database.

---

## Architecture

CSV File → Python ETL → PostgreSQL (Dockerized)

- Extract: Read raw data from CSV  
- Transform: Clean and enrich data using Pandas  
- Load: Store processed data in PostgreSQL  

---

## Tech Stack

- Python (Pandas, SQLAlchemy)
- PostgreSQL
- Docker
- Docker Compose

---

## Project Structure

```
docker-data-pipeline/
│
├── data/
│   └── sales.csv
│
├── etl/
│   ├── etl.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## How It Works

1. Docker Compose starts two services:
   - PostgreSQL database
   - ETL container

2. The ETL script:
   - Reads the CSV file
   - Removes duplicates and null values
   - Converts data types
   - Creates a new column (total_amount)
   - Loads the cleaned data into PostgreSQL

---

## Running the Project

Make sure Docker is installed, then run:

```bash
docker compose up --build
```

---

## Verifying the Data

To access PostgreSQL:

```bash
docker exec -it postgres_db psql -U aya -d sales_db
```

Then run:

```sql
SELECT * FROM sales;
```

---

## Data Persistence

Docker volumes are used to ensure that database data is preserved even if containers are stopped or removed.

---

## Key Features

- End-to-end ETL pipeline
- Containerized environment using Docker
- Automated data processing
- Persistent database storage using volumes

---

## Skills Demonstrated

- Data Engineering Fundamentals
- ETL Pipeline Development
- Docker & Containerization
- Database Integration
- Data Cleaning and Transformation

---

## Future Improvements

- Add workflow orchestration using Apache Airflow
- Implement logging and monitoring
- Add data validation checks
- Extend pipeline to support multiple data sources

---

## Author

Aya Gamal  
Data Engineer
