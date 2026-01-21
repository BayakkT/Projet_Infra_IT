from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "change_me_please"  # simple pour le projet

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# =========================
# Helpers auth
# =========================
def est_admin():
    return session.get("auth_admin") is True

def est_user():
    return session.get("auth_user") is True


# =========================
# ROUTE 1 : ACCUEIL
# =========================
@app.route('/')
def index():
    conn = get_db_connection()
    livres = conn.execute('SELECT * FROM livres').fetchall()
    conn.close()

    html = "<h1>📚 Ma Bibliothèque</h1>"
    html += "<p>"
    html += "<a href='/admin'>➕ Ajouter un livre (Admin)</a> | "
    html += "<a href='/recherche'>🔍 Rechercher</a> | "
    html += "<a href='/login_user'>👤 Login User</a> | "
    html += "<a href='/login_admin'>🔐 Login Admin</a> | "
    html += "<a href='/logout'>Logout</a>"
    html += "</p>"

    html += "<ul>"
    for livre in livres:
        html += f"<li><b>{livre['titre']}</b> ({livre['auteur']}) "
        if livre['stock'] > 0:
            html += f"✅ Stock: {livre['stock']} <a href='/emprunter/{livre['id']}' style='color:pink;'>[EMPRUNTER]</a>"
        else:
            html += "❌ <span style='color:purple'>Rupture</span>"
        html += "</li><br>"
    html += "</ul>"
    return html


# =========================
# ROUTE 2 : EMPRUNTER (protégé USER)
# =========================
@app.route('/emprunter/<int:id_livre>')
def emprunter(id_livre):
    # protection user/12345
    if not est_user():
        return redirect(url_for("login_user"))

    conn = get_db_connection()
    livre = conn.execute('SELECT stock FROM livres WHERE id = ?', (id_livre,)).fetchone()

    if livre and livre['stock'] > 0:
        conn.execute('UPDATE livres SET stock = stock - 1 WHERE id = ?', (id_livre,))
        conn.execute('INSERT INTO emprunts (livre_id, emprunteur) VALUES (?, ?)', (id_livre, 'User'))
        conn.commit()

    conn.close()
    return redirect('/')


# =========================
# ROUTE 3 : RECHERCHE
# =========================
@app.route('/recherche')
def recherche():
    query = request.args.get('q')
    html = "<h1>🔍 Recherche</h1>"
    html += "<form><input name='q'><input type='submit' value='Chercher'></form>"
    html += "<p><a href='/'>🏠 Accueil</a></p>"

    if query:
        conn = get_db_connection()
        livres = conn.execute('SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ?',
                              ('%' + query + '%', '%' + query + '%')).fetchall()
        conn.close()

        html += "<ul>"
        for livre in livres:
            html += f"<li>{livre['titre']} — {livre['auteur']} ({livre['stock']} dispo)</li>"
        html += "</ul>"
    return html


# =========================
# ROUTE 4 : ADMIN (AJOUTER UN LIVRE) protégé ADMIN
# =========================
@app.route('/admin', methods=('GET', 'POST'))
def admin():
    if not est_admin():
        return redirect(url_for("login_admin"))

    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        stock = request.form['stock']

        if titre and auteur:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO livres (titre, auteur, stock) VALUES (?, ?, ?)',
                (titre, auteur, stock)
            )
            conn.commit()
            conn.close()
            return redirect('/')

    html = "<h1>➕ Ajouter un livre</h1>"
    html += "<form method='post'>"
    html += "Titre : <br><input type='text' name='titre' required><br>"
    html += "Auteur : <br><input type='text' name='auteur' required><br>"
    html += "Stock : <br><input type='number' name='stock' value='1' min='0'><br><br>"
    html += "<input type='submit' value='Enregistrer le livre'>"
    html += "</form>"
    html += "<p><a href='/'>🏠 Retour Accueil</a></p>"
    return html


# =========================
# LOGIN ADMIN (admin/password)
# =========================
@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "password":
            session["auth_admin"] = True
            return redirect(url_for("admin"))
        return render_template("formulaire_authentification.html", error=True, form_action=url_for("login_admin"))

    return render_template("formulaire_authentification.html", error=False, form_action=url_for("login_admin"))


# =========================
# LOGIN USER (user/12345)
# =========================
@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        if request.form["username"] == "user" and request.form["password"] == "12345":
            session["auth_user"] = True
            return redirect(url_for("index"))
        return render_template("formulaire_authentification.html", error=True, form_action=url_for("login_user"))

    return render_template("formulaire_authentification.html", error=False, form_action=url_for("login_user"))


# =========================
# LOGOUT
# =========================
@app.route('/logout')
def logout():
    session.pop("auth_admin", None)
    session.pop("auth_user", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
