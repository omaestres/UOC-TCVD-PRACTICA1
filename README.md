# El Mundo vs El País

***

## Perspectiva balanceada de las noticias de los dos principales diarios Españoles con tendencias conservadoras y liberales

![](https://upload.wikimedia.org/wikipedia/commons/3/32/Peri%C3%B3dicosespa%C3%B1olesysustendenciaspol%C3%ADticas.jpg)

## Contexto

Este Dataset fue obtenido desde los portales web de los dos principales diarios españoles de información general según la EGM (Estudio General de Medios http://www.aimc.es/-Datos-EGM-Resumen-General-.html): El Mundo (http://www.elmundo.es) y El País (https://elpais.com). El principal objetivo es poner a disposición los datos minados de ambos portales, para que los ciudadanos puedan contrastar la información publicada en los titulares de noticias de cada diario y evidenciar sus tendencias liberales o conservadoras.

## Contenido

El conjunto de datos esta compuesto por los siguientes campos:

* TITULAR: Es el titular de la noticia
* URL: Es el enlace que apunta a la noticia completa
* FECHA: Fecha de publicacion de la noticia
* AUTOR: Autor o Agencia de noticias
* DIARIO: Es el diario de donde se recopiló la noticia (El Mundo o El País)

Los datos son obtenidos mediante un script en Python, usando la tecnica de Web Scraping en los portales Web de noticias. El script extrae el codigo HTML, identifica los datos relevantes, hace limpieza, seleccion de los datos y finalmente almacena toda la informacion en el archivo dataset.csv. El formato del archivo dataset.csv separa los valores de los campos por puntos y comas (;).

Los principales modulos de Python usados en este proyecto para hacer Web scraping fueron:

Requests y BeautifulSoup

## Agradecimientos

Agradezco principalmente a la Profesora Laia Subirats Maté quien nos brindó las pautas y herramientas para llevar a cabo esta actividad. Y tambien agradezco a las editoriales del EL MUNDO y EL PAIS quienes publican diariamente las noticias en sus portales Web. 

## Inspiración

Este Dataset fue inspirado en el proyecto "Unite These Fuckers" (http://unitethesefuckers.com/), el cual hace un paralelo de las noticias de los principales diarios de habla inglesa, de tendencias liberales y conservadoras. La importancia de este dataset reside en los usuarios pueden comparar si existe algun tipo de sesgo o carga ideológica en la información cuando se abordan las mismas noticias. 

## Licencia
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png)

El Dataset y el codigo de este proyecto esta publicado con licencia Creative Commons CC BY-NC-SA 4.0, la cual debe dar credito a las editoriales de EL MUNDO y EL PAIS y no se puede dar uso comercial de este material. Se ha elegido este licenciamiento para permitir el acceso al publico y a la vez mantener compatibilidad de terminos legales con las fuentes de los datos.
