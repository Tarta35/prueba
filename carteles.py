import sys
import validnument
from getpass import getpass
from os import system as b
sys.path.append("Descargas")
from validnument import validaRangoDigitos as s
import time
import pickle
import os
import os.path
from cprint import *

global Codl
Codl = [0]*50

def switchCarteles(opc):             #Diferentes prints a mostrar del menu de admin.

    if opc == 6:
        cartelAdmin()
    elif opc == 1:
        cartelGestLocales()
    elif opc == 2:
        enConstrucc()
    elif opc == 3:
        enConstrucc()
    elif opc == 4:
        cartelGestNov()
    elif opc == 5:
        enConstrucc()

def cartelAdmin():               #.
    cprint.info("\n1. Gestion de locales.\n2. Crear cuentas de duenos de locales\n3. Aprobar / Denegar solicitud de descuento\n4. Gestion de novedades\n5. Reporte de utilizacion de descuentos\n0. Salir\n")

def cartelGestLocales():                  #Cartel para el menu de gestion de locales.
    cprint.info('1. Gestion de locales.\n\n\ta) Crear locales\n\tb) Modificar local\n\tc) Eliminar local\n\td) Mapa de Locales\n\te) Volver')

def cartelGestNov():                 #.
    cprint.info('\n\ta) Crear novedades\n\tb) Modificar novedad\n\tc) Eliminar novedad\n\td) Volver\n')

def cartelCrearDueno():
    "fijarse si es necesario"

def enConstrucc():                             #.
    cprint.ok("\nEn construccion...")
    time.sleep(3)
    b("cls")

def mapa():                     #Mapa de locales
    m=0
    for l in range (10):
        print("+------"*5+"+")
        print("| {:^4.0f} | {:^4.0f} | {:^4.0f} | {:^4.0f} | {:^4.0f} |".format(Codl[m],Codl[m+1],Codl[m+2],Codl[m+3],Codl[m+4]))
        m=m+5
    print("+------"*5+"+")
    decis=input("\nIngrese * para cerrar el mapa: ")
    while decis!="*":
        decis= input("\nIngrese * para cerrar el mapa: ")