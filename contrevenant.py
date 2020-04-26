class Contrevenant:
    def __init__(self, id, proprietaire, categorie,
        etablissement, adresse, ville,
        description, date_infraction, date_jugement, montant):
        self.id = id
        self.proprietaire = proprietaire
        self.categorie = categorie
        self.etablissement = etablissement
        self.adresse = adresse
        self.ville = ville
        self.description = description
        self.date_infraction = date_infraction
        self.date_jugement = date_jugement
        self.montant = montant

    def asDictionary(self):
        return {"id": self.id,
                "proprietaire": self.proprietaire,
                "categorie": self.categorie,
                "etablissement": self.etablissement,
                "adresse": self.adresse,
                "ville": self.ville,
                "description": self.description,
                "date_infraction": self.date_infraction,
                "date_jugement": self.date_jugement,
                "montant": self.montant}
