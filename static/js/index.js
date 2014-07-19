$(document).ready(function(){
	
	var input = document.getElementById("schoolform");
	$("input").click(function(){
	
		var e = document.getElementById("item1");
		if($(e).val() == ""){
			alert("You forgot to choose a school!");
			return false;
		}
	});
});