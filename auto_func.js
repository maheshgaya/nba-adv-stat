//function toggles "Show Advanced Statistics"
function toggleTable(num){
	var elementname = 'advanced_stat' + num.toString();
	var ltable = document.getElementById(elementname);
	var textname = 'advanced' + num.toString();
	var changeText = document.getElementById(textname);
	/*ltable.style.display = (ltable.style.display == "table")? "none" : "table";*/

	if (ltable.style.display == "table"){
		ltable.style.display = "none";
		changeText.innerHTML = "Show Advanced Player Statistics";
	} 
	else {
		ltable.style.display = "table";
		changeText.innerHTML = "Hide Advanced Player Statistics";
	}
}

//function toggles "Show Advanced Statistics"
function toggleTeam(num){
	var elementname = 'team_stat' + num.toString();
	var ltable = document.getElementById(elementname);
	var textname = 'team' + num.toString();
	var changeText = document.getElementById(textname);
	/*ltable.style.display = (ltable.style.display == "table")? "none" : "table";*/

	if (ltable.style.display == "table"){
		ltable.style.display = "none";
		changeText.innerHTML = "Show Team Statistics";
	} 
	else {
		ltable.style.display = "table";
		changeText.innerHTML = "Hide Team Statistics";
	}
}

