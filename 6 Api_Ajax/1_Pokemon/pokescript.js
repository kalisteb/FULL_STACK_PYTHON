$(document).ready(function(){
    for(var i=1; i<=151; i++){
        $('#pokemon').append('<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'+i+'.png">');
    }
    $('#pokemon, img').css('margin', '1%');
    $('img').css('border', '1px solid black');
    $('img').css('background-color', 'lightgrey');
    $('body').css('text-align', 'center');
})