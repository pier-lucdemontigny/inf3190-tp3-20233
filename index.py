# Copyright 2023 <Votre nom et code permanent>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from flask import render_template
from flask import g
from flask import request
import random
from .database import Database
import sqlite3
from werkzeug.exceptions import BadRequest
import re


app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@app.route('/')
def index():
    db = get_db()
    liste_animaux = db.get_animaux()
    animaux = random.choices(liste_animaux, k=5)
    return render_template('index.html', animaux=animaux)

@app.route('/animal/<id>')
def animal(id):
    db = get_db()
    animal = db.get_animal(id)
    return render_template('infos.html',animal = animal)

@app.route('/formulaire-adoption')
def form():
    return render_template('form.html')



@app.route('/formulaire-soumis', methods=['POST'])
def submit_form():
    nom = request.form.get('nom')
    espece = request.form.get('espece')
    race = request.form.get('race')
    age = request.form.get('age')
    description = request.form.get('description')
    courriel = request.form.get('courriel')
    adresse = request.form.get('adresse')
    ville = request.form.get('ville')
    cp = request.form.get('cp')

    # Validation form niveau backend
    if not nom or not espece or not race or not age or not description or not courriel or not adresse or not ville or not cp:
        raise BadRequest("Tout les champs sont requis")
    if ',' in nom or ',' in espece or ',' in race or ',' in age or ',' in description or ',' in courriel or ',' in adresse or ',' in ville or ',' in cp:
        raise BadRequest("Les champs ne peuvent pas contenir de virgules")
    if not nom.isalpha() or not espece.isalpha() or not race.isalpha() or not ville.isalpha():
        raise BadRequest("Nom, Espèce, Race, and Ville ne doivent pas contenir de chiffres")
    if not age.isdigit() or int(age) < 0 or int(age) > 30:
        raise BadRequest("Age doit être une valeur numérique entre 0 et 30.")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", courriel):
        raise BadRequest("Courriel invalide")
    if not re.match(r"^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$", cp):
        raise BadRequest("Le code postal doit avoir un format canadien.")

    # Ajout des données a la BD
    conn = sqlite3.connect('db/animaux.db')
    cursor = conn.cursor()

    query = """
        INSERT INTO animaux (nom, espece, race, age, description, courriel, adresse, ville, cp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (nom, espece, race, age, description, courriel, adresse, ville, cp))
    conn.commit()
    conn.close()

    return render_template('animal.html', nom=nom, espece=espece, race=race, age=age, description=description, courriel=courriel, adresse=adresse, ville=ville, cp=cp), 200


def recherche_animal(query):
    conn = sqlite3.connect('db/animaux.db')
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animaux WHERE nom LIKE ?", ('%' + query + '%',))
    resultats = [dict(row) for row in cursor.fetchall()]  
    conn.close()
    return resultats

@app.route('/resultats_recherche')
def search():
    query = request.args.get('q')
    if not query:
        abort(404)
    resultats = recherche_animal(query)
    return render_template('resultats.html', resultats=resultats)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404