$(document).ready(function(){

	$("input").click(function(){
	
		var e = document.getElementById("item1");
		if($(e).val() == ""){
			alert("You forgot to choose a school!");
			return false;
		}
	});
});