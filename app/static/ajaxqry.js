$(function() {

    $('#chercher').click(function() {
        //console.log(url);
        $.ajax({
          url : '/api/contrevenants?debut=' + document.getElementById('debut'
               ).value + '&fin=' + document.getElementById('fin').value,
          success: function(data)  {
              $('#myTable').html("<tr>" +
                  "<th>Établissement</th>"+
                  "<th>Nombre d'infractions</th>"+
              "</tr>")
              for (var i=0; i<data.length; i++) {
                var j=data.length - 1;
                var nbr_infraction = 1;
                while (i<j) {
                    if(data[i].etablissement.localeCompare(
                       data[j].etablissement) == 0){
                        data.splice(j,1);
                        nbr_infraction++;

                    }
                    j--;
               }
                  var row = $('<tr><td>' + data[i].etablissement+ '</td><td>' +
                      nbr_infraction + '</td></tr>');
                  $('#myTable').append(row);
              }
          },
          error: function(jqXHR, textStatus, errorThrown){
              alert('Error: ' + textStatus + ' - ' + errorThrown);
          }

        });
    });


    $('#recherche_infractions').click(function() {
        //console.log(url);
        $.ajax({
          url : '/api/contrevenants/infractions?nom_etablissement=' +
          document.getElementById('etablissement').value,
          success: function(data)  {
              $('#table_infractions').html("<tr>" +
                  "<th>Établissement</th>"+
                  "<th>proprietaire</th>"+
                  "<th>adresse</th>"+
                  "<th>Ville</th>"+
                  "<th>Description</th>"+
                  "<th>Date d'infraction</th>"+
                  "<th>Date de jugement</th>"+
                  "<th>montant</th>"+
              "</tr>")
              for (var i=0; i<data.length; i++) {
                  var row = $('<tr><td>' + data[i].etablissement+ '</td><td>' +
                      data[i].proprietaire + '</td><td>'+
                      data[i].adresse + '</td><td>' +
                      data[i].ville + '</td><td>'+
                      data[i].description + '</td><td>'+
                      data[i].date_infraction + '</td><td>'+
                      data[i].date_jugement + '</td><td>'+
                      data[i].montant + '</td></tr>');
                  $('#table_infractions').append(row);

              }
          },
          error: function(jqXHR, textStatus, errorThrown){
              alert('Error: ' + textStatus + ' - ' + errorThrown);
          }

        });
    });
})
