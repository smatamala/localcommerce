<?php

$bd = new SQLite3('entry.db');
$sql = "SELECT id,latitud ,longitud,description,user FROM entry";
	 
	function getArraySQL($sql){
		$results = $db->query($sql);
		$rawdata = array();
		$i=0;
		while($row = $results->fetchArray())){
			$rawdata[$i] = $row;
			$i++;
		}
	 	return $rawdata;
	}
	$myArray = getArraySQL($sql);
	echo json_encode($myArray);
?>