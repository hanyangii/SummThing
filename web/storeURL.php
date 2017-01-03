<!DOCTYPE html>
<html>
<head><link rel="stylesheet" type="text/css" href="design.css">
<meta charset="utf-8">
<a href=./storeURL.php><div class="head"><h1>SummThing</h1></div></a>
<title>Store URL</title>
</head>
<body>
<br>

<form method="post" action="displayText.php"><div style="text-align:center"><br>
	<input type="text" size = 100 text-color = "gray" value = "url 입력" onclick="this.value = ''" id="url" name="url" style="color:gray ; font-size: 10pt">
	<button name="store_but">summary</button>

</form>

<?php 
// If store button is clicked -> function call
if(isset($_POST["store_but"])){
	$filename = "../data/url.txt";

	if(file_exists($filename)){
		unlink($filename);
	}

	// Open file with write option.
	if(($handle = fopen($filename, "c")) !== FALSE){
		// String text = "http://~~";
		$text = $_POST["url"];
		$text .= "\r\n";
		fwrite($handle, $text);
		fclose($handle);
//		echo "<script>alert(\"saved\");</script>";
	}
	else{
		echo "Can't not open the ".$filename."<br>";
	}
}
?>



</body>
</html>