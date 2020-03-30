import requests
import shutil
import re
import pandas as pd
import sys 
from bs4 import BeautifulSoup

headers = {'User-agent': 'Mozilla/5.0'}


item = sys.argv[0]
diretorio = sys.argv[1]





searchUrl = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj0guz07pfoAhVwHbkGHTX8CVwQ_AUoA3oECA4QBQ".format(item)

d = requests.get(searchUrl,headers).text
soup = BeautifulSoup(d,'html.parser')

ls_text = []

for texto in list(soup.find_all('td')):
	if re.search("http",str(texto)):
		try:
			ls_text.append(texto.get_text())
		except:
			pass


dt_texto = pd.DataFrame({'Texto':ls_text})
dt_texto.to_excel(diretorio+'/texto.xlsx')