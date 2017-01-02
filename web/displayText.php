
<html>
<head>
<meta charset="utf-8">
<title>Idong</title>
</head>
<body>

<?php
//function utf2euc($str) { return iconv("UTF-8","cp949//IGNORE", $str); }
//function euc2utf($str) { return iconv("cp949","UTF-8//IGNORE", $str); }

function coloringWord($str, $color) {
	return "<a href='http://dic.naver.com/search.nhn?sLn=kr&&searchOption=&isOnlyViewEE=N&query=".$str."'>
		<span style=\"color:".$color."\">".$str."</span></a>";
}
$colorList = array("red", "blue", "green", "yellow", "pink");


#   Words text File Warning 
#   : It should be ended with "\r\n" << blank line.

//$filename = "../data/".$_POST["txtTitle"].".txt";
$wordF = "../data/writeWord.txt";
$textF = "../data/writeTest.txt";

//echo$buffer;
$row = 0;
$wf = fopen($wordF, "r") or die("Failed to load file.");

echo "Key words<br>";
while(!feof($wf)){
	$keys[$row++] = trim(fgets($wf));
}
for($row=0; $row < count($keys)-1; $row++){
	$colorKeys[$row] = coloringWord($keys[$row], $colorList[$row]);
	echo $colorKeys[$row]."<br>";
}
echo "<br><br>";


$tf = fopen($textF, "r") or die("Failed to load file.");
while(!feof($tf)){
	$buffer = fgets($tf)."<br>";
	if($buffer == "\r\n<br>") continue;
	
	$newbuffer = str_replace($keys, $colorKeys, $buffer);
	echo "#".$newbuffer;
	
	
	echo "<br>";
}


//echo$buffer;
fclose($tf);
fclose($wf);



?>
</body>
</html>
