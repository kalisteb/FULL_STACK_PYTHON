$(document).ready(function(){
    for (let x = 1; x<=151; x++){
        $('#pokemon').append("<a href='#'><img id="+x+" src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+x+".png'></a>");
    }
    $('img').on('click',function(){
        $('#info').empty();
        var x = $(this).attr('id');
        $.get('https://pokeapi.co/api/v2/pokemon/'+x+'/',function(info){
            $('#info').append('<h2>'+info.name+'</h2>');
            $('#info').append("<img id="+x+" src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+x+".png'><br>");
            $('#info').append('<h2>Tipos</h2>');
            $('#info').append('<ul>');
            for (var i = 0; i<info.types.length; i++){
                $('#info').append('<li>'+info.types[i].type.name+'</li>');
            }
            $('#info').append('</ul>')
            $('#info').append('<h2>Altura</h2>')
            $('#info').append('<p>'+info.height+'</p>');
            $('#info').append('<h2>Peso</h2>');
            $('#info').append('<p>'+info.weight+'</p>');
        }, 'json');
    });
});