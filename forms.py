from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, validators, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
class FormRechercheContrevenants(Form):
    choix = [('etablissement', 'Etablissement'),
               ('proprietaire', 'Proprietaire'),
               ('rue', 'Rue')]
    selection = SelectField('Recherche un contrevenant:', choices=choix)
    recherche = StringField('')

class DemandeInspectionForm(FlaskForm):
    prenom = StringField('Prenom', validators=[DataRequired()])
    nom_de_famille = StringField('Nom de famille', validators=[DataRequired()])
    nom_etablissement = StringField("nom de l'etablissement",
        validators=[DataRequired()])
    adresse = StringField('Adresse', validators=[DataRequired()])
    ville = StringField('Ville', validators=[DataRequired()])
    date_visite = DateField('Date de la visite', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()],
        widget=TextArea())
    envoyer = SubmitField('Envoyer')
