from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' 

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    taches = conn.execute('SELECT * FROM taches ORDER BY est_terminee ASC, id DESC').fetchall()
    conn.close()
    return render_template('index.html', taches=taches)

@app.route('/ajouter', methods=('GET', 'POST'))
def ajouter():
    if request.method == 'POST':
        titre = request.form.get('titre')
        description = request.form.get('description')
        date_echeance = request.form.get('date_echeance')

        # Petite vérification de sécurité
        if not titre:
            # Optionnel : envoyer un message d'alerte à l'utilisateur
            return render_template('ajouter.html', error="Le titre est obligatoire !")

        conn = get_db_connection()
        conn.execute('INSERT INTO taches (titre, description, date_echeance) VALUES (?, ?, ?)',
                     (titre, description, date_echeance))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
            
    return render_template('ajouter.html')

@app.route('/supprimer/<int:id>', methods=('POST',))
def supprimer(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM taches WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/terminer/<int:id>', methods=('POST',))
def terminer(id):
    conn = get_db_connection()
    # On bascule l'état (si c'est 0 ça devient 1, si c'est 1 ça devient 0)
    # C'est plus flexible que de forcer à 1
    conn.execute('UPDATE taches SET est_terminee = 1 - est_terminee WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
