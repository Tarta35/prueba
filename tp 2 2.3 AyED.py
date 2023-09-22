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

##########################################
global Cuentas
Cuentas = [[""]*3 for i in range (100)]      #Def anterior de arrays (dejar por ahora)
global Locales
Locales = [[""]*4 for i in range(50)]
global Cod
Cod = [0]*100
global Codl
Codl = [0]*50
rubros = [""]*3
rubroscant= [0]*3
rubros[0]= "indumentaria"
rubros[1]= "perfumeria"
rubros[2]= "comida"
rutaenri = "C:\\Enri\\unt ins\\"
##########################################


#Definicion de Class y Registros

class Usuarios:
    def __init__(self):
        self.codus=0
        self.nomus=" "
        self.claveus=" "
        self.tipous=" "

class Locales:
    def __init__(self):
        self.codloc=0
        self.nomloc=""
        self.ubiloc=""
        self.rubloc=""
        self.codus = 0
        self.estado="" #Tipo Char

class Promociones:
    def __init__(self):
        self.codpromo=0
        self.txtpromo=""
        self.fechadesdepromo="" #Son iguales a date en el pdf, revisar
        self.fechahastapromo="" #Son iguales a date en el pdf, revisar
        self.diasemana= [0]*7
        self.estado=""
        self.codloc=0

class UsoPromociones:
    def __init__(self):
        self.codcli=0
        self.codpromo=0
        self.fechausopromo="" #Son iguales a date en el pdf, revisar

class Novedades:
    def __init__(self):
        self.codnov=0
        self.txtnov=""
        self.fechadesdenov="" #Son iguales a date en el pdf, revisar
        self.fechahastanov="" #Son iguales a date en el pdf, revisar
        self.tipous=""
        self.estado="" #Tipo Char

class CantRub:
    def __init__(self):
        self.rubro = ""
        self.cant = 0

regus= Usuarios()
regloc=Locales()
regpromo=Promociones()
regusopromo=UsoPromociones()
regnov=Novedades()
regcantrub=[CantRub()]*3
for i in range (0,2):
    regcantrub[i].cant = 0
regcantrub[0].rubro = "indumentaria"
regcantrub[1].rubro = "perfumeria"
regcantrub[2].rubro = "comida"

#Formateos

def formateo_usuarios():
    regus.codus= str(regus.codus)
    regus.codus= regus.codus.ljust(3, ' ')
    regus.nomus= regus.nomus.ljust(100, ' ')
    regus.claveus= regus.claveus.ljust(8, ' ')
    regus.tipous= regus.tipous.ljust(1, ' ')

def formateo_locales():
    regloc.codloc= str(regloc.codloc)
    regloc.codloc= regloc.codloc.ljust(3, " ")
    regloc.nomloc= regloc.nomloc.ljust(50, " ")
    regloc.rubloc= regloc.rubloc.ljust(50, " ")
    regloc.codus= str(regloc.codus)
    regloc.codus= regloc.codus.ljust(3, " ")
    #Por si acaso no hice el formateo de estado ya que es char y todos son de mismo tamaño

def formateo_promociones():
    regpromo.codpromo= str(regpromo.codpromo)
    regpromo.txtpromo= regpromo.txtpromo.ljust(200, "")
    regpromo.fechadesdepromo= regpromo.fechadesdepromo.ljust(10, "") #Defino los fecha porque si bien se guardan como date
    regpromo.fechahastapromo= regpromo.fechahastapromo.ljust(10, "") #a lo mejor la funcion devuelve una string (10 pero cambiable)
    for i in range (0,7): #No formateo el tamaño del array ya que se supone todos son del mismo tamaño (1)
        regpromo.diasemana[i]= str(regpromo.diasemana[i])
    regpromo.estado= regpromo.estado.ljust(10, "")
    regpromo.codloc= str(regpromo.codloc)
    regpromo.codloc= regpromo.codloc.ljust(3, "")

def formateouso_promociones():
    regusopromo.codcli= str(regusopromo.codcli)
    regusopromo.codcli= regusopromo.codcli(3, "")
    regusopromo.codpromo= str(regusopromo.codpromo)
    regusopromo.codpromo= regusopromo.codpromo.ljust(3, "")
    regusopromo.fechausopromo= regusopromo.fechausopromo.ljust(10, "")
    #Lo formateo con 10 porq posiblemente eso devuelva el tipo de dato date

