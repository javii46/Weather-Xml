# -*- coding: utf-8 -*-

from jinja2 import Template
from lxml import etree
import webbrowser

plantilla=open("plantilla.html","r")
resultado=open("resultado.html","w")
contador=0
provincias=["Almeria","Cadiz","Cordoba","Huelva","Jaen","Malaga","Sevilla"]
velocidad=[]
direccion=[]
listamax=[]
listamin=[]


for i in provincias:

informacion=etree.parse('http://api.openweathermap.org/data/2.5/weather?q=%s&mode=xml&units=metric&lang=es'% i)
temperaturaminima=informacion.find('temperature')
tempmin=temperaturaminima.attrib['min']
listaminima.append(tempmin)

temperaturamaxima=informacion.find('temperature')
tempmax=temperaturamaxima.attrib['max']
listamax.append(tempmax)

velocidad=informacion.find('wind/speed')
vel=velocidad.attrib['value']
velocidad.append(vel)

direccion=informacion.find('wind/direction')
direc=direccion.attrib['code']
direccion.append(direc)

resultado = ""

for linea in plantilla:
resultado += linea

insercion= Template(resultado)
inserccion1= insercion.render(provincias=provincias,velocidad_vel=velocidad,temperatura_minima=listamin,temperatura_maxima=listamax,direccion_dir=direccion)

abrir.write(insercion)

webbrowser.open('resultado.html')






