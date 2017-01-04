<!DOCTYPE html>
<html>
<head><link rel="stylesheet" type="text/css" href="design.css">
<meta charset="utf-8">
<a href=./storeURL.php><div class="head"><h1>SummThing</h1></div></a>
<title>Store URL</title>
</head>
<body>
<br><br>

<form method="post" action="selectType.php"><div style="text-align:center">
	<input type="text" size = 100 value = "url 입력" onclick="this.value = ''" 
	id="url" name="url" style="color:gray ; font-size: 10pt">
	<button name="store_but">url입력</button>	
</form>
<!--
<form method="post" action="selectType.php">
	<input type="submit" value="결과보기" >
</form>


<script type="text/javascript" language="javascript">
	
	function btn_js_confirm_click(){
	  /* confirm(문자열, 초기값) */
	  var check = confirm("확인 또는 취소 버튼");
	  /* if(check == true) else false */
	  if(check) alert("확인버튼 클릭");
	  else alert("취소버튼 클릭");
	}

</script>
<form method="post">
	<input type="button" name="btn_js_confirm" id="btn_js_confirm" onclick="btn_js_confirm_click();" value="확인창" />
</form>

-->
</body>
</html>