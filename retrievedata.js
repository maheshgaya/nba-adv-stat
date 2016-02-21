$(document).ready(function(){
	$("tr.StephCurry").html
});

jQuery.get('playerstat/curry.txt', function(data){
	$('tr.StephCurry').html(data)
}, 'text');