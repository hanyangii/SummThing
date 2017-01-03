<html>
<head>
<link rel="stylesheet" type="text/css" href="design.css">
<meta charset="utf-8">
<br><br>
<a href=./storeURL.php><h1>SummThing</h1></a>
<title>Select Type</title>
</head>

<form method="post"><div style="text-align:center">
	<input type="text" size = 100 id="url" 
	 value = <?php $url = $_POST["url"]; echo $url;?> 
	 name="url" style="font-size: 10pt">
	<button name="store_but">url입력</button>	
</form>

<br><br>

<form method="post" action="displayText.php">
	<input type="submit" value="요약문보기" >
</form>
<form method="post" action="showCloud.php">
	<input type="submit" value="워드클라우드보기" >
</form>
<form method="post" action="showCloud.php">
	<input type="submit" value="워드클라우드보기" >
</form>


<?php 

// If store button is clicked -> function call
$filename = "../data/url.txt";

// Open file with write option.
if(($handle = fopen($filename, "w")) !== FALSE){
	// String text = "http://~~";
	$text = $_POST["url"];
	$text .= "\r\n";
	fwrite($handle, $text);
	fclose($handle);
	echo "<script>alert(\"saved\");</script>";
}
else{
	echo "<script>alert(\"can't not open\");</script>";
}
?>


<body>
</body>
</html>
