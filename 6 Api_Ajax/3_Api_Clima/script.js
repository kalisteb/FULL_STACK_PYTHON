$(document).ready(function(){
    $('form').submit(function() {
        var ciudad = $('#city').val();
        var units = $("input[name='units']:checked").val();
        var url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&units=' + units + '&lang={sp, es}' +'&&appid=f83fa28c9dca41604aad53a9f4c5cf70';
        
        $.get(url, function(data) {

            if($('#wrapper').find('#datos')){
                $('#datos').remove();
            }

            $('#searchForm').append('<div id="datos"></div>');
            $('#datos').append('<br><h5>Temperatura en ' + data.name + '<br></h5>');

            var tempUnit;
            if(units == 'imperial'){
                tempUnit = 'F°';
            }
            else if(units == 'metric'){
                tempUnit = 'C°';
            }

            var str = '<h6>Actual: ' + data.main.temp + ' ' + tempUnit + '</h6>' +
                '<h6>Mínima: ' + data.main.temp_min + ' ' + tempUnit + '</h6>' +
                '<h6>Máxima: ' + data.main.temp_max+ ' ' + tempUnit + '</h6>' +
                '<h6>Humedad: ' + data.main.humidity + '%</h6>' +
                '<h5>Coordenadas'+ '</h5>' +
                '<h6>Longitud: ' + data.coord.lon + '</h6>' +
                '<h6>Latitud: ' + data.coord.lat + '</h6>' +
                '<h5>Tiempo '  + '</h5>';
            
            $('#datos').append(str);

            str = '';
            for(var i = 0; i < data.weather.length; i++){
                str += '<h6>' + data.weather[i].description + '</h6>'
            }

            $('#datos').append(str);

        }, 'json');
        return false;
    });
});