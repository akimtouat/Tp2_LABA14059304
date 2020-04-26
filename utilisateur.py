class Utilisateur:
    def __init__(self,id, prenom, nom_de_famille, adresse_mail, etablissements):
        self.id = id
        self.prenom = prenom
        sel.nom_de_famille = nom_de_famille
        self.adresse_mail = adresse_mail
        self.etablissements = etablissements

    def asDictionary(self):
        return {
            "id": self.id,
            "prenom": self.prenom,
            "nom_de_famille": self.nom_de_famille,
            "adresse_mail": self.adresse_mail,
            "etablissements" = self.etablissements }
