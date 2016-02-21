<?php
$myfile = fopen("userdata.txt", r) or die("Unable to open file!");
$doc = new DomDocument;
$doc->Load('showstat.html');

while(!feof($myfile)){
	$input = fgets($myfile);
	if (preg_match('/[A-Za-z]+/', $input)){
		$element = $doc->getElementById($input);
		echo $element;

	}
	else
	{
		echo "<td>".$input."</td>";
	}

}
fclose($myfile);
?>