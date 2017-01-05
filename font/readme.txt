한글을 지원하는 폰트를 적용하기 위해
‘BMDOHYEON_ttf.ttf ‘ 파일을 

site-packages/pytagcloud/fonts 에 넣어준다.

그리고 fonts 디렉토리 안에

fonts.json 파일에

{
	"name" : "korean",
	"ttf" : "BMDOHYEON_ttf.ttf",
	"web" : "http://fonts.googleapis.com/css?family=Nobile"
}

을 추가해준다.