//toggle-menu
$(document).ready(function  () {
	$("#bar").click(function () {
		$("#menu").toggle("swing");
		console.log("click en la barra");
	});
});


//scrooll
$(document).ready(function  () {
	$(window).scroll(function  () {
		$("#menu").hide("swing");
	});
});


