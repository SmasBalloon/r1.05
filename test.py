import pymysql

conn = None
try:
    conn = pymysql.connect(
        host='164.81.120.19',
        user='sauvage36',
        password='Banane24@',
        database='G2B_sauvage_Mathis_s1-05'
    )
    print("Connexion réussie avec pymysql !")
except pymysql.MySQLError as err:
    print(f"Erreur MySQL avec pymysql : {err}")
finally:
    if conn is not None and conn.open:
        conn.close()
