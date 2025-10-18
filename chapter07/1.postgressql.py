import pandas as pd
import psycopg2
from psycopg2 import sql

def table_exists(cursor, table_name):
    cursor.execute(
        sql.SQL("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)"),
        [table_name]
    )
    return cursor.fetchone()[0]

def create_table(cursor, table_name):
    cursor.execute(
        sql.SQL("""
            CREATE TABLE {} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                age INT
            )
        """).format(sql.Identifier(table_name))
    )

def insert_data(cursor, table_name, data):
    cursor.executemany(
        sql.SQL("INSERT INTO {} (name, age) VALUES (%s, %s)").format(sql.Identifier(table_name)),
        data
    )

def print_table_data(cursor, table_name):
    cursor.execute(
        sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 22]
}

df = pd.DataFrame(data)

db_params = {
    'dbname': 'learn_sql',
    'user': 'the_great_coder',
    'password': 'the_great_coder_again',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

table_name = 'example_table'

if not table_exists(cursor, table_name):
    create_table(cursor, table_name)

insert_data(cursor, table_name, df.values.tolist())

conn.commit()

print_table_data(cursor, table_name)

cursor.close()
conn.close()