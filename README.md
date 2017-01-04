![SummThing](./img/logo.png)

## What is SummThing?
'SummThing'은 한글로 된 인터넷 기사를 분석하여 핵심 정보를 Summary 하고, 분석된 기사와 관련된 다른 기사 및 정보들을 검색해주는 웹 기반의 서비스입니다. 

SummThing Project는 python과 php언어를 기반으로 개발되었으며, python National Language Toolkit(NLTK), 한국어 National Language Process Library인 KoNLPy, python article extractor인 goose-extractor와 newspapaer등을 이용하고 있습니다. 

* NLTK에 대해 더 알고싶다면?
  http://www.nltk.org/

* KoNLpy에 대해 더 알고싶다면?
  http://konlpy.org/en/v0.4.4/


## Envrionment
SummThing은 다음과 같은 운영체제를 지원합니다. 
- Ubuntu
- Mac OS

SummThing은 다음과 같은 환경에서 구동됩니다. 
- Python  2.7.x 이상
- PHP 5.6
- Apache 2.4 

## Installaion(Ubuntu)
	
	$ sudo apt-get update
	$ sudo apt-get install pip git curl libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev python-pygame python3-pip
	$ sudo pip install JPype1 konlpy Pillow
	$ sudo pip install -U lxml
	$ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
	$ cd SUMMTHING_HOME
	$ pip install https://pypi.python.org/packages/source/g/goose-extractor/goose-extractor-1.0.22.tar.gz
	
## Installation(Mac OS)
	
	$ pip install JPype1
	$ pip install konlpy
	$ pip install --upgrade lxml
	$ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

	$ brew install homebrew/python/pygame
	$ brew install libtiff libjpeg webp littlecms
	$ pip install Pillow
	$ easy_install regex
	$ pip install -U textblob

	$ cd SUMMTHING_HOME
	$ pip install https://pypi.python.org/packages/source/g/goose-extractor/goose-extractor-1.0.22.tar.gz
	

Naver D2 FEST Open Source Project
