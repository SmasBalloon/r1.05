import csv
import mysql.connector

# Remplacez ces valeurs par les informations de votre base de données distante
db_host = '164.81.120.19'
db_user = 'sauvage36'
db_password = 'Banane24@'
db_name = 'G2B_sauvage_Mathis_s1-05'

try:
    with open('vgsales.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)  # Lire l'en-tête
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()

        # Création de la table
        cursor.execute("""CREATE TABLE IF NOT EXISTS jeux_video (
                    Rank INT PRIMARY KEY,
                    Name VARCHAR(255), 
                    Platform VARCHAR(255), 
                    Year INT, 
                    Genre VARCHAR(255), 
                    Publisher VARCHAR(255), 
                    NA_Sales FLOAT, 
                    EU_Sales FLOAT, 
                    JP_Sales FLOAT, 
                    Other_Sales FLOAT, 
                    Global_Sales FLOAT)
                    """)
        
        # Insertion des données
        for row in reader:
            try:
                if len(row) != 11:
                    print(f"Ligne ignorée (mauvais format) : {row}")
                else:
                    cursor.execute(
                        "INSERT INTO jeux_video VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                        row
                    )
            except mysql.connector.Error as e:
                print(f"Erreur d'insertion pour la ligne {row}: {e}")
        
        # Commit et fermeture
        conn.commit()
        print("Données insérées avec succès.")
    conn.close()

except mysql.connector.Error as e:
    print(f"Erreur de connexion ou SQL : {e}")
except FileNotFoundError:
    print("Le fichier vgsales.csv est introuvable.")
except Exception as e:
    print(f"Erreur inattendue : {e}")
