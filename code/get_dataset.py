#!/usr/bin/env python
# -*- coding: utf-8 -*-


import bs4
import html5lib
import requests

"""
proxy = urllib2.ProxyHandler({'http': 'http://omaestre:##QWasZX123##@10.66.3.149:8080',
                              'https': 'https://omaestre:##QWasZX123##@10.66.3.149:8080'}
                             )
                             
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)
"""

#url = "https://elpais.com"
#url = "http://www.lavanguardia.com"
#url = "http://www.abc.es"


url_elmundo = "http://www.elmundo.es"
contenido = requests.get(url_elmundo)
html_elmundo = contenido.text
sopa_elmundo = bs4.BeautifulSoup(html_elmundo, "html5lib")


url_elpais = "https://elpais.com/s/setEspana.html"
contenido2 = requests.get(url_elpais)
html_elpais = contenido2.text
sopa_elpais = bs4.BeautifulSoup(html_elpais, "html5lib")



def scrap_elmundo():
	articulo = {"class":"mod-item"}
	titulo   = {"itemprop" : "headline"}
	salida = sopa_elmundo.findAll("article", attrs = articulo)
	for titular in salida:
		try:
			h3 = titular.find("h3", attrs = titulo)
			a=h3.find("a", href=True)
			fecha = titular.find("time").text
			autor = titular.find("span",attrs={"itemprop":"name"}).text
			print h3.text, a['href'], fecha, autor
		except Exception as e:
			pass
			#print e
	print len(salida)

#scrap_elmundo()



def scrap_elpais():
	#articulo = {"class":"articulo__interior"}
	#titulo   = {"class":"articulo-titulo"}
	articulo2 = {"class":"articulo"}
	titulo2 = {"itemprop" : "headline"}
	salida = sopa_elpais.findAll("article", attrs=articulo2)#, attrs = articulo)
	#print len(salida)
	for titular in salida:
		try:
			h2 = titular.find("h2", attrs = titulo2)			
			a=h2.find("a", href=True)			
			fecha = titular.find("meta", attrs={"itemprop":"datePublished"})["content"]
			autor = titular.find("div",attrs={"class":"autor"}).text
			print h2.text, a['href'], fecha, autor.strip()
		except Exception as e:
			#print e
			pass
	print len(salida)

scrap_elpais()
