# -*- coding: utf-8 -*-
from sqlite3 import dbapi2 as sqlite3
from flask import (
    Flask,
    render_template,
    url_for,
    request,
    flash,
    redirect)

app = Flask(__name__)

def connect_db():
    """Retorna una conexión a la BD"""
    path_to_db = 'entry.db'
    rv = sqlite3.connect(path_to_db)
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    """Crea las tablas y datos de prueba"""
    db = connect_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

@app.route('/')
def base():
    db = connect_db()
    cur = db.execute('SELECT id,latitud ,longitud,description,user FROM entry')
    entries = cur.fetchall()
    cur = db.execute('SELECT distinct user FROM entry order by user desc')
    users = cur.fetchall()
    db.close()
    return render_template('entries.html',entries=entries,users=users)

@app.route('/<username>')
def show_user(username):
    db = connect_db()
    cur = db.execute('SELECT id,latitud ,longitud,description,user FROM entry where user=?',[username])
    entries = cur.fetchall()
    cur = db.execute('SELECT distinct user FROM entry order by user desc')
    users = cur.fetchall()
    db.close()
    return render_template('entries.html',entries=entries,users=users)

@app.route('/new',methods=['POST'])
def new_entry():
    if request.method == 'POST':
        categoria = request.form['categoria']
        description = request.form['descripcion']
        latitud=request.form['latitud']
        longitud=request.form['longitud']
        db = connect_db()
        db.execute(
            'INSERT INTO entry (user, description, latitud,longitud) values (?, ?,?,?)',
            [categoria, description,latitud,longitud])
        db.commit()
        db.close()
        return render_template('new.html')
    else:
        return "Acceso denegado"

@app.route('/delete',methods=['POST'])
def delete():
    if request.method == 'POST':
        ids = request.form['ids']
        db = connect_db()
        db.execute('DELETE FROM entry where id=?',[ids])
        db.commit()
        db.close()
        return render_template('delete.html')
    else:
        return "Acceso denegado"

if __name__ == "__main__":
    app.run(debug=True)