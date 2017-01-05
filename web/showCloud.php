
<html>
<head><link rel="stylesheet" type="text/css" href="design.css">
<meta charset="utf-8">
<br><br>
<a href=./storeURL.php><h1>SummThing</h1></a>
<div style="text-align:center"><p>----------------<br>워드 클라우드 보기</p></div>
<title>Word Cloud</title>
</head>


<?php 

	// If store button is clicked -> function call
	$filename = "../wordcloud.png";

	// Open file with write option.
	if(($handle = fopen($filename, "w")) !== FALSE){
	//	fwrite($handle, $text);
		echo "created<br>";
	}
	else{
		echo "can't not create<br>";
	}
	exec('chmod 777 ../wordcloud.png', $output);
	while(list($key, $val)=each($output)){
		echo $key."=".$val."\n";
	}
	
	$command = "/usr/local/bin/python ../wordCloud.py 2>&1";
    $pid = popen( $command,"r");
	while( !feof( $pid ) )
	{
		 echo fread($pid, 256);
		 flush();
		 ob_flush();
		 usleep(100000);
	}
	pclose($pid);
	fclose($handle);
	
	
?>

<body>
<br><br>
<div style="text-align: center">
<img src="../wordcloud.png" width="500" alt="wordCloud.png" /> 
</div>
<br><br><br>

</body>

</html>
