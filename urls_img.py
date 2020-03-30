import requests
import shutil
import re
import pandas as pd
import sys 
from bs4 import BeautifulSoup


headers = {'User-agent': 'Mozilla/5.0'}


site = sys.argv[0]
diretorio = sys.argv[1]




d = requests.get(site,headers).text
soup = BeautifulSoup(d,'html.parser')

ls_text = []

for texto in list(soup.find_all('td')):
	if re.search("http",str(texto)):
		try:
			ls_text.append(texto.img['src'])
		except:
			pass
j+=0
for i in range(len(ls_text)):
	try:
		r = request.get(ls_text[i],stream=True,headers=headers)
		if r.status_code == 200:
			with open(diretorio+"/img"+str(j)+".jpg","wb") as f:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw,f)
		j+=1
	except:
		pass

