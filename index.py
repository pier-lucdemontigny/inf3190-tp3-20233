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

# Index, page d'accueil
@app.route('/')
def index():
    db = get_db()
    liste_animaux = db.get_animaux()
    animaux = random.sample(liste_animaux, 5)
    return render_template('index.html', animaux=animaux)

# Page d'informations sur un animale
@app.route('/animal/<id>')
def animal(id):
    db = get_db()
    animal = db.get_animal(id)
    if animal is None:
        return render_template('404.html'), 404
    else:
        return render_template('infos.html',animal = animal)

# Page de formulaire
@app.route('/formulaire-adoption')
def form():
    return render_template('form.html')

# Page de soumision
@app.route('/formulaire-soumis', methods=['POST'])
def soumission_form():
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
    erreurs = []
    if not nom or not espece or not race or not age or not description or not courriel or not adresse or not ville or not cp:
        erreurs.append("Tout les champs sont requis")
    if ',' in nom or ',' in espece or ',' in race or ',' in age or ',' in description or ',' in courriel or ',' in adresse or ',' in ville or ',' in cp:
        erreurs.append("Les champs ne peuvent pas contenir de virgules")
    if len(nom) < 3 or len(nom) > 20:
        erreurs.append("Nom doit être entre 3 et 20 caractères")
    if not nom.isalpha() or not espece.isalpha() or not race.isalpha() or not ville.isalpha():
        erreurs.append("Nom, Espèce, Race, et Ville ne doivent pas contenir de chiffres")
    if not age.isdigit() or int(age) < 0 or int(age) > 30:
        erreurs.append("Age doit être une valeur numérique entre 0 et 30.")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", courriel):
        erreurs.append("Courriel invalide")
    if not re.match(r"^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$", cp):
         erreurs.append("Le code postal doit avoir un format canadien.")
    
    if erreurs:
        return str(erreurs), 400

    # Ajout des données a la BD
    db = get_db()
    lastId = db.add_animal(nom, espece, race, age, description, courriel, adresse, ville, cp)

    animal = db.get_animal(lastId)
    return render_template('animal.html', animal=animal), 200

# Recherche d'un animal
def recherche_animal(query):
    db = get_db()
    resultats = db.get_animaux()
    resultats = [animal for animal in resultats if query.lower() in (animal['nom'].lower() if animal['nom'] else '') or 
                                                       query.lower() in (animal['espece'].lower() if animal['espece'] else '') or 
                                                       query.lower() in (animal['race'].lower() if animal['race'] else '') or 
                                                       query.lower() in (animal['description'].lower() if animal['description'] else '') or 
                                                       query.lower() == (animal['courriel'].lower() if animal['courriel'] else '') or 
                                                       query.lower() == (animal['ville'].lower() if animal['ville'] else '') or
                                                       query.lower() == (animal['cp'].lower() if animal['cp'] else '') or
                                                       query.lower() == (animal['adresse'].lower() if animal['adresse'] else '')]
    return resultats

# Page de resultat de recherche
@app.route('/resultats_recherche')
def recherche():
    query = request.args.get('q')
    resultats = recherche_animal(query)
    return render_template('resultats.html', resultats=resultats)

# Page non trouve (404)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404