
<html>
<head>
<meta charset="utf-8">
<title>Idong</title>
</head>
<body>

<?php
function utf2euc($str) { return iconv("UTF-8","cp949//IGNORE", $str); }
function euc2utf($str) { return iconv("cp949","UTF-8//IGNORE", $str); }

$filename = "../data/".$_POST["txtTitle"].".txt";


echo "txtTitle :  ";
echo $filename;
echo "<br>";
//echo $_SERVER['HTTP_USER_AGENT'] . "\n\n";

$browser = get_browser(null, true);

if($browser[platform] != 'MacOSX')
	$filename = utf2euc($filename);

if(($handle = fopen($filename, "a")) !== FALSE){
	$text = $_POST[context];
	$text .= "\r\n";
	fwrite($handle, $text);
	fclose($handle);
}

echo "txtTitle2 :  ";
echo $filename;
echo "<br>";

$filename = euc2utf($filename);


echo "txtTitle3 :  ";
echo $filename;
echo "<br>";

?>
</body>
</html>
