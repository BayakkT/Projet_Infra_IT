import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql', encoding='utf-8') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()

print("✅ Base de données tâches créée (database.db)")
