# Akim Laberge-Touat
# LABA14059307
#
# https://www.roytuts.com/how-to-download-file-using-python-flask/
#
#
#
# -*- coding: iso-8601-*-

import sqlite3
import datetime
import time
import json
from sqlite3 import OperationalError
from app import app, db
from flask import flash, send_file, render_template, request, redirect
from flask import jsonify
from forms import FormRechercheContrevenants
from tableaux import Resultats
from app.models import Contrevenants
from db_setup import init_db, db_session
from xml_a_db import xml_download
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError
from apscheduler.schedulers.background import BackgroundScheduler
from werkzeug.security import generate_password_hash, check_password_hash

from schemas import utilisateur_schema
from schemas import inspection_schema
from contrevenant import Contrevenant

schema = JsonSchema(app)
init_db()

def toDate(dateString):
    return datetime.datetime.strptime(dateString, "%Y-%m-%d").date()

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def recherche_contrevenants():

    sched = BackgroundScheduler(daemon=True)
    sched.add_job(xml_download,'cron',hour=0, minute=0)
    sched.start()

    recherche = FormRechercheContrevenants(request.form)
    if request.method == 'POST':
        return resultats_recherche(recherche)

    return render_template('recherche_contrevenants.html', form=recherche)


@app.route('/resultats')
def resultats_recherche(recherche):
    resultats = []
    resultats_cherche = recherche.data['recherche']

    if resultats_cherche:
        if recherche.data['selection'] == 'etablissement':
            qry = db_session.query(Contrevenants).filter(
                Contrevenants.etablissement.contains(resultats_cherche))
            resultats = qry.all()
        elif recherche.data['selection'] == 'proprietaire':
            qry = db_session.query(Contrevenants).filter(
                Contrevenants.proprietaire.contains(resultats_cherche))
            resultats = qry.all()
        elif recherche.data['selection'] == 'rue':
            qry = db_session.query(Contrevenants).filter(
                Contrevenants.adresse.contains(resultats_cherche))
            resultats = qry.all()
        else:
            qry = db_session.query(Contrevenants)
            resultats = qry.all()
    else:
        qry = db_session.query(Contrevenants)
        resultats = qry.all()

    if not resultats:
        flash('Aucun resultat trouve!')
        return redirect('/')
    else:
        # afficher resultats
        tableau = Resultats(resultats)
        tableau.border = True
        return render_template('resultats.html', table=tableau)

@app.route('/api/contrevenants', methods= ["GET"])
def recherche_dates():
    resultats = []
    debut = request.args.get('debut')
    fin = request.args.get('fin')
    try:  # Will raise an error if date can't be parsed.
        date_debut = datetime.datetime.strptime(debut,
            "%Y-%m-%d").date()
        date_fin = datetime.datetime.strptime(fin,
            "%Y-%m-%d").date()
        conn = sqlite3.connect('db/contrevenants.db', check_same_thread=False)
        c = conn.cursor()
        c.execute("select * from contrevenant where date_infraction between ? "
                  "and ?",
                  (date_debut, date_fin))
        qry = c.fetchall()
        resultats = [Contrevenant(contrevenant[0], contrevenant[1],
                     contrevenant[2], contrevenant[3], contrevenant[4],
                     contrevenant[5], contrevenant[6], contrevenant[7],
                     contrevenant[8], contrevenant[9])
                     for contrevenant in qry]
        return jsonify([resultat.asDictionary() for resultat in
                       resultats]), 200

    except:
        return debut, 400

@app.route('/api/contrevenants/infractions', methods= ["GET"])
def recherche_infractions():
    resultats = []
    nom_etablissement = request.args.get('nom_etablissement')
    try:
        conn = sqlite3.connect('db/contrevenants.db', check_same_thread=False)
        c = conn.cursor()
        c.execute("select * from contrevenant where etablissement = ?",
        (nom_etablissement,))
        qry = c.fetchall()
        resultats = [Contrevenant(contrevenant[0], contrevenant[1],
                     contrevenant[2], contrevenant[3], contrevenant[4],
                     contrevenant[5], contrevenant[6], contrevenant[7],
                     contrevenant[8], contrevenant[9])
                     for contrevenant in qry]
        return jsonify([contrevenant.asDictionary() for contrevenant in
                       resultats]), 200

    except:
        return "", 400

@app.route('/api/utilisateur', methods= ["POST"])
@schema.validate(utilisateur_schema)
def creation_utilisateur():
    data = request.get_json()
    try:
        hash_mot_de_passe = generate_password_hash(data["mot_de_passe"])

        array_to_string = json.dumps(data["etablissements"])

        conn = sqlite3.connect('db/contrevenants.db', check_same_thread=False)
        c = conn.cursor()
        sql_statement = """insert into utilisateurs(prenom, nom_de_famille,
            mot_de_passe, adresse_mail, etablissement)
            VALUES(?,?,?,?,?)"""
        c.execute(sql_statement,
            (data["prenom"],data["nom_de_famille"],hash_mot_de_passe,
                data["adresse_mail"], array_to_string))
        conn.commit()
        return "", 201

    except:
        return "", 400

@app.route('/api/inspection', methods= ["POST"])
@schema.validate(inspection_schema)
def demande_inspection():
    data = request.get_json()
    try:
        date_visite = datetime.datetime.strptime(data["date_visite"],
            "%Y-%m-%d").date()

        conn = sqlite3.connect('db/contrevenants.db', check_same_thread=False)
        c = conn.cursor()
        sql_statement = """insert into inspections(prenom, nom_de_famille,
            nom_etablissement, adresse, ville, date_visite, description)
            VALUES(?,?,?,?,?,?,?)"""
        c.execute(sql_statement,
            (data["prenom"],data["nom_de_famille"],data["nom_etablissement"],
                data["adresse"],data["ville"],
                date_visite, data["description"]))
        conn.commit()
        return "", 201

    except:
        return "", 400

@app.route('/doc')
def doc_template():
    return render_template('doc.html')

@app.route('/recherche_dates')
def recherche_dates_template():
    return render_template('recherche_dates.html', reload = time.time())

@app.route('/recherche_etablissements')
def recherche_etablissements_template():
    qry = db_session.query(Contrevenants)
    resultats = qry.all()
    return render_template('recherche_etablissements.html',
        noms_etablissements=resultats, reload = time.time())

@app.route('/demande_inspection')
def inspections_template():
    return render_template('inspection.html', reload = time.time())



if __name__ == "__main__":
    app.run()
