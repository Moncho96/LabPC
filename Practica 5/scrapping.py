# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:34:36 2021

@author: Moncho
"""
import requests
from bs4 import BeautifulSoup as bs
import re
from openpyxl import Workbook
import os

book = Workbook()
dir = input("Ingresar nombre de la carpeta que quiere crear: ")
os.system("mkdir " + dir)
sheet = book.active

# Informacion personal Checo Perez
def informacionAtleta():
    print("-----------------Informacion personal del Atleta------------------")
    print()
    archInfo = open ("WikiCheco.txt","r")
    c = archInfo.read()
    source = requests.get(c)
    soup = bs(source.content, 'html.parser')
    content = soup.find(class_="infobox")
    datos = content.find_all('tr')
    
    sheet["A1"] = "Informacion personal del Atleta"
    
    #Nombre del atleta
    nom = re.compile(r"\w{6}.\w{6}.\w{5}.\w{7}")
    nom2 = nom.findall(str(datos))
    print("Nombre:", nom2[0])
    print()
    sheet["A2"] = "Nombre"
    sheet["B2"] = str(nom2[0])
    
    #Fecha de nacimiento
    an = re.compile(r'\d{2}.\w{2}.\w{5}.\w{2}.\d{4}')
    an2 = an.findall(str(datos))
    print("Nacimiento:",an2[0])
    print()
    sheet["A3"] = "Fecha de nacimiento"
    sheet["B3"] = str(an2[0])
    
    #Debut
    debut = re.compile(r'\d{4}')
    debut2 = debut.findall(str(datos))
    print("Debut:", debut2[10])
    print()
    sheet["A4"] = "Debut"
    sheet["B4"] = str(debut2[10])
    
    #Nacionalidad
    nac = re.compile(r'\w{8}')
    nac2 = nac.findall(str(datos))
    print("Nacionalidad:", nac2[34])
    print()
    sheet["A5"] = "Nacionalidad"
    sheet["B5"] = str(nac2[34])
    
def noticiasAtleta():
    print("-----------------------------Noticias-----------------------------")
    print()
    
    sheet["D1"] = "Noticias"
    
    #Archivo noticias 1
    archNot = open("noticias1.txt","r")
    c = archNot.read()
    source = requests.get(c)
    soup = bs(source.content,'html.parser')
    not1 = soup.find('title').text
    print("NOTICIOOOON!!!!!:",not1)
    print()
    sheet["D2"] = "Noticia 1"
    sheet["E2"] = not1
    
    #Archivo noticias 2
    archNot = open("noticias2.txt","r")
    c = archNot.read()
    source = requests.get(c)
    soup = bs(source.content,'html.parser')
    not1 = soup.find('title').text
    print("NO ME LA CREOOOOO:",not1)
    print()
    sheet["D3"] = "Noticia 2"
    sheet["E3"] = not1
    
    #Primera imagen
    img1 = soup.find('figure', class_="single-featured-image")
    img2 = img1.find('img')['data-src']
    nom = "imagenNot2.jpg"
    imagen1 = requests.get('https:'+img2).content
    with open(dir + "/" + nom, 'wb') as f:
        f.write(imagen1)
        print ("******Imagen descargada, guardada como: ", nom,(" **********"))
    print()
    
    #Archivo noticias 3
    archNot = open("noticias3.txt","r")
    c = archNot.read()
    source = requests.get(c)
    soup = bs(source.content,'html.parser')
    not1 = soup.find('title').text
    print("NI EL BICHO ES TAN HUMILDE:",not1)
    print()
    sheet["D4"] = "Noticia 3"
    sheet["E4"] = not1
    
    #Segunda imagen
    img1 = soup.find('div', class_="nd-md-base")
    img2 = img1.find('img')['src']
    nom = "imagenNot3.jpg"
    imagen1 = requests.get(img2).content
    with open(dir + "/" + nom, 'wb') as f:
        f.write(imagen1)
        print ("******Imagen descargada, guardada como: ", nom,(" **********"))
    print()
    
def climaProximo():
    print("---------------------Proximas fechas de la F1---------------------")
    print()
    api_address = #Insertar API
    print("PORTIMAO CIRCUIT 30 de mayo de 2021")
    ciudad = "portimao"
    horaUTC = "&start=1622350800"
    url = api_address + ciudad + horaUTC
    
    json_data = requests.get(url).json()
    clima = json_data['weather'][0]['main']
    tempe = json_data['main']['temp']
    print("El clima para esa fecha sera:",clima,"y la temperatura sera: ",tempe,"°F")
    print()
    sheet["A8"] = "Clima"
    sheet["A9"] = "Sede y Fecha"
    sheet["B9"] = "Clima"
    sheet["C9"] = "Temperatura"
    
    sheet["A10"] = "PORTIMAO CIRCUIT 30 de mayo de 2021"
    sheet["B10"] = clima
    sheet["C10"] = tempe
    
    print("BAKU CITY CIRCUIT 4 de junio de 2021")
    ciudad = "BAKU"
    horaUTC = "&start=1622764800"
    url = api_address + ciudad + horaUTC
    json_data = requests.get(url).json()
    clima = json_data['weather'][0]['main']
    tempe = json_data['main']['temp']
    print("El clima para esa fecha sera:",clima,"y la temperatura sera: ",tempe,"°F")
    print()
    sheet["A11"] = "BAKU CITY CIRCUIT 4 de junio de 2021"
    sheet["B11"] = clima
    sheet["C11"] = tempe
    
    
    print("PAUL RICARD CIRCUIT 18 de junio de 2021")
    ciudad = "CASTELLET"
    horaUTC = "&start=1623974400"
    url = api_address + ciudad + horaUTC
    json_data = requests.get(url).json()
    clima = json_data['weather'][0]['main']
    tempe = json_data['main']['temp']
    print("El clima para esa fecha sera:",clima,"y la temperatura sera: ",tempe,"°F")
    print()
    
    sheet["A12"] = "PAUL RICARD CIRCUIT 18 de junio de 2021"
    sheet["B12"] = clima
    sheet["C12"] = tempe
    
    book.save('Checo.xlsx')

def main():
    informacionAtleta()
    noticiasAtleta()
    climaProximo()
    
if __name__=="__main__":
    main()
