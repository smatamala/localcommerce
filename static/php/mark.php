<?php  
	$sql = "select * from marker";
	function connectDB(){
		$server = "localhost";
		$user = "root";
		$pass = "udec12345";
		$bd = "markers";
		$conexion = mysqli_connect($server, $user, $pass,$bd);
		return $conexion;
	}
	 
	function disconnectDB($conexion){
		$close = mysqli_close($conexion);
	 	return $close;
	}
	 
	function getArraySQL($sql){
		$conexion = connectDB();
		mysqli_set_charset($conexion, "utf8");
		if(!$result = mysqli_query($conexion, $sql)) die();
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

	// metodo utilizado para conectar la base de datos http://geekytheory.com/json-ii-creacion-de-un-json-a-partir-de-una-consulta-en-mysql/

	?>