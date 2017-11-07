#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Oscar Maestre Sanmiguel
# Se cargan las librerias
import bs4
import html5lib
import requests

# Archivo donde se almacena el dataset
dataset = open("dataset.csv", "a")

# URL EL MUNDO
url_elmundo = "http://www.elmundo.es"
contenido = requests.get(url_elmundo)
html_elmundo = contenido.text
sopa_elmundo = bs4.BeautifulSoup(html_elmundo, "html5lib")

#URL EL PAIS
url_elpais = "https://elpais.com/s/setEspana.html"
contenido2 = requests.get(url_elpais)
html_elpais = contenido2.text
sopa_elpais = bs4.BeautifulSoup(html_elpais, "html5lib")

# FUNCION QUE EXTRAE LOS CAMPOS RELEVANTES DE EL MUNDO
def scrap_elmundo():
	global dataset	
	articulo = {"class":"mod-item"}
	titulo   = {"itemprop" : "headline"}
	salida = sopa_elmundo.findAll("article", attrs = articulo)
	print len(salida)
	for titular in salida:
		try:
			autor=""
			fecha=""			
			h3 = titular.find("h3", attrs = titulo)
			a=h3.find("a", href=True)
			fecha = titular.find("time").text
			autor = titular.find("span",attrs={"itemprop":"name"}).text
			#print h3.text, a['href'], fecha, autor
			registro = h3.text + ";" + a['href'] + ";" + fecha + ";" + autor.strip() + ";EL MUNDO"
			registro = registro.replace("\r","")
			registro = registro.replace("\n","")
			dataset.write(registro.encode('utf-8') + "\n")
		except Exception as e:
			if not autor:
				print "EXCEPCION",autor
				autor = "NA"
			if not fecha:
				print "EXCEPCION",fecha
				fecha = "NA"
			else:
				print e					
			registro = h3.text + ";" + a['href'] + ";" + fecha + ";" + autor.strip() + ";EL MUNDO"
			registro = registro.replace("\r","")
			registro = registro.replace("\n","")
			dataset.write(registro.encode('utf-8') + "\n")				

# FUNCION QUE EXTRAE LOS CAMPOS RELEVANTES DE EL PAIS
def scrap_elpais():
	global dataset
	articulo2 = {"class":"articulo"}
	titulo2 = {"itemprop" : "headline"}
	salida2 = sopa_elpais.findAll("article", attrs=articulo2)#, attrs = articulo)
	print len(salida2)
	for titular in salida2:
		try:
			autor=""
			fecha=""
			h2 = titular.find("h2", attrs = titulo2)			
			a=h2.find("a", href=True)			
			fecha = titular.find("meta", attrs={"itemprop":"datePublished"})["content"]
			autor = titular.find("div",attrs={"class":"autor"}).text
			#print h2.text, a['href'], fecha, autor.strip()
			registro = h2.text + ";" + a['href'] + ";" + fecha + ";" + autor.strip() + ";EL PAIS"
			registro = registro.replace("\r","")
			registro = registro.replace("\n","")
			dataset.write(registro.encode('utf-8') + "\n")			
		except Exception as e:
			flag = True
			if not autor:
				print "EXCEPCION",autor
				autor = "NA"
			if not fecha:
				print "EXCEPCION",fecha
				fecha = "NA"
			if not h2:
				print "EXCEPCION",h2
				fecha = "NA"				
				flag = False	
			else:
				print e	
				
			if flag:					
				registro = a.text + ";" + a['href'] + ";" + fecha + ";" + autor.strip() + ";EL PAIS"
				registro = registro.replace("\r","")
				registro = registro.replace("\n","")
				dataset.write(registro.encode('utf-8') + "\n")				

# Invocar funciones de Scraping
scrap_elmundo()
scrap_elpais()

# Cerrar archivo CSV
dataset.close()
