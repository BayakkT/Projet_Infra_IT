from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- ROUTE 1 : ACCUEIL ---
@app.route('/')
def index():
    conn = get_db_connection()
    livres = conn.execute('SELECT * FROM livres').fetchall()
    conn.close()
    
    html = "<h1>📚 Ma Bibliothèque</h1>"
    # Lien vers l'admin
    html += "<p><a href='/admin'>➕ Ajouter un livre (Admin)</a> | <a href='/recherche'>🔍 Rechercher</a></p>"
    
    html += "<ul>"
    for livre in livres:
        html += f"<li><b>{livre['titre']}</b> ({livre['auteur']}) "
        if livre['stock'] > 0:
            html += f"✅ Stock: {livre['stock']} <a href='/emprunter/{livre['id']}' style='color:green;'>[EMPRUNTER]</a>"
        else:
            html += "❌ <span style='color:red'>Rupture</span>"
        html += "</li><br>"
    html += "</ul>"
    return html

# --- ROUTE 2 : EMPRUNTER ---
@app.route('/emprunter/<int:id_livre>')
def emprunter(id_livre):
    conn = get_db_connection()
    livre = conn.execute('SELECT stock FROM livres WHERE id = ?', (id_livre,)).fetchone()
    if livre and livre['stock'] > 0:
        conn.execute('UPDATE livres SET stock = stock - 1 WHERE id = ?', (id_livre,))
        conn.execute('INSERT INTO emprunts (livre_id, emprunteur) VALUES (?, ?)', (id_livre, 'Invité'))
        conn.commit()
    conn.close()
    return redirect('/')

# --- ROUTE 3 : RECHERCHE ---
@app.route('/recherche')
def recherche():
    query = request.args.get('q')
    html = "<h1>🔍 Recherche</h1><form><input name='q'><input type='submit' value='Chercher'></form><p><a href='/'>🏠 Accueil</a></p>"
    if query:
        conn = get_db_connection()
        livres = conn.execute('SELECT * FROM livres WHERE titre LIKE ?', ('%' + query + '%',)).fetchall()
        conn.close()
        html += "<ul>"
        for livre in livres:
            html += f"<li>{livre['titre']} ({livre['stock']} dispo)</li>"
        html += "</ul>"
    return html

# --- ROUTE 4 : ADMIN (AJOUTER UN LIVRE) ---
@app.route('/admin', methods=('GET', 'POST'))
def admin():
    # Protection simple (On pourrait remettre le Basic Auth ici)
    
    if request.method == 'POST':
        # On récupère les données du formulaire
        titre = request.form['titre']
        auteur = request.form['auteur']
        stock = request.form['stock']

        if titre and auteur:
            conn = get_db_connection()
            conn.execute('INSERT INTO livres (titre, auteur, stock) VALUES (?, ?, ?)',
                         (titre, auteur, stock))
            conn.commit()
            conn.close()
            return redirect('/')

    # Affichage du formulaire
    html = "<h1>➕ Ajouter un livre</h1>"
    html += "<form method='post'>"
    html += "Titre : <br><input type='text' name='titre'><br>"
    html += "Auteur : <br><input type='text' name='auteur'><br>"
    html += "Stock : <br><input type='number' name='stock' value='1'><br><br>"
    html += "<input type='submit' value='Enregistrer le livre'>"
    html += "</form>"
    html += "<p><a href='/'>🏠 Retour Accueil</a></p>"
    return html
