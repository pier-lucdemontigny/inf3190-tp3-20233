# INF3190 travail pratique 3 Automne 2023

## Identification

- Andoulsi, Firas (ANDF79070105)
- De Montigny, Pier Luc (DEMP64110106)

## Comment installer et exécuter le projet

### Étape 1
Confirmer que Flask, Python 3 et pip3 sont installés en fesant les commandes suivantes dans le terminal :
```sh
$ python3 --version
$ pip3 --version
$ flask --version
```

Si un de ses modules ne sont pas installés, il peut être installé en fesant une des commandes suivantes dans le terminal :
```sh
$ sudo apt install python3
$ sudo apt install python3-pip
$ pip3 install Flask
```

### Étape 2
Après avoir décompresser le dossier, ouvrir le terminal à l'interieur de celui-ci est faire les commandes suivantes :
```sh
$ export FLASK_APP=index.py
$ FLASK_APP=index.py flask run
```

### Étape 3
Ouvrir le navigateur en suivant le lien inscrit dans le terminal afin d'accéder au site :
```sh
http://127.0.0.1:5000
```