def formateo_novedades():
    regnov.codnov= str(regnov.codnov)
    regnov.codnov= regnov.codnov.ljust(3, "")
    regnov.fechadesdenov= regnov.fechadesdenov.ljust(10, "")
    regnov.fechahastanov= regnov.fechahastanov.ljust(10, "")
    regnov.tipous= regnov.tipous.ljust(20, "")
    #No definimos estado ya que es tipo char
    #Nuevamente la fecha la definimos con tamaño 10 por ahora

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

def enConstrucc():                             #.
    cprint.ok("\nEn construccion...")
    time.sleep(3)
    b("cls")

def mostrarLocales():
        tam = os.path.getsize(AFlocales)
        if tam > 0:
            ALlocales.seek(0,0)
            b("cls")
            cprint.ok("Lista de locales actualmente existentes.\n\n")
            while ALlocales.tell() < tam:
                regloc = pickle.load(ALlocales)
                cprint.ok("\nCodigo del local: ",regloc.codloc)
                cprint.ok("Codigo del local: ",regloc.nomloc)
                cprint.ok("Codigo del local: ",regloc.ubiloc)
                cprint.ok("Codigo del local: ",regloc.rubloc)
                cprint.ok("Codigo del local: ",regloc.codus)
                cprint.ok("Codigo del local: ",regloc.estado)
        cprint.ok("Ingrese * para cerrar la lista de locales.")
        decis = input()
        while decis != '*':
            cprint.ok("Ingrese * para cerrar la lista de locales.")
            decis = input()


def tamreg(AF, AL):
    if os.path.getsize(AF) > 0:
        AL.seek(0,0)
        aux = pickle.load(AL)
        t = int(AL.tell())
        return t

def cantreg(AF, AL):
    if os.path.getsize(AF) > 0:
        AL.seek(0,0)
        aux = pickle.load(AL)
        tamReg = AL.tell()
        tamArch = os.path.getsize(AF)
        t = round(tamArch/tamReg)
        return t
    return 0

def verifusuario(dato):                #Devuelve la posicion en la que se encuentra un nombre o -1.
    tam = os.path.getsize(AFusuarios)
    pos = 0
    ALusuarios.seek(0,0)
    while ALusuarios.tell() < tam:
        pos = ALusuarios.tell()
        regus = pickle.load(ALusuarios)
        if regus.nomus.strip() == dato:
            return pos
    return -1

def verifcontra(user, contra):                  #Devuelve la posicion en la que se encuentra un nombre o -1.
    pos = verifusuario(user)
    ALusuarios.seek(pos,0)
    regus = pickle.load(ALusuarios)
    if regus.claveus.strip() != contra:
        return -1
    return pos

def guardauser(codus, nomus, claveus, tipous):          #Guarda un usuario en el archivo
    ALusuarios.seek(0,2)
    regus.codus = codus
    regus.nomus = nomus
    regus.claveus = claveus
    regus.tipous = tipous
    formateo_usuarios()
    pickle.dump(regus, ALusuarios)
    ALusuarios.flush()

def registro(rub):                       #Registro de una cuenta.
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
    contra=input()
    while validartam(8,contra):
        b("cls")
        cprint.info("Ingrese un correo (maximo 100 caracteres): ",contra)
        cprint.warn("\nSe excedio el tamano, vuelva a ingresarlo: ")
        contra=input()
    
    cod = cantreg(AFusuarios, ALusuarios) + 1
    tipous = rub

    guardauser(cod, nombre, contra, tipous)

    b("cls")
    cprint.ok("\nSu cuenta se ha creado correctamente.")
    cprint.ok("\nSu codigo de usuario es: ",cod)
    time.sleep(5)
    b("cls")

def ingreso():       #Ingreso de un usuario.

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

def MenuAd():                        #Menu del admin.
    opc = 6
    while opc != 0:
        switchCarteles(6)
        opc = int(leerOpc())
        if opc == 1:
            b("cls")
            switchCarteles(1)
            subopc = leerSubOpc1()
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

