import sys
import validnument
from getpass import getpass
def b(a):
    print(a)
#from os import system as b
sys.path.append("Descargas")
from validnument import validaRangoDigitos as s
import time
import pickle
import os
import os.path
from cprint import *
from usuarios import valcodDue
from rutas import rutaluciano as ruta


class Locales:
    def __init__(self):
        self.codloc=0
        self.nomloc=""
        self.ubiloc=""
        self.rubloc=""
        self.codus = 0
        self.estado="" #Tipo Char

def formateo_locales():
    regloc.codloc= regloc.codloc
    regloc.nomloc= regloc.nomloc.ljust(50, " ")
    regloc.rubloc= regloc.rubloc.ljust(50, " ")
    regloc.codus= regloc.codus
    #Por si acaso no hice el formateo de estado ya que es char y todos son de mismo tamaño

regloc = Locales()

AFlocales= ruta + "ALlocales.dat"
if not os.path.exists(AFlocales):
    ALlocales = open(AFlocales, "w+b")
else:
    ALlocales = open(AFlocales, "r+b")

class CantRub:
    def init(self):
        self.rubro = ""
        self.cant = 0

regcantrub = [None]*3
for i in range (0,3):
    regcantrub[i] = CantRub()
for i in range (0,3):
    regcantrub[i].cant = 0
regcantrub[0].rubro = "indumentaria"
regcantrub[1].rubro = "perfumeria"
regcantrub[2].rubro = "comida"

maparray = [""]*50

def archnull():
    return os.path.getsize(AFlocales) > 0

def tamreg():
    if archnull():
        ALlocales.seek(0,0)
        aux = pickle.load(ALlocales)
        t = ALlocales.tell()
        return t
    
def cantreg():
    if archnull():
        tamReg = tamreg()
        tamArch = os.path.getsize(AFlocales)
        t = round(tamArch/tamReg)
        return t
    else:
        return 0
    
def validartam(tam, dato):                  #Valida que el string ingresado sea del tamaño limitado.
    if len(dato)>tam:
        return True
    else:
        return False

def guardalocal(cod, nom, ubi, rub, codue, est, pos):
    regloc.codloc = cod
    regloc.nomloc = nom
    regloc.ubiloc = ubi
    regloc.rubloc = rub
    regloc.codus = codue
    regloc.estado = est
    formateo_locales()
    ALlocales.seek(pos,0)
    pickle.dump(regloc, ALlocales)
    ALlocales.flush()

def valSioNo():
    decis=input("\n\t")
    while decis!="si" and decis!="no":
        cprint.info("Ingrese solo (si) o (no), ")
        decis=input()
    return decis

def validartam(tam, dato):                          #Valida que el string ingresado sea del tamaño limitado.
    if len(dato)>tam:
        return True
    else:
        return False

def listalocales():               #Printeo de locales en forma de lista

    b("cls")
    if os.path.getsize(AFlocales) > 0:
        cprint.info("¿Desea ver los locales existentes? Si o No: ")
        decis= valSioNo()
        if decis=="si":
            contenido = '\033[0;34m'+"| {:^26s} | {:^49s} | {:^27s} | {:^27s} | {:^26s} | {:^20s} |"+'\033[0m'
            simbolos = '\033[0;34m'+"-"*110+'\033[0m'
            while decis!="*":
                b("cls")
                print(contenido.format('\033[0;33m'+"Codigo Local"+'\033[0;34m','\033[0;33m'+"Nombre Local"+'\033[0;34m','\033[0;33m'+"Ubicacion"+'\033[0;34m','\033[0;33m'+"Rubro"+'\033[0;34m','\033[0;33m'+"Codigo Dueno"+'\033[0;34m','\033[0;33m'+"Estado"+'\033[0;34m'))
                tam = cantreg()
                ALlocales.seek(0,0)
                for w in range(0,tam):
                    regloc = pickle.load(ALlocales)
                    if regloc.estado == "A":
                        regloc.codloc = '\033[0;32m'+str(regloc.codloc)+'\033[0;34m'
                        regloc.nomloc = '\033[0;32m'+regloc.nomloc.strip()+'\033[0;34m'
                        regloc.ubiloc = '\033[0;32m'+regloc.ubiloc.strip()+'\033[0;34m'
                        regloc.rubloc = '\033[0;32m'+regloc.rubloc.strip()+'\033[0;34m'
                        regloc.codus = '\033[0;32m'+str(regloc.codus)+'\033[0;34m'
                        regloc.estado = '\033[0;32m'+regloc.estado+'\033[0;34m'
                    else:
                        regloc.codloc = '\033[0;31m'+str(regloc.codloc)+'\033[0;34m'
                        regloc.nomloc = '\033[0;31m'+regloc.nomloc.strip()+'\033[0;34m'
                        regloc.ubiloc = '\033[0;31m'+regloc.ubiloc.strip()+'\033[0;34m'
                        regloc.rubloc = '\033[0;31m'+regloc.rubloc.strip()+'\033[0;34m'
                        regloc.codus = '\033[0;31m'+str(regloc.codus)+'\033[0;34m'
                        regloc.estado = '\033[0;31m'+regloc.estado+'\033[0;34m'
                    print(simbolos)
                    print(contenido.format(regloc.codloc,regloc.nomloc,regloc.ubiloc,regloc.rubloc,regloc.codus,regloc.estado))
                print(simbolos)
                decis=input("Ingrese * para cerrar la lista")
                while decis!="*":
                    decis=input("Ingrese * para cerrar la lista")
                b("cls")

