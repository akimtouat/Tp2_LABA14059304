create table contrevenant (
  id integer primary key,
  proprietaire varchar(100),
  categorie varchar(100),
  etablissement varchar(50),
  adresse varchar(100),
  ville varchar(100),
  description varchar(1000),
  date_infraction date,
  date_jugement date,
  montant varchar(100)
);

create table utilisateurs(
  id integer primary key,
  prenom varchar(50) NOT NULL ,
  nom_de_famille varchar(50) NOT NULL,
  mot_de_passe varchar(50) NOT NULL,
  adresse_mail varchar(50) NOT NULL UNIQUE,
  etablissement text
);

create table inspections(
  id integer primary key,
  prenom varchar(50) ,
  nom_de_famille varchar(50) ,
  nom_etablissement varchar(50) ,
  adresse varchar(50) ,
  ville varchar(50),
  date_visite date,
  description text
)