def MenuDue():                        #Menu del dueño.
    mendue="t"
    while mendue!="0":
        b("cls")
        cprint.info("\nIngrese una opcion del nuevo menu: \n1. Gestion de locales\n   a) Crear descuento para mi local\n   b) Modificar descuento de mi local\n   c) Eliminar descuento de mi local\n   d) Volver\n2. Aceptar/Rechazar pedido de descuento\n3. Reporte de uso de descuentos\n0. Salir")
        mendue=input("\n\t")
        b("cls")
        while mendue!="a" and mendue!="b" and mendue!="c" and mendue!="d" and mendue!="2" and mendue!="3" and mendue!="0":
            cprint.warn("\nLa opcion ingresada no es valida, se volvera a desplegar el menu.")
            time.sleep(0.5)
            b("cls")
            cprint.warn("\nIngrese una opcion valida (letras minusculas de la (a) a la (e), 0, 2 o 3):")
            cprint.info("\n\n1. Gestion de locales\n   a) Crear descuento para mi local\n   b) Modificar descuento de mi local\n   c) Eliminar descuento de mi local\n   d) Volver\n2. Aceptar/Rechazar pedido de descuento\n3. Reporte de uso de descuentos\n0. Salir.\n\t")
            mendue=input()
            b("cls")
        if mendue!="0":
            enConstrucc()

def MenuCli():                       #Menu del cliente.
    mencli="t"
    while mencli!="0":
        cprint.info("\n1. Registrarme\n2. Buscar descuentos de locales\n3. Solicitar descuento\n4. Ver novedades\n0. Salir")     
        cprint.info("\nIngrese una opcion: ")
        mencli=input()
        while mencli!="1" and mencli!="2" and mencli!="3" and mencli!="4" and mencli!="0":
            cprint.info("\n1. Registrarme\n2. Buscar descuentos de locales\n3. Solicitar descuento\n4. Ver novedades\n0. Salir")            
            cprint.warn("\nIngrese una opcion valida: ")
            mencli=input()
        if mencli!="0":
            b("cls")
            enConstrucc()
        else:
            b("cls")

def leerOpc():                    #Lectura de la opcion deseada en el menu admin  (en revision)
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
        mostrarLocales()

    if subopc == 'a':
        b("cls")
        ingresoLocal()
        ordReg(AFlocales, ALlocales, "nomloc")
    elif subopc == 'b':
        b("cls")
        ordReg(AFlocales, ALlocales, "nomloc")
        menmodifLocal()
        ordReg(AFlocales, ALlocales, "nomloc")
    elif subopc == 'c':
        b("cls")
        ordReg(AFlocales, ALlocales, "nomloc")
        elimLocal()
        ordReg(AFlocales, ALlocales, "nomloc")
    elif subopc == 'd':
        b("cls")
        mapa()
    
    return subopc

def listalocales():               #Printeo de locales en forma de lista

    b("cls")
    print("¿Desea ver locales ya existentes? Si o No: ")
    decis= valSioNo()
    if decis=="si":
        while decis!="*":
            b("cls")
            print("| {:^35s} | {:^12s} | {:^13s} | {:^13s} | {:^6s} |".format("Nombre Local","Ubicacion","Rubro","Acceso","Codigo"))
            for w in range(50):
                print("-"*95)
                print("| {:^35s} | {:^12s} | {:^13s} | {:^13s} | {:^6.0f} |".format(Locales[w][0],Locales[w][1],Locales[w][2],Locales[w][3],Codl[w]))
            print("-"*95)
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
    if os.path.getsize(AFlocales) > 0:
        tamReg = tamreg(AFlocales, ALlocales)
        cantReg = cantreg(AFlocales, ALlocales)
        desde = 0
        hasta = cantReg - 1    
        medio = (desde + hasta) // 2
        ALlocales.seek(medio*tamReg, 0)
        regloc = pickle.load(ALlocales)
        while regloc.nomloc.strip() != dato and desde < hasta:
            if dato < regloc.nomloc.strip():
                hasta = medio - 1
            else:
                desde = medio + 1
            medio = (desde + hasta) // 2

        if regloc.nomloc.strip() == dato:						
            return medio * tamReg							
        else:
            return -1
    else:
        return -1