def valRubro():                     #Validacion del input que coincida con un rubro
    global rubro
    cprint.info("\nIngrese el rubro del local: ")
    rubro = input()                    
    while rubro != 'indumentaria' and rubro != 'perfumeria' and rubro != 'comida':  
                b("cls")
                cprint.warn("\nEl rubro ingresado no se identifico, vuelva a ingresarlo.")
                cprint.info("\nIngrese el rubro del local: ")
                rubro = input()

def busqdico(dato):                   #Busqueda dicotomica para no repetir nombre de local.
    if archnull():
        tamReg = tamreg()
        cantReg = cantreg()
        desde = 0
        hasta = cantReg - 1    
        print(cantReg)
        medio = (desde + hasta) // 2
        #print(medio*tamReg)
        ALlocales.seek(medio*tamReg, 0)
        regloc = pickle.load(ALlocales)
        while regloc.nomloc.strip() != dato and desde < hasta:
            if dato < regloc.nomloc.strip():
                hasta = medio - 1
            else:
                desde = medio + 1
            medio = (desde + hasta) // 2
            print("medio:",medio,"medio en byte:",medio*tamReg,"desde:",desde,"hasta:",hasta)
            ALlocales.seek(medio*tamReg, 0)
            regloc = pickle.load(ALlocales)

        if regloc.nomloc.strip() == dato:						
            return medio * tamReg							
        else:
            return -1
            print("ssalio por el else")
    else:
        return -1

def ordLoc():
    if archnull():
        tamReg = tamreg()
        tamArch = os.path.getsize(AFlocales)
        cantReg = int(tamArch / tamReg)
        for i in range(0, cantReg-1):
            for j in range (i+1, cantReg):
                ALlocales.seek (i*tamReg, 0)
                auxi = pickle.load(ALlocales)
                ALlocales.seek (j*tamReg, 0)
                auxj = pickle.load(ALlocales)
                if auxi.nomloc.strip() > auxj.nomloc.strip():
                    ALlocales.seek (i*tamReg, 0)
                    pickle.dump(auxj, ALlocales)
                    ALlocales.seek (j*tamReg, 0)
                    pickle.dump(auxi,ALlocales)
                    ALlocales.flush()

def maymenLocal():                     #Ordenamiento de mayor a menor de los rubros contados
    for y in range (0,2):
        for z in range(y+1,3):
            if regcantrub[y].cant < regcantrub[z].cant:
                auxc=regcantrub[y].cant
                regcantrub[y].cant = regcantrub[z].cant
                regcantrub[z].cant = auxc
                auxr = regcantrub[y].rubro
                regcantrub[y].rubro = regcantrub[z].rubro
                regcantrub[z].rubro=auxr
    for y in range (0,3):
        print("Rubro:",regcantrub[y].rubro,"Cantidad:",regcantrub[y].cant)  #Seria bueno formatearlo como una lista
    time.sleep(3)

def valModifLoc():
    b("cls")
    cprint.info("Ingrese el codigo del local a modificar:")
    cod = input()
    while s(cod, 1, cantreg()):
        cprint.warn("\nEl codigo del local no existe.")
        cprint.info("\nQuieres ingresar un nuevo codigo de local? Ingrese (si) o (no).")
        if valSioNo() == "si":
            b("cls")
            cprint.info("Ingrese el codigo del local a modificar:")
            cod = input()
        else:
            return -1
    cod = int(cod)
    ALlocales.seek(0,0)
    pos = 0
    regloc = pickle.load(ALlocales)
    while ALlocales.tell() < os.path.getsize(AFlocales) and regloc.codloc != cod:
        pos = ALlocales.tell()
        regloc = pickle.load(ALlocales)
    return pos

