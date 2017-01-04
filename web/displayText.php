
<html>
<head><link rel="stylesheet" type="text/css" href="design.css">
<meta charset="utf-8">
<br><br>
<a href=./storeURL.php><h1>SummThing</h1></a>
<div style="text-align:center"><p>------------<br>요약문 보기</p></div>
<title>Summarize Text</title>
</head>

<body>

<?php
//function utf2euc($str) { return iconv("UTF-8","cp949//IGNORE", $str); }
//function euc2utf($str) { return iconv("cp949","UTF-8//IGNORE", $str); }

function coloringWord($str, $color) {
	return "<a href='http://dic.naver.com/search.nhn?sLn=kr&&searchOption=&isOnlyViewEE=N&query=".$str."'>
		<span style=\"color:".$color."\" >".$str."</span></a>";
}
$colorList = array("ff0033", "#0099ff", "orange", "009933", "grey");


#   Words text File Warning 
#   : It should be ended with "\r\n" << blank line.

//$filename = "../data/".$_POST["txtTitle"].".txt";
$wordF = "../data/writeWord.txt";
$textF = "../data/writeTest.txt";

//echo$buffer;
$row = 0;
$wf = fopen($wordF, "r") or die("Failed to load file.");
echo "<div class=section>";

echo "Key words<br>";
while(!feof($wf)){ //check the file's end
	$keys[$row++] = trim(fgets($wf));
}
for($row=0; $row < count($keys)-1; $row++){
	$colorKeys[$row] = coloringWord($keys[$row], $colorList[$row]);
	echo "<tt>$colorKeys[$row]</tt>";
}
echo "<br><br><br>";


$tf = fopen($textF, "r") or die("Failed to load file.");
while(!feof($tf)){//check the file's end
	$buffer = fgets($tf)."<br>";
	if($buffer == "\r\n") continue;
	
	$newbuffer = str_replace($keys, $colorKeys, $buffer);
	echo "<tt>#$newbuffer</tt>";
	echo "<br>";
}


//echo$buffer;
fclose($tf);
fclose($wf);


?>
</body>
</html>
