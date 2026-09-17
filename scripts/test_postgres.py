import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="postgres-password",
    database="database_name"
)

print("Connected to PostgreSQL successfully!")

conn.close()