def valElimLocal():
    b("cls")
    cprint.info("Ingrese el codigo del local a eliminar:")
    cod = input()
    while s(cod, 1, cantreg()):
        cprint.warn("\nEl codigo del local no existe.")
        cprint.info("\nQuieres ingresar un nuevo codigo de local? Ingrese (si) o (no).")
        if valSioNo() == "si":
            b("cls")
            cprint.info("Ingrese el codigo del local a eliminar:")
            cod = input()
        else:
            return -1
    cod = int(cod)
    ALlocales.seek(0,0)
    pos = 0
    regloc = pickle.load(ALlocales)
    while ALlocales.tell() < os.path.getsize(AFlocales) and regloc.codloc != cod:
        pos = ALlocales.tell()
        regloc = pickle.load(ALlocales)
    return pos

def ingresoLocal():             #Creacion de locales
    ordLoc()
    print("termina actualiza")
    cprint.info("\nIngrese el nombre del local o * para salir(maximo 50 caracteres): ")
    nombre = input()
    if nombre != "*":
        while validartam(50,nombre) or (busqdico(nombre) != -1):
            b("cls")
            if validartam(50,nombre):
                cprint.warn("\nSe excedio el tamano, ingrese el nombre nuevamente: ")
            else:
                cprint.warn("\nEste nombre ya existe, ingrese uno diferente (maximo 50 caracteres): ")
            nombre = input()
        b("cls")
        while nombre!="*":
            cprint.info("\nIngrese la ubicacion del local: ")
            ubicacion = input() 
            while validartam(50,ubicacion):
                b("cls")
                cprint.warn("\nSe excedio el tamano, ingrese la ubicacion nuevamente: ")
                ubicacion = input()
            b("cls")
            valRubro()
            b("cls")
            cprint.info("\nIngrese el codigo de usuario de algun dueno: ")
            codueno=input()
            while s(codueno,1,100):
                b("cls")
                cprint.warn("\nIngrese solo valores numericos entre 1 y 100: ")
                codueno=input()
            codueno=int(codueno)
            if (valcodDue(codueno) != -1):
                guardalocal(cantreg() + 1, nombre, ubicacion, rubro, codueno, "A", os.path.getsize(AFlocales))
                sumresmatriz(rubro, 1)
                b("cls")
                cprint.ok("\nEl local se ha creado correctamente.")
            else:
                b("cls")
                cprint.err("\nCodigo incorrecto o inexistente.")
            cprint.info("\nIngrese el nombre del siguiente local a crear o * para terminar: ")
            nombre=input()
            if nombre != "*":
                while validartam(50,nombre) or (busqdico(nombre) != -1):
                    b("cls")
                    if validartam(50,nombre):
                        cprint.warn("\nSe excedio el tamano, ingrese el nombre nuevamente: ")
                    else:
                        cprint.warn("\nEste nombre ya existe, ingrese uno diferente (maximo 50 caracteres): ")
                    nombre = input()
            b("cls")
    b("cls")
    #actualizamatriz()
    maymenLocal()
    ordLoc()
    listalocales()

def menmodifLocal():                     #Menu de modificar locales
    if archnull():
        pos = valModifLoc()
        ALlocales.seek(pos,0)
        regloc = pickle.load(ALlocales)
        print(pos,os.path.getsize(AFlocales))
        b("cls")
        if pos != -1:
            if regloc.estado == "B":
                b("cls")
                cprint.info("\nPara modificar el local debes primero darlo de alta, quieres hacerlo? Ingresar si o no.")
                if valSioNo() == "si":                    
                    regloc.estado = "A"
                    sumresmatriz(regloc.rubloc.strip(), 1)
            if regloc.estado == "A":
                b("cls")
                cprint.info("\n1. Cambiar nombre.\n2. Cambiar ubicacion.\n3. Cambiar rubro.\n0. Salir.")
                op = input("\t")
                while s(op,0,3):
                    b("cls")
                    cprint.warn("\nSe ah ingresado una opcion invalida, vuela a intentarlo (recuerde que es un numero entre 0 y 3).")
                    cprint.info("\n1. Cambiar nombre.\n2. Cambiar ubicacion.\n3. Cambiar rubro.\n0. Salir.")
                    op = input("\t")
                op = int(op)
                while op !=0:
                    b("cls")
                    if op == 1:
                        print("\nIngrese el nuevo nombre del local (maximo 50 caracteres): ")
                        nombre = input()
                        while validartam(50,nombre) or (busqdico(nombre) != -1):
                            b("cls")
                            if validartam(50,nombre):
                                print("\nSe excedio el tamano, ingrese el nombre nuevamente: ")
                            else:
                                print("\nEste nombre ya existe, ingrese uno diferente (maximo 50 caracteres): ")
                            nombre = input()
                        regloc.nomloc = nombre
                    elif op == 2:
                        print("\nIngrese la nueva ubicacion del local (maximo 50 caracteres): ")
                        ubicacion = input()
                        while validartam(50,ubicacion):
                            b("cls")
                            print("\nSe excedio el tamano, ingrese la ubicacion nuevamente: ")
                            ubicacion = input()
                        regloc.ubiloc = ubicacion
                    elif op == 3:
                        valRubro()
                        sumresmatriz(regloc.rubloc.strip(), -1)
                        sumresmatriz(rubro, 1)
                        b("cls")
                        regloc.rubloc = rubro
                    b("cls")
                    print("\nSeleccione la opcion del menu que desee realizar.\n\n1. Cambiar nombre.\n2. Cambiar ubicacion.\n3. Cambiar rubro.\n0. Salir.")
                    op = input("\n\t")
                    while s(op,0,3):
                        b("cls")
                        print("\nSe ah ingresado una opcion invalida, vuela a intentarlo (recuerde que es un numero entre 0 y 3).")
                        print("\nSeleccione la opcion del menu que desee realizar.\n\n1. Cambiar nombre.\n2. Cambiar ubicacion.\n3. Cambiar rubro.\n0. Salir.")
                        op=input("\t")
                    b("cls")
                    op = int(op)
                guardalocal(regloc.codloc, regloc.nomloc, regloc.ubiloc, regloc.rubloc, regloc.codus, "A", pos)
                ordLoc()
                listalocales()
                maymenLocal()

