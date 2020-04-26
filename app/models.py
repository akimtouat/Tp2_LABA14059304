from app import db

class Contrevenants(db.Model):
    """"""
    __tablename__ = "contrevenant"

    id = db.Column(db.Integer, primary_key=True)
    proprietaire = db.Column(db.String(100))
    categorie = db.Column(db.String(100))
    etablissement = db.Column(db.String(50))
    adresse = db.Column(db.String(100))
    ville = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    date_infraction = db.Column(db.String(100))
    date_jugement = db.Column(db.String(100))
    montant = db.Column(db.String(100))

    def __repr__(self):
        return '<contrevenant %r>' % (self.etablissement)
