<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Store URL</title>
</head>
<body>

<form method="post">
	url : 
	<input type="text" id="url" name="url"> <br>
	<button name="store_but">Store</button>
</form>

<?php 
// If store button is clicked -> function call
if(isset($_POST["store_but"])){
	$filename = "../data/url.txt";
	// Open file with write option.
	if(($handle = fopen($filename, "a")) !== FALSE){
		// String text = "http://~~";
		$text = $_POST["url"];
		$text .= "\r\n";
		fwrite($handle, $text);
		fclose($handle);
	}
	else{
		echo "Can't not open the ".$filename."<br>";
	}
}
?>



</body>
</html>