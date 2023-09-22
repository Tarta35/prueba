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
from usuarios import verifusuario, verifcontra, guardauser, AFusuarios, ALusuarios, cantregus, regus
from carteles import switchCarteles, mapa, enConstrucc
from locales import ordLoc, listalocales, validartam, cantreg, menmodifLocal, ingresoLocal, elimlocal, actualizamatriz, mapa
from rutas import rutaluciano as ruta



global Cuentas
Cuentas = [[""]*3 for i in range (100)]      #Def anterior de arrays (dejar por ahora)
global Locales
Locales = [[""]*4 for i in range(50)]
global Cod
Cod = [0]*100
rubros = [""]*3
rubroscant= [0]*3
rubros[0]= "indumentaria"
rubros[1]= "perfumeria"
rubros[2]= "comida"

def registro(tipocuenta):                          #Registro de una cuenta.
    cprint.info("\nIngrese un correo (maximo 100 caracteres): ")
    nombre=input()
    while (validartam(100,nombre) == False) and (verifusuario(nombre) != -1):
        if validartam(100,nombre):
            b("cls")
            cprint.warn("\nSe excedio el tamano, vuelva a ingresarlo: ")
        else:
            b("cls")
            cprint.warn("\nEl correo ingresado ya esta en uso, por favor ingrese otro: ")
        nombre = input()
    b("cls")
    cprint.info("Ingrese un correo (maximo 100 caracteres): ",nombre)
    cprint.info("\nIngrese una contrasena (maximo 8 caracteres): ")
    contra=getpass("")
    while validartam(8,contra):
        b("cls")
        cprint.info("Ingrese un correo (maximo 100 caracteres): ",contra)
        cprint.warn("\nSe excedio el tamano, vuelva a ingresarlo: ")
        contra=getpass("")
    cod = cantregus() + 1
    tipous = tipocuenta

    guardauser(cod, nombre, contra, tipous)

    b("cls")
    cprint.ok("\nSu cuenta se ha creado correctamente.")
    cprint.ok("\nSu codigo de usuario es: ",cod)
    time.sleep(5)
    b("cls")

def ingreso():                              #Ingreso de un usuario.

    b("cls")
    cprint.info("\nIngrese su correo o * para salir: ")
    usuario= input()

    while verifusuario(usuario)==-1 and usuario!="*":
        b("cls")
        cprint.warn("\nUsuario incorrecto, ingreselo nuevamente o * para salir: ")
        usuario= input()

    if usuario!="*":
        cprint.info("\nIngrese su contrasena o * para salir: ")
        contrasena= getpass("")
        intentos=2
        b("cls")

        while contrasena!="*" and verifcontra(usuario, contrasena) == -1 and intentos!=0:
            cprint.info("\nIngrese su correo o * para salir: ",usuario)
            cprint.warn("\nLa contrasena ingresada es incorrecta, le quedan",intentos,"intentos. Ingrese su contrasena nuevamente o * para salir: \n\t")
            contrasena= getpass("")
            time.sleep(0.5)
            b("cls")
            if contrasena == '*':
                return 2
            intentos=intentos-1

        if intentos == 0:
            return 1
        else:
            return verifusuario(usuario)
    else:
        b("cls")
        return 2
    
def MenuAd():                               #Menu del admin.
    opc = 6
    while opc != 0:
        switchCarteles(6)
        opc = int(leerOpc())
        if opc == 1:
            b("cls")
            switchCarteles(1)
            subopc = leerSubOpc1()
            b("cls")
        elif opc == 2:
            b("cls")
            registro("dueno")
            b("cls")
        elif opc == 4:
            b("cls")
            switchCarteles(4)
            cprint.info("\nSeleccione una opcion del nuevo menu: ")
            subopc = input()
            b("cls")
            cprint.ok("\nLas opciones de este menu solo estan desarrolladas en chapin, volvera al menu prinicipal.")
            time.sleep(3)
            b("cls")
        else:
            b("cls")
            switchCarteles(opc)

def leerOpc():                             #Lectura de la opcion deseada en el menu admin  (en revision)
    cprint.info("\nSeleccione la accion a realizar: ")
    opc = input()
    
    while not(opc.isdigit()) or opc < "0" or opc > "5":
        b("cls")
        cprint.warn("\nNo se ha escogido una opcion valida, vuelva a intentar.")
        switchCarteles(6)
        cprint.info("\nSeleccione la accion a realizar: ")
        opc = input()

    return opc

def leerSubOpc1():        #Lectura de la opcion deseada en el submenu del menu admin

    cprint.info("\nSeleccione una opcion del nuevo menu: ")
    subopc = input()
    while subopc!="a" and subopc!="b" and subopc!="c" and subopc!="d" and subopc!="e":
        b("cls")
        cprint.warn("\nNo se ha escogido una opcion valida, vuelva a intentar.")
        switchCarteles(1)
        cprint.warn("\nSeleccione una opcion valida: ")
        subopc=input()

    if subopc >= 'a' and subopc <= 'c':
        listalocales()

    if subopc == 'a':
        b("cls")
        ingresoLocal()
        ordLoc()
    elif subopc == 'b':
        b("cls")
        ordLoc()
        menmodifLocal()
    elif subopc == 'c':
        b("cls")
        ordLoc()
        elimlocal()
        ordLoc()
    elif subopc == 'd':
        b("cls")
        ordLoc()
        mapa()
    
    return subopc
    
def sistema():                     #Sistema principal
    actualizamatriz() #Cargo la matriz de cantidad de rubros aqui, asi funciona como un registro que no pierde los datos.
    b("cls")
    decision="0"
    while decision!="3":
        cprint.info("\nSeleccione una de las siguientes opciones:\n\n1. Ingresar con usuario registrado\n2. Registrarse como cliente\n3. Salir\n\t")
        decision=input()
        while decision!="1" and decision!="2" and decision!="3":
            b("cls")
            cprint.info("\nSeleccione una de las siguientes opciones:\n\n1. Ingresar con usuario registrado\n2. Registrarse como cliente\n3. Salir\n\t")
            decision=input()
        if decision == "2":
            b("cls")
            cprint.info("Seleccione el tipo de usuario que desea crear: ")
            tipouser = input()
            registro(tipouser)
        elif decision == "1":
            x = ingreso()
            if x==1:
                cprint.err("Se alcanzo el maximo de intentos.")
                decision = "3"
            elif x != 2:
                ALusuarios.seek(x,0)
                regus = pickle.load(ALusuarios)
                cprint.ok("\nEl codigo de usuario del usuario con correo: ",regus.nomus.strip()," es: ",regus.codus.strip(),".")
                if regus.tipous.strip() == 'administrador': 
                    MenuAd()
                elif regus.tipous.strip() == 'dueno':
                    enConstrucc()
                    #MenuDue()
                else:
                    enConstrucc()
                    #MenuCli()

    cprint.ok("¡Hasta luego!")

ALusuarios.seek(0,0)
while ALusuarios.tell() < os.path.getsize(AFusuarios):
    regus = pickle.load(ALusuarios)
    print("Usuario:",regus.nomus,"Contrasena:",regus.claveus,"Codigo:",regus.codus,"Usuario:",regus.tipous)


sistema()