def ordReg(AF, AL, campo):
    if os.path.getsize(AF) > 0:
        tamReg = tamreg(AF, AL)
        tamArch = os.path.getsize(AF)
        cantReg = int(tamArch / tamReg)  
        for i in range(0, cantReg-1):
            for j in range (i+1, cantReg):
                AL.seek (i*tamReg, 0)
                auxi = pickle.load(AL)
                AL.seek (j*tamReg, 0)
                auxj = pickle.load(AL)
                if auxi.nomloc.strip() > auxj.nomloc.strip():
                    AL.seek (i*tamReg, 0)
                    pickle.dump(auxj, AL)
                    AL.seek (j*tamReg, 0)
                    pickle.dump(auxi,AL)
                    AL.flush()

def valcodDue(cod):
    tam = os.path.getsize(AFusuarios)
    pos = 0
    ALusuarios.seek(0,0)
    while ALusuarios.tell() < tam:
        pos = ALusuarios.tell()
        regus = pickle.load(ALusuarios)
        if int(regus.codus) == cod and regus.tipous.strip() == 'dueno':
            return pos
    return -1

def ingresoLocal():             #Creacion de locales
    
    ordReg(AFlocales, ALlocales, "nomloc")

    cprint.info("\nIngrese el nombre del local o * para salir(maximo 50 caracteres): ")
    nombre = input()
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
            regloc.codloc = 0
            regloc.nomloc = nombre
            regloc.ubiloc = ubicacion
            regloc.rubloc = rubro
            regloc.codus = cantreg(AFlocales, ALlocales) + 1
            regloc.estado = "A"
            formateo_locales()
            ALlocales.seek(0,2)
            pickle.dump(regloc, ALlocales)
            ALlocales.flush()

            if regcantrub[0].rubro == rubro:
                regcantrub[0].cant = regcantrub[0].cant + 1
            elif regcantrub[1].rubro == rubro:
                    regcantrub[1].cant = regcantrub[1].cant + 1
            else:
                    regcantrub[2].cant = regcantrub[2].cant + 1

            b("cls")
            cprint.ok("\nEl local se ha creado correctamente.")     
        else:
            b("cls")
            cprint.err("\nCodigo incorrecto o inexistente.")
        cprint.info("\nIngrese el nombre del siguiente local a crear o * para terminar: ")
        nombre=input()
        while validartam(50,nombre) or (busqdico(nombre) != -1):
            b("cls")
            if validartam(50,nombre):
                cprint.warn("\nSe excedio el tamano, ingrese el nombre nuevamente: ")
            else:
                cprint.warn("\nEste nombre ya existe, ingrese uno diferente (maximo 50 caracteres): ")
            nombre = input()
        b("cls")
    b("cls")
    maymenLocal()

def valSioNo():
    decis=input("\n\t")
    while decis!="si" and decis!="no":
        cprint.info("Ingrese solo (si) o (no), ")
        decis=input()
    return decis

def menmodifLocal():                     #Menu de modificar locales

    i = valModifLoc() 
    b("cls")
    if i == -1:
        print("\nEn codigo del local no existe.")
        print("\nQuieres ingresar un nuevo codigo de local? Ingrese (si) o (no).")
        if valSioNo() == "si":
            b("cls")
            valModifLoc()
    else:
        if Locales[i][3] == "B":
            b("cls")
            print("\nPara modificar el local debes primero darlo de alta, quieres hacerlo? Ingresar si o no.")
            if valSioNo() == "si":
                Locales[i][3] = "A"
                indrubro=verifdato(Locales[i][2],3,rubros)
                rubroscant[indrubro]= rubroscant[indrubro]+1
        if Locales[i][3] == "A":
            b("cls")
            print("\n1. Cambiar nombre.\n2. Cambiar ubicacion.\n3. Cambiar rubro.\n0. Salir.")
            op = input("\t")
            while s(op,0,3):
                b("cls")
                print("\nSe ah ingresado una opcion invalida, vuela a intentarlo (recuerde que es un numero entre 0 y 3).")
                print("\n1. Cambiar nombre.\n2. Cambiar ubicacion.\n3. Cambiar rubro.\n0. Salir.")
                op=input("\t")
            op = int(op)
            while op !=0:
                b("cls")
                if op == 1:
                    print("\nIngrese el nuevo nombre del local (maximo 50 caracteres): ")
                    nombre = input()
                    loc=verifespacio(50,Locales)
                    ordenamiento(loc)
                    while validartam(50,nombre) or busqdico(Locales,loc,nombre):
                        b("cls")
                        if validartam(50,nombre):
                            print("\nSe excedio el tamano, ingrese el nombre nuevamente: ")
                        else:
                            print("\nEste nombre ya existe, ingrese uno diferente (maximo 50 caracteres): ")
                        nombre = input()
                    Locales[i][0] = nombre
                elif op == 2:
                    print("\nIngrese la nueva ubicacion del local (maximo 50 caracteres): ")
                    ubicacion = input()
                    while validartam(50,ubicacion):
                        b("cls")
                        print("\nSe excedio el tamano, ingrese la ubicacion nuevamente: ")
                        ubicacion = input()
                    Locales[i][1] = ubicacion
                elif op == 3:
                    valRubro()
                    b("cls")
                    indrubro=verifdato(Locales[i][2],3,rubros)
                    rubroscant[indrubro]= rubroscant[indrubro] - 1
                    indrubro=verifdato(rubro,3,rubros)
                    rubroscant[indrubro]= rubroscant[indrubro] + 1
                    Locales[i][2] = rubro
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

