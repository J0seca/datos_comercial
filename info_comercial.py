import os
import time
import urllib
from urllib import request
from bs4 import BeautifulSoup

def clr():
    os.system("cls")

#Crea y abre link de chileautos buscando modelo y año específico

def link_chileautos():
    clr()
    modelo = input("Ingrese modelo: ").replace(" ","+")
    anio = input("Ingrese año: ")
    url = "https://www.chileautos.cl/vehiculos/?q=(And.Servicio.chileautos._.CarAll.keyword(" + modelo + ")._.Ano.range(" + anio + ".." + anio + ").)"
    print("\n" + url + "\n")
    os.system("start chrome " + url)
    input()
    main()

#búsca datos por patente

def modelo_por_patente():
    patente = input("Ingrese patente: ")
    url = "https://permisodecirculacion.cl/home/?p=" + patente
    source = urllib.request.urlopen(url)
    soup = BeautifulSoup(source, "html.parser")
    info_auto = []
    for auto in soup.find_all("p"):
        auto = str(auto).strip("<p>")
        auto = auto.strip("</p>")
        info_auto.append(auto)
    print("\nMARCA: " + info_auto[1] + "\nMODELO: " + info_auto[2] + "\nAÑO: " + info_auto[3] + "\nMOTOR: " + info_auto[4] + "\nCHASIS: " + info_auto[5])
    input()
    main()   

#Cálculo de datos liquidaciones

def calcula_imponible():
    print("\nhttps://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2021.htm\n")
    os.system("start chrome https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2021.htm")
    try:
        imponible = int(input("Ingrese total imponible: "))
        renta_max = imponible * 0.8 + imponible * 0.25
        print("** Renta máxima con 25% de no imponibles: ", int(renta_max))
    

        afp = int(input("\nIngrese descuento de AFP: "))
        salud = int(input("Ingrese descuento de SALUD: "))
        afc = int(input("Ingrese descuento de AFC: "))
        tributable = imponible - afp - salud - afc
        print("\n\nTotal tributable: ", int(tributable))
    
        factor = float(input("\n\nIngrese factor según renta: ").replace(",","."))
        rebaja = float(input("\nIngrese cantidad a rebajar: ").replace(",","."))
    
        impuesto = tributable * factor - rebaja
    except:
        print("\n ERROR INGRESANDO DATOS! ")
        calcula_imponible()
    print("\n**Total impuesto: ", int(impuesto))
    input()
    main()

#Función principal

def main():
    clr()
    print("""
LISTA DE OPCIONES:

1- Link chileautos.

2- Modelo por patente.

3- Cálculo imponible.

""")
    try:
        opcion = int(input("INGRESE OPCIÓN: "))
    except:
        input("\n ERROR EN INGRESO!")
        main()
    if opcion == 1:
        clr()
        link_chileautos()
    if opcion == 2:
        clr()
        modelo_por_patente()
    if opcion == 3:
        clr()
        calcula_imponible()
    else:
        input("\n ERROR EN INGRESO!")
        main()
main()
