pour lancer l'application il faut lancer l'environnement virtuel
source venv/bin/activate
ensuite il faut installer les librairies suivantes
pip install requests
pip install flask_table
pip install Flask-WTF
pip install apscheduler
pip install flask-json-schema
pip install SQLAlchemy
pip install flask_sqlalchemy
pip install Flask
pip install dateparser

ensuite
export FLASK_APP=main.py
et finalement on lance l'application avec
flask run