def elimLocal():                      #Menu de eliminar locales 
    b("cls")
    codloc=input("Ingrese el codigo del local a eliminar: ")
    while s(codloc,1,50):
        b("cls")
        codloc=input("Ingrese solo numeros entre el 1 y el 50: ")
    codloc=int(codloc)
    w = verifcod(codloc,50,Codl)
    if w!=-1:
        if Locales[w][3]=="A":
            b("cls")
            decis = input("\nSe solicita confirmacion para eliminar el local, ingrese 1 para elimiar o 2 para cancelar la operacion: ")
            while decis != "1" and decis != "2":
                b("cls")
                print("\nSe solicita confirmacion para eliminar el local, ingrese 1 para elimiar o 2 para cancelar la operacion: ")
                decis = input("Solo ingree (1) o (2): ")
            if decis == "1":
                b("cls")
                Locales[w][3]="B"
                print("\nEl local se ha dado de baja con exito.")
                indrubro=verifdato(Locales[w][2],3,rubros)
                rubroscant[indrubro]= rubroscant[indrubro]-1
        else:
            b("cls")
            print("El local ya esta de baja.")
            time.sleep(2)
    else:
        b("cls")
        print("No se encontro ningun local con el codigo ingresado.")
        time.sleep(2)

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

def sistema():                     #Sistema principal
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
            elif x != 2:
                ALusuarios.seek(x,0)
                regus = pickle.load(ALusuarios)
                cprint.ok("\nEl codigo de usuario del usuario con correo: ",regus.nomus.strip()," es: ",regus.codus.strip(),".")
                if regus.tipous.strip() == 'administrador': 
                    MenuAd()
                elif regus.tipous.strip() == 'dueno':
                    MenuDue()
                else:
                    MenuCli()

    cprint.ok("¡Hasta luego!")

def validartam(tam, dato):                          #Valida que el string ingresado sea del tamaño limitado.
    if len(dato)>tam:
        return True
    else:
        return False

#Las siguientes funciones hasta enConstrucc son prints

def mostrarLocales2():
        tam = os.path.getsize(AFlocales)
        if tam > 0:
            ALlocales.seek(0,0)
            b("cls")
            print("Lista de locales actualmente existentes.\n\n")
            while ALlocales.tell() < tam:
                regloc = pickle.load(ALlocales)
                print("\nCodigo del local: ",regloc.codloc)
                print("Codigo del local: ",regloc.nomloc)
                print("Codigo del local: ",regloc.ubiloc)
                print("Codigo del local: ",regloc.rubloc)
                print("Codigo del local: ",regloc.codus)
                print("Codigo del local: ",regloc.estado)

def switchCarteles2(opc):             #Diferentes prints a mostrar del menu de admin.

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

def cartelAdmin2():               #.
    print("\n1. Gestion de locales.\n2. Crear cuentas de duenos de locales\n3. Aprobar / Denegar solicitud de descuento\n4. Gestion de novedades\n5. Reporte de utilizacion de descuentos\n0. Salir\n")

