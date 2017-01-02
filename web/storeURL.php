<!DOCTYPE html>
<html>
<head><link rel="stylesheet" type="text/css" href="design.css">
<meta charset="utf-8">
<a href=./MainPage.php><div class="head"><h1>SummThing</h1></div></a>
<title>Store URL</title>
</head>
<body>

<br>

<form method="post"><div style="text-align:center">
	url : 
	<input type="text" size = 100 id="url" name="url"><br><br>
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