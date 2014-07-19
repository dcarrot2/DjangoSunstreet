$(document).ready(function(){
	

	$("input").click(function(){
		
		var e = document.getElementById("item1");
		if($(e).val() == ""){
			alert("You forgot to choose a school!");
			return false;
		}
		else{

			document.school_select_form.action = document.school_select_form.action + event.target.id;
			return true;
		}


	});
});