from typing import List
import sqlite3 as sql

def fetch_all_tables(cursor: sql.Cursor) -> List[str]:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

conn = sql.connect('S1.05.db')
cursor = conn.cursor()
tables = fetch_all_tables(cursor)

for table in tables:
    cursor.execute(f"SELECT count(*) FROM {table}")
    rows = cursor.fetchall()
    print(f'Table: {table}')
    for row in rows:
        print(row)
    print()

conn.close()