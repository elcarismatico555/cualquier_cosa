from math import inf
from bs4 import BeautifulSoup
from random import choice
import requests

#if __name__ != "__main__":
#    exit()

#var1 = input("dame url")



def url(link):

    var1 = "pivigames.com"

    respuesta = requests.get(f"https://urlvoid.com/scan/{var1}")
    codigo_retorno = respuesta
    resultado_html = respuesta.text


    soup = BeautifulSoup(resultado_html,"lxml")
    campo_informacion1 = soup.find("tbody")


    labels_tr = []

    for i in campo_informacion1.find_all("tr",limit=8):
        labels_tr.append(i)

    tr1 = labels_tr[0]
    tr2 = labels_tr[1] #  unused
    tr3 = labels_tr[2]
    tr4 = labels_tr[3]
    tr5 = labels_tr[4] #  unused
    tr6 = labels_tr[5]
    tr7 = labels_tr[6]
    tr8 = labels_tr[7]

    info1 = tr1.find("strong").get_text()   #  direccion web
    info2 = tr3.find("span", class_="label label-success").get_text()   #  encontrado en 0 de 44 listas negras

    td = 0
    for i in tr4.find_all("td"):
        td += 1
        if td == 2:
            tr4 = i
    tr4 = str(tr4)
    info3 = tr4.replace("<td>","")
    info3 = info3.replace("</td>","")   #  fecha de registro de dominio


    info4 = tr6.find("strong").get_text()   #  IP de dns


    td = 0
    for i in tr7.find_all("td"):
        td += 1
        if td == 2:
            tr7 = i
    tr7 = str(tr7)
    info5 = tr7.replace("<td>","")
    info5 = info5.replace("</td>","")   #  Nombre DNS


    td = 0
    for i in tr8.find_all("td"):
        td += 1
        if td == 2:
            tr8 = i

    print(tr8)

    info6 = tr8.find("a").get_text()    #  Numero sistema autónomo

    nombreASN = []
    tr8 = str(tr8)
    contador = 0
    for i in tr8:
        if i == " ":
            contador += 1

        if contador == 6 or 7:
            nombreASN.append(i)

    info6_1 = "".join(nombreASN)
    info6_1 = info6_1.replace("</td>","")     # nombre sistema autónomo

    print(info1,info2,info3,info4,info5,info6,info6_1)

url(0)