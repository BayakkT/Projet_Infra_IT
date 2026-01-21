import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# On insère quelques livres pour commencer
cur.execute("INSERT INTO livres (titre, auteur, stock) VALUES (?, ?, ?)",
            ('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 3))

cur.execute("INSERT INTO livres (titre, auteur, stock) VALUES (?, ?, ?)",
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', 5))

cur.execute("INSERT INTO livres (titre, auteur, stock) VALUES (?, ?, ?)",
            ('1984', 'George Orwell', 2))

connection.commit()
connection.close()
