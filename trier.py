import csv
import sqlite3 as sql

with open('vgsales.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)
    conn = sql.connect('S1.05.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS jeux_video (
                Rank INTEGER PRIMARY KEY,
                Name TEXT, 
                Platform TEXT, 
                Year INTEGER, 
                Genre TEXT, 
                Publisher TEXT, 
                NA_Sales REAL, 
                EU_Sales REAL, 
                JP_Sales REAL, 
                Other_Sales REAL, 
                Global_Sales REAL)
                """)
    for row in reader:
        if len(row) != 11:
            print(f"The CSV file does not have 11 columns \n {row}")
        else: 
            cursor.execute("INSERT INTO jeux_video VALUES (?,?,?,?,?,?,?,?,?,?,?)", row)
    conn.commit()
    conn.close()