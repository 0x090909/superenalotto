import requests 
import os
import json
#URL = https://www.gntn-pgd.it/gntn-info-web/rest/gioco/superenalotto/estrazioni/archivioconcorso/2015/5

def fetch_JSON(year, month):
	year = str(year)
	month = str(month)
	url = "https://www.gntn-pgd.it/gntn-info-web/rest/gioco/superenalotto/estrazioni/archivioconcorso/"+year+"/"+month
	r = requests.get(url)
	return r.text


def dump_to_file(year, month, content):
	file = open(str(year) + " - " + str(month), "w")
	file.write(content)
	file.close()


def dump_csv():
	big_file = "out.csv"
	BF = open(big_file, "a")
	path = '/home/lavoro/Scrivania/SuperenaLotto'
	files = []
	for i in os.listdir(path):
    		if os.path.isfile(os.path.join(path,i)) and '20' in i:
        		files.append(path+"/"+i) 
	for file in files:
		f = open(file,"r")
		cont = f.read()
		j = json.loads(cont)
		conc = j['concorsi']
		for c in conc:
			print(file)
			est = (c['combinazioneVincente']['estratti'])
			BF.write(str(est)+"\n")
	
	BF.close()
	return files
if __name__ == "__main__":
	dump_csv()
	exit()
	for year in range(2009,2021,1):
		for month in range(1,13,1):
			cont = fetch_JSON(year,month)
			dump_to_file(year, month, cont)
			print(year)
			print(month)
