utilisateur_schema = {
    'type': 'object',
    'required': ['prenom', 'nom_de_famille', 'mot_de_passe', 'adresse_mail',
                 'etablissements'],
    'properties': {
        'prenom': {
            'type': 'string'
        },
        'nom_de_famille': {
            'type': 'string'
        },
        'mot_de_passe': {
            'type': 'string'
        },
        'adresse_mail': {
            'type': 'string'
        },
        'etablissements': {
            'type': 'array',
            "contains": {
              "type": "string"
            }
        },
        'additionalProperties': False
    }
}

contrevenant_schema = {
    'type': 'object',
    'required': ['proprietaire', 'categorie', 'etablissement', 'adresse',
                 'ville', 'description', 'date_infraction', 'date_jugement',
                 'montant'],
    'properties': {
        'proprietaire': {
            'type': 'string'
        },
        'categorie': {
            'type': 'string'
        },
        'etablissement': {
            'type': 'string'
        },
        'adresse': {
            'type': 'string'
        },
        'ville': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'date_infraction': {
            'type': 'string'
        },
        'date_jugement': {
            'type': 'string'
        },
        'montant': {
            'type': 'string'
        },
        'additionalProperties': False
    }
}

inspection_schema = {
    'type': 'object',
    'required': ['prenom', 'nom_de_famille', 'nom_etablissement', 'adresse',
                 'ville', 'date_visite', 'description'],
    'properties': {
        'prenom': {
            'type': 'string'
        },
        'nom_de_famille': {
            'type': 'string'
        },
        'nom_etablissement': {
            'type': 'string'
        },
        'adresse': {
            'type': 'string'
        },
        'ville': {
            'type': 'string'
        },
        'date_visite': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'additionalProperties': False
    }
}
