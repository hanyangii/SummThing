<html>
<head>
<link rel="stylesheet" type="text/css" href="design.css">
<meta charset="utf-8">
<br><br>
<a href=./storeURL.php><h1>SummThing</h1></a>
<title>Select Type</title>
</head>
<br>
<form method="post"><div style="text-align:center">
	<input type="text" size = 100 id="url" 
	 value = <?php $url = $_POST["url"]; echo $url;?> 
	 name="url" style="font-size: 10pt">

	<button name="store_but">url입력</button>	
</form>
<br><br><br>

<div align="center">
<table class=maintable>
<tr><td>
	<a href=./displayText.php>요약문보기</a>
</td><td>
	<a href=./showCloud.php>워드클라우드보기</a>
</td><td>
	<a href=./showCloud.php>단어위치보기</a>
</td><td>
	<a href=./graphTest.html>그래프보기</a>
</td></tr>

</div>

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