def cartelGestLocales2():                  #Cartel para el menu de gestion de locales.
    print('1. Gestion de locales.\n\n\ta) Crear locales\n\tb) Modificar local\n\tc) Eliminar local\n\td) Mapa de Locales\n\te) Volver')

def cartelGestNov2():                 #.
    print('\n\ta) Crear novedades\n\tb) Modificar novedad\n\tc) Eliminar novedad\n\td) Volver\n')

def enConstrucc2():                             #.
    print("\nEn construccion...")
    time.sleep(3)
    b("cls")

def maymenLocal():                     #Ordenamiento de mayor a menor de los rubros contados
    for y in range (0,2):
        for z in range(y+1,3):
            if regcantrub[y].cant<regcantrub[z].cant:
                auxc=regcantrub[y]
                regcantrub[y]=regcantrub[z]
                regcantrub[z]=auxc
    print("Rubro con mayor cantidad de locales: ",regcantrub[0].rubro,"cantidad de locales del rubro: ",regcantrub[0].cant)
    print("El rubro: ",regcantrub[1].rubro,"tiene: ",regcantrub[1].cant, "locales creados")
    print("El rubro: ",regcantrub[2].rubro,"tiene: ",regcantrub[2].cant, "locales creados")
    time.sleep(3)


#Programa principal y Definicion de archivos

AFusuarios= rutaenri + "tp3\\ALusuarios.dat"
if not os.path.exists(AFusuarios) or (os.path.getsize(AFusuarios) == 0):
    ALusuarios = open(AFusuarios, "w+b")
    ALusuarios.seek(0,0)
    regus.codus= 1
    regus.nomus= "admin@shopping.com"
    regus.claveus= "12345"
    regus.tipous= "administrador"
    formateo_usuarios()
    pickle.dump(regus, ALusuarios)
    ALusuarios.flush()
    regus.codus= 2
    regus.nomus= "enrico"
    regus.claveus= "123"
    regus.tipous= "administrador"
    formateo_usuarios()
    pickle.dump(regus, ALusuarios)
    ALusuarios.flush()
    regus.codus= 3
    regus.nomus= "vitti"
    regus.claveus= "123"
    regus.tipous= "dueno"
    formateo_usuarios()
    pickle.dump(regus, ALusuarios)
    ALusuarios.flush()
else:
    ALusuarios = open(AFusuarios, "r+b")

AFlocales= rutaenri + "tp3\\ALlocales.dat"
if not os.path.exists(AFlocales):
    ALlocales = open(AFlocales, "w+b")
else:
    ALlocales = open(AFlocales, "r+b")

AFpromo= rutaenri + "tp3\\ALpromo.dat"
if not os.path.exists(AFpromo):
    ALpromo = open(AFpromo,"w+b")
else:
    ALpromo = open(AFpromo,"r+b")

AFusopromo= rutaenri + "tp3\\ALusopromo.dat"
if not os.path.exists(AFusopromo):
    ALusopromo = open(AFusopromo,"w+b")
else:
    ALusopromo = open(AFusopromo,"r+b")

AFnovedades= rutaenri + "tp3\\ALnovedades.dat"
if not os.path.exists(AFnovedades):
    ALnovedades = open(AFnovedades,"w+b")
else:
    ALnovedades = open(AFnovedades,"r+b")

def init():
    print("\nesto es para nosotros, pasa saber que usuarios estan ya creados e ingresar rapido\n")
    ALusuarios.seek(0,0)
    tam = os.path.getsize(AFusuarios)
    while ALusuarios.tell() < tam:
        regus = pickle.load(ALusuarios)
        print(regus.nomus.strip())
        print(regus.claveus.strip())
        print(regus.codus.strip())
        print(regus.tipous.strip())
        print("")
    o = ""
    while o != "0":
        o = input("\n\naprieten 0 para que arranque\n\n")

def info():
    cprint("arg") 							# WHITE
    cprint.ok("arg")							# BLUE
    cprint.info("arg")						# GREEN
    cprint.warn("arg")						# YELLOW
    cprint.err("arg", interrupt=False)		# BROWN
    cprint.fatal("arg", interrupt=False)		# RED

#init()
sistema()
info()



ALusuarios.close()
ALlocales.close()
ALusopromo.close()
ALpromo.close()
ALusopromo.close()



