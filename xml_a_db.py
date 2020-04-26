import requests
import sqlite3
import dateparser
import xml.etree.ElementTree as Et
from sqlite3 import OperationalError
from db_setup import init_db, db_session
from app.models import Contrevenants

def xml_download():
    init_db()



    r = requests.get("""http://donnees.ville.montreal.qc.ca/dataset/a5c1f0b9-261f-4247-99d8-f28da5000688/resource/92719d9b-8bf2-4dfd-b8e0-1021ffcaee2f/download/inspection-aliments-contrevenants.xml""")

    with open('db/contrevenants.xml', 'wb') as f:
        f.write(r.content)

    conn = sqlite3.connect('db/contrevenants.db', check_same_thread=False)
    c = conn.cursor()

    tree = Et.parse('db/contrevenants.xml')
    root = tree.getroot()
    for contrevenant in root:
        resultats = []
        infraction = dateparser.parse(contrevenant[6].text).date().isoformat()
        jugement = dateparser.parse(contrevenant[7].text).date().isoformat()
        qry = db_session.query(Contrevenants).filter(
            Contrevenants.proprietaire.contains(contrevenant[0].text)).filter(
            Contrevenants.categorie.contains(contrevenant[1].text)).filter(
            Contrevenants.etablissement.contains(contrevenant[2].text)).filter(
            Contrevenants.adresse.contains(contrevenant[3].text)).filter(
            Contrevenants.ville.contains(contrevenant[4].text)).filter(
            Contrevenants.description.contains(contrevenant[5].text)).filter(
            Contrevenants.date_infraction.contains(infraction)).filter(
            Contrevenants.date_jugement.contains(jugement)).filter(
            Contrevenants.montant.contains(contrevenant[8].text))
        resultats = qry.all()

        if not resultats:
            sql_statement = """insert into contrevenant(proprietaire, categorie,
                etablissement, adresse, ville,
                description, date_infraction, date_jugement, montant)
                VALUES(?,?,?,?,?,?,?,?,?)"""
            c.execute(sql_statement,
                (contrevenant[0].text, contrevenant[1].text,
                contrevenant[2].text, contrevenant[3].text,
                contrevenant[4].text, contrevenant[5].text,
                infraction, jugement,
                contrevenant[8].text))
            conn.commit()
