import os.path
import urllib.request
from random import choice
from bs4 import BeautifulSoup
from requests import get
from os import system

class lightextender:
	def generate(_symbols: str="qwertyuiopasdfghjklzxcvbnm1234567890", _len=6):
		"""This function returns a random link index with a screenshot to lightshot"""
		_index = ""
		for i in range(0, _len):
			_index += choice(_symbols)
		return _index
	
	def request(_index: str):
		"""This function gets a link to the exact picture"""
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
		urllib.request.install_opener(opener)

		html = urllib.request.urlopen("https://prnt.sc/"+_index).read()
		soup = BeautifulSoup(html, 'html.parser')
		try:
			picture_url = soup.find(id='screenshot-image')['src']
		except TypeError:
			return False

		return picture_url
	def bashdownload(_source_url: str):
		"""This function loads the image.
		However, the download is done with
		commands to terminal. Wget must already 
		be installed."""
		if os.path.exists("images") != True:
			system("mkdir images")
		if _source_url != False:
			return system("wget -P images/ -q "+ _source_url)
	def download(_source_url: str):
		"""This function downloads the picture using the urlretrieve"""
		urllib.request.urlretrieve(_source_url, _source_url[32:])
	def download_content(_source_url: str):
		"""This function downloads the picture using the requests.get"""
		if type(_source_url) not in [' ', bool]:
			_output_url = _source_url.replace("https://i.imgur.com/", "").replace("https://image.prntscr.com/image/", "")
			open(f"images/{_output_url}", "wb").write(get(_source_url).content)