def elimlocal():
    if archnull():
        pos = valElimLocal()
        ALlocales.seek(pos,0)
        regloc = pickle.load(ALlocales)
        if regloc.estado == "A":
            cprint.warn("Estas seguro de querer eliminar el local?")
            if valSioNo() == "si":
                guardalocal(regloc.codloc, regloc.nomloc, regloc.ubiloc, regloc.rubloc, regloc.codus, "B", pos)
                cprint.ok("\nEl local ha sido eliminado correctamente.\n")
                sumresmatriz(regloc.rubloc.strip(), -1)
                listalocales()
    maymenLocal()

def actualizamatriz():
    ALlocales.seek(0,0)
    tam = os.path.getsize(AFlocales)
    while ALlocales.tell() < tam:
        regloc = pickle.load(ALlocales)
        for i in range(0,3):
            if regloc.rubloc.strip() == regcantrub[i].rubro and regloc.estado == "A":
                regcantrub[i].cant = regcantrub[i].cant + 1
    for i in range(0,3):
        print("rubro:",regcantrub[i].rubro,"cantidad:",regcantrub[i].cant)

def maymenLocal():                     #Ordenamiento de mayor a menor de los rubros contados
    for i in range (0,2):
        for j in range(i+1,3):
            if regcantrub[i].cant < regcantrub[j].cant:
                aux = regcantrub[i]
                regcantrub[i] = regcantrub[j]
                regcantrub[j]= aux
    for i in range (0,3):
        print("Rubro:",regcantrub[i].rubro,"Cantidad:",regcantrub[i].cant)  #Seria bueno formatearlo como una lista
    time.sleep(3)

def sumresmatriz(rubro, sumres):
    for i in range(0,3):
        if rubro == regcantrub[i].rubro:
            regcantrub[i].cant = regcantrub[i].cant + sumres

def mapa():                     #Mapa de locales
    for i in range (0,50): #Limpia el mapa
        maparray[i] = '\033[0;33m'+"0"+'\033[0;34m'
    i = 0
    ALlocales.seek(0,0)
    while ALlocales.tell() < os.path.getsize(AFlocales): #Carga el mapa segun cantidad de registros
        regloc = pickle.load(ALlocales)
        if regloc.estado == "A":
            maparray[i] = '\033[0;32m'+str(regloc.codloc)+'\033[0;34m'
        else:
            maparray[i] = '\033[0;31m'+str(regloc.codloc)+'\033[0;34m'
        i = i + 1
    m=0
    contenido = '\033[0;34m'+"| {:^18s} | {:^18s} | {:^18s} | {:^18s} | {:^18s} |"+'\033[0m'
    simbolos = '\033[0;34m'+"+------"*5+"+"+'\033[0m'
    for l in range (10):
        print(simbolos)
        print(contenido.format(maparray[m],maparray[m+1],maparray[m+2],maparray[m+3],maparray[m+4]))
        m=m+5
    print(simbolos)
    print("Próximamente se habilitará un mapa con los demás locales...")
    decis=input("\nIngrese * para cerrar el mapa: ")
    while decis!="*":
        decis= input("\nIngrese * para cerrar el mapa: ")

