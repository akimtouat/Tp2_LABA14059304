from flask_table import Table, Col, LinkCol

class Resultats(Table):
    id = Col('id')
    proprietaire = Col('proprietaire')
    categorie = Col('categorie')
    etablissement = Col('etablissement')
    adresse = Col('adresse')
    ville = Col('ville')
    description = Col('description')
    date_infraction = Col('date_infraction')
    date_jugement = Col('date_jugement')
    montant = Col('montant')
