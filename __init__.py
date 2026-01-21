from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Fonction de connexion BDD
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- ROUTE 1 : ACCUEIL (Liste + Bouton Emprunter) ---
@app.route('/')
def index():
    conn = get_db_connection()
    livres = conn.execute('SELECT * FROM livres').fetchall()
    conn.close()
    
    html = "<h1>📚 Ma Bibliothèque</h1>"
    html += "<p><a href='/recherche' style='font-size:1.2em'>🔍 Rechercher un livre</a></p>"
    
    html += "<ul>"
    for livre in livres:
        # On affiche le titre
        html += f"<li><b>{livre['titre']}</b> ({livre['auteur']}) "
        
        # Logique d'affichage du stock
        if livre['stock'] > 0:
            # Si du stock : Bouton vert pour emprunter
            html += f"✅ Dispo: {livre['stock']} "
            html += f"<a href='/emprunter/{livre['id']}' style='color:green; font-weight:bold;'>[EMPRUNTER]</a>"
        else:
            # Pas de stock : Texte rouge
            html += "❌ <span style='color:red'>Rupture de stock</span>"
        
        html += "</li><br>"
    html += "</ul>"
    return html

# --- ROUTE 2 : ACTION EMPRUNTER ---
@app.route('/emprunter/<int:id_livre>')
def emprunter(id_livre):
    conn = get_db_connection()
    
    # 1. On vérifie le stock actuel
    livre = conn.execute('SELECT stock FROM livres WHERE id = ?', (id_livre,)).fetchone()
    
    if livre and livre['stock'] > 0:
        # 2. On baisse le stock de 1
        conn.execute('UPDATE livres SET stock = stock - 1 WHERE id = ?', (id_livre,))
        
        # 3. On enregistre l'emprunt (Ici on met "Invité" par défaut pour simplifier)
        conn.execute('INSERT INTO emprunts (livre_id, emprunteur) VALUES (?, ?)', (id_livre, 'Invité'))
        
        conn.commit()
    
    conn.close()
    # 4. On redirige vers l'accueil pour voir le changement
    return redirect('/')

# --- ROUTE 3 : RECHERCHE ---
@app.route('/recherche')
def recherche():
    query = request.args.get('q')
    html = "<h1>🔍 Recherche de livre</h1>"
    html += "<form><input name='q' placeholder='Titre...'><input type='submit' value='Chercher'></form>"
    html += "<p><a href='/'>🏠 Retour Accueil</a></p>"

    if query:
        conn = get_db_connection()
        livres = conn.execute('SELECT * FROM livres WHERE titre LIKE ?', ('%' + query + '%',)).fetchall()
        conn.close()
        
        html += "<h3>Résultats :</h3><ul>"
        for livre in livres:
            html += f"<li>{livre['titre']} - Stock: {livre['stock']}</li>"
        html += "</ul>"
        
    return html
