<?php
$db = new SQLite3('../../entry.db');
$sql = "SELECT id,latitud ,longitud,description,user FROM entry";
	 
	function disconnectDB($conexion){
		$close = mysqli_close($conexion);
	 	return $close;
	}
	 
	function getArraySQL($sql){
		$results = $db->query($sql);
		$rawdata = array();
		$i=0;
		while($row = mysqli_fetch_array($result)){
			$rawdata[$i] = $row;
			$i++;
		}
	 	return $rawdata;
		disconnectDB($conexion);
	}
	$myArray = getArraySQL($sql);
	echo json_encode($myArray);
?>