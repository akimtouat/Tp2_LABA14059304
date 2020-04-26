$(function() {



    document.getElementById('inspection').onclick=function() {
        //console.log(url);
        var inspection = {
          prenom: document.getElementById('prenom').value,
          nom_de_famille: document.getElementById('nom_de_famille').value,
          nom_etablissement: document.getElementById('nom_etablissement').value,
          adresse: document.getElementById('adresse').value,
          ville: document.getElementById('ville').value,
          date_visite: document.getElementById('date_visite').value,
          description: document.getElementById('description').value
        };
        var json_to_string = JSON.stringify(inspection);
        var xhttp = new XMLHttpRequest();

        xhttp.open("POST", "/api/inspection", true);

        xhttp.setRequestHeader("Content-Type", "application/json");


        xhttp.send(JSON.stringify(inspection));
        $("body").html("La demande d'inspection a été reçu");
    };

})
