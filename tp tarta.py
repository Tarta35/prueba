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
rutaluciano = "D:\\Familia\\Escritorio\\TP 3 py\\tp archivos prueba\\"
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
    def init(self):
        self.rubro = ""
        self.cant = 0

regus= Usuarios()
regloc=Locales()
regpromo=Promociones()
regusopromo=UsoPromociones()
regnov=Novedades()
regcantrub=[None]*3
for i in range (0,3):
    regcantrub[i] = CantRub()
for i in range (0,3):
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

def tamreg(AF, AL):
    if os.path.getsize(AF) > 0:
        AL.seek(0,0)
        aux = pickle.load(AL)
        t = (AL.tell())
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
    nombre=input("\nIngrese un correo (maximo 100 caracteres): ")
    while (validartam(100,nombre) == False) and (verifusuario(nombre) != -1):
        if validartam(100,nombre):
            b("cls")
            print("\nSe excedio el tamano, vuelva a ingresarlo: ")
        else:
            b("cls")
            print("\nEl correo ingresado ya esta en uso, por favor ingrese otro: ")
        nombre = input()
    b("cls")
    print("Ingrese un correo (maximo 100 caracteres): ",nombre)
    contra=input("\nIngrese una contrasena (maximo 8 caracteres): ")
    while validartam(8,contra):
        b("cls")
        print("Ingrese un correo (maximo 100 caracteres): ",contra)
        contra=input("\nSe excedio el tamano, vuelva a ingresarlo: ")
    
    cod = cantreg(AFusuarios, ALusuarios) + 1
    tipous = rub

    guardauser(cod, nombre, contra, tipous)

    b("cls")
    print("\nSu cuenta se ha creado correctamente.")
    print("\nSu codigo de usuario es: ",cod)
    time.sleep(5)
    b("cls")

def ingreso():       #Ingreso de un usuario.

    b("cls")
    usuario= input("\nIngrese su correo o * para salir: ")

    while verifusuario(usuario)==-1 and usuario!="*":
        b("cls")
        usuario= input("\nUsuario incorrecto, ingreselo nuevamente o * para salir: ")

    if usuario!="*":
        contrasena= getpass("\nIngrese su contrasena o * para salir: ")
        intentos=2
        b("cls")

        while contrasena!="*" and verifcontra(usuario, contrasena) == -1 and intentos!=0:
            print("\nIngrese su correo o * para salir: ",usuario)
            print("\nLa contrasena ingresada es incorrecta, le quedan",intentos,"intentos. Ingrese su contrasena nuevamente o * para salir: ")
            contrasena= getpass("\n\t")
            time.sleep(0.5)
            b("cls")
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
            subopc = input("\nSeleccione una opcion del nuevo menu: ")
            b("cls")
            print("\nLas opciones de este menu solo estan desarrolladas en chapin, volvera al menu prinicipal.")
            time.sleep(3)
            b("cls")
        else:
            b("cls")
            switchCarteles(opc)

def MenuDue():                        #Menu del dueño.
    mendue="t"
    while mendue!="0":
        b("cls")
        print("\nIngrese una opcion del nuevo menu: \n1. Gestion de locales\n   a) Crear descuento para mi local\n   b) Modificar descuento de mi local\n   c) Eliminar descuento de mi local\n   d) Volver\n2. Aceptar/Rechazar pedido de descuento\n3. Reporte de uso de descuentos\n0. Salir")
        mendue=input("\n\t")
        b("cls")
        while mendue!="a" and mendue!="b" and mendue!="c" and mendue!="d" and mendue!="2" and mendue!="3" and mendue!="0":
            print("\nLa opcion ingresada no es valida, se volvera a desplegar el menu.")
            time.sleep(0.5)
            b("cls")
            print("\nIngrese una opcion valida (letras minusculas de la (a) a la (e), 0, 2 o 3): \n\n1. Gestion de locales\n   a) Crear descuento para mi local\n   b) Modificar descuento de mi local\n   c) Eliminar descuento de mi local\n   d) Volver\n2. Aceptar/Rechazar pedido de descuento\n3. Reporte de uso de descuentos\n0. Salir.")
            mendue=input("\n\t")
            b("cls")
        if mendue!="0":
            enConstrucc()

def MenuCli():                       #Menu del cliente.
    mencli="t"
    while mencli!="0":
        print("\n1. Registrarme\n2. Buscar descuentos de locales\n3. Solicitar descuento\n4. Ver novedades\n0. Salir")     
        mencli=input("\nIngrese una opcion: ")
        while mencli!="1" and mencli!="2" and mencli!="3" and mencli!="4" and mencli!="0":
            print("\n1. Registrarme\n2. Buscar descuentos de locales\n3. Solicitar descuento\n4. Ver novedades\n0. Salir")            
            mencli=input("\nIngrese una opcion valida: ")
        if mencli!="0":
            b("cls")
            enConstrucc()
        else:
            b("cls")

def leerOpc():                    #Lectura de la opcion deseada en el menu admin  (en revision)
    opc = input("\nSeleccione la accion a realizar: ")
    
    while not(opc.isdigit()) or opc < "0" or opc > "5":
        b("cls")
        print("\nNo se ha escogido una opcion valida, vuelva a intentar.")
        switchCarteles(6)
        opc = input("\nSeleccione la accion a realizar: ")

    return opc

def leerSubOpc1():        #Lectura de la opcion deseada en el submenu del menu admin

    subopc = input("\nSeleccione una opcion del nuevo menu: ")
    while subopc!="a" and subopc!="b" and subopc!="c" and subopc!="d" and subopc!="e":
        b("cls")
        print("\nNo se ha escogido una opcion valida, vuelva a intentar.")
        switchCarteles(1)
        subopc=input("\nSeleccione una opcion valida: ")

    if subopc >= 'a' and subopc <= 'c':
        mostrarLocales()

    if subopc == 'a':
        b("cls")
        ingresoLocal()
        ordReg(AFlocales, ALlocales)
    elif subopc == 'b':
        b("cls")
        ordReg(AFlocales, ALlocales)
        menmodifLocal()
        ordReg(AFlocales, ALlocales)
    elif subopc == 'c':
        b("cls")
        ordReg(AFlocales, ALlocales)
        elimLocal()
        ordReg(AFlocales, ALlocales)
    elif subopc == 'd':
        b("cls")
        mapa()
    
    return subopc

def listalocales():               #Printeo de locales en forma de lista

    b("cls")
    if os.path.getsize(AFlocales) > 0:
        print("¿Desea ver locales ya existentes? Si o No: ")
        decis= valSioNo()
        if decis=="si":
            while decis!="*":
                b("cls")
                print("| {:^12s} | {:^35s} | {:^13s} | {:^13s} | {:^12s} | {:^6s} |".format("Codigo Local","Nombre Local","Ubicacion","Rubro","Codigo Dueno","Estado"))
                tam = cantreg(AFlocales,ALlocales)
                ALlocales.seek(0,0)
                for w in range(0,tam):
                    regloc = pickle.load(ALlocales)
                    print("-"*110)
                    print("| {:^12s} | {:^35s} | {:^13s} | {:^13s} | {:^12s} | {:^6s} |".format(regloc.codloc,regloc.nomloc.strip(),regloc.ubiloc.strip(),regloc.rubloc.strip(),regloc.codus,regloc.estado))
                print("-"*110)
                decis=input("Ingrese * para cerrar la lista")
                while decis!="*":
                    decis=input("Ingrese * para cerrar la lista")
                b("cls")

def valRubro():
    global rubro
    rubro= input("\nIngrese el rubro del local: ")                    #Validacion del input que coincida con un rubro
    while rubro != 'indumentaria' and rubro != 'perfumeria' and rubro != 'comida':  
                b("cls")
                print("\nEl rubro ingresado no se identifico, vuelva a ingresarlo.")
                rubro = input("\nIngrese el rubro del local: ")

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

def ordReg(AF, AL):                     #idealmente no parametrisar, dejar par alocales
    if os.path.getsize(AF) > 0:
        tamReg = tamreg(AFlocales, ALlocales)
        tamArch = os.path.getsize(AFlocales)
        cantReg = int(tamArch/tamReg)
        for i in range(0, cantReg-1):
            for j in range (i+1, cantReg):
                ALlocales.seek (i*tamReg, 0)
                auxi = pickle.load(ALlocales)
                ALlocales.seek (j*tamReg, 0)
                print("tamaño:",os.path.getsize(AFlocales),"posicion j:",j,"posicion i:",i,"el tell:",ALlocales.tell(),"posicion bytes:",tamReg*j)
                auxj = pickle.load(ALlocales)
                if auxi.nomloc.strip() > auxj.nomloc.strip():
                    ALlocales.seek(i*tamReg,0)
                    pickle.dump(auxj, ALlocales)
                    ALlocales.seek(j*tamReg,0)
                    pickle.dump(auxi,ALlocales)
                    ALlocales.flush()
                    print("ya dumpeo")
                else:
                    print("no dumpeo")
                    print("tamaño archiv:",os.path.getsize(AFlocales))



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
    
    ordReg(AFlocales, ALlocales)
    listalocales()
    nombre = input("\nIngrese el nombre del local o * para salir(maximo 50 caracteres): ")
    while validartam(50,nombre) or (busqdico(nombre) != -1):
        b("cls")
        if validartam(50,nombre):
            print("\nSe excedio el tamano, ingrese el nombre nuevamente: ")
        else:
            print("\nEste nombre ya existe, ingrese uno diferente (maximo 50 caracteres): ")
        nombre = input()
    b("cls")
    while nombre!="*":
        ubicacion = input("\nIngrese la ubicacion del local: ") 
        while validartam(50,ubicacion):
            b("cls")
            ubicacion = input("\nSe excedio el tamano, ingrese la ubicacion nuevamente: ")
        b("cls")
        valRubro()
        b("cls")
        codueno=input("\nIngrese el codigo de usuario de algun dueno: ")
        while s(codueno,1,100):
            b("cls")
            codueno=input("\nIngrese solo valores numericos entre 1 y 100: ")
        codueno=int(codueno)
        if (valcodDue(codueno) != -1):
            regloc.codloc = cantreg(AFlocales, ALlocales) + 1
            regloc.nomloc = nombre
            regloc.ubiloc = ubicacion
            regloc.rubloc = rubro
            regloc.codus = codueno
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
            print("\nEl local se ha creado correctamente.")     
        else:
            b("cls")
            print("\nCodigo incorrecto o inexistente.")
        nombre=input("\nIngrese el nombre del siguiente local a crear o * para terminar: ")
        while validartam(50,nombre) or (busqdico(nombre) != -1):
            b("cls")
            if validartam(50,nombre):
                print("\nSe excedio el tamano, ingrese el nombre nuevamente: ")
            else:
                print("\nEste nombre ya existe, ingrese uno diferente (maximo 50 caracteres): ")
            nombre = input()
        b("cls")
    b("cls")
    maymenLocal()
    ordReg(AFlocales, ALlocales)
    listalocales()

def valSioNo():
    decis=input("\n\t")
    while decis!="si" and decis!="no":
        decis=input("Ingrese solo (si) o (no), ")
    return decis

def menmodifLocal():                     #Menu de modificar locales

    if os.path.getsize(AFlocales):
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
        decision=input("\nSeleccione una de las siguientes opciones:\n\n1. Ingresar con usuario registrado\n2. Registrarse como cliente\n3. Salir\n\t")
        while decision!="1" and decision!="2" and decision!="3":
            b("cls")
            decision=input("\nSeleccione una de las siguientes opciones:\n\n1. Ingresar con usuario registrado\n2. Registrarse como cliente\n3. Salir\n\t")
        if decision == "2":
            b("cls")
            tipouser = input()
            registro(tipouser)
        elif decision == "1":
            x = ingreso()
            if x==1:
                print("Se alcanzo el maximo de intentos")
            elif x != 2:
                ALusuarios.seek(x,0)
                regus = pickle.load(ALusuarios)
                print("\nEl codigo de usuario del usuario con correo: ",regus.nomus.strip()," es: ",regus.codus.strip(),".")
                if regus.tipous.strip() == 'administrador': 
                    print("entro al coso de admin", regus.nomus)
                    MenuAd()
                elif regus.tipous.strip() == 'dueno':
                    print("entro al coso de duenos")
                    MenuDue()
                else:
                    print("entro al coso de clientes")
                    MenuCli()

    print("¡Hasta luego!")

def validartam(tam, dato):                          #Valida que el string ingresado sea del tamaño limitado.
    if len(dato)>tam:
        return True
    else:
        return False

#Las siguientes funciones hasta enConstrucc son prints

def mostrarLocales():
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
    print("\n1. Gestion de locales.\n2. Crear cuentas de duenos de locales\n3. Aprobar / Denegar solicitud de descuento\n4. Gestion de novedades\n5. Reporte de utilizacion de descuentos\n0. Salir\n")

def cartelGestLocales():                  #Cartel para el menu de gestion de locales.
    print('1. Gestion de locales.\n\n\ta) Crear locales\n\tb) Modificar local\n\tc) Eliminar local\n\td) Mapa de Locales\n\te) Volver')

def cartelGestNov():                 #.
    print('\n\ta) Crear novedades\n\tb) Modificar novedad\n\tc) Eliminar novedad\n\td) Volver\n')

def enConstrucc():                             #.
    print("\nEn construccion...")
    time.sleep(3)
    b("cls")

def maymenLocal():                     #Ordenamiento de mayor a menor de los rubros contados
    for y in range (0,2):
        for z in range(y+1,3):
            if regcantrub[y].cant<regcantrub[z].cant:
                auxc=regcantrub[y].cant
                regcantrub[y].cant=regcantrub[z].cant
                regcantrub[z].cant=auxc
                auxr = regcantrub[y].rubro
                regcantrub[y].rubro=regcantrub[z].rubro
                regcantrub[z].rubro=auxr
    for y in range (0,3):
        print("Rubro:",regcantrub[y].rubro,"Cantidad:",regcantrub[y].cant)  #Seria bueno formatearlo como una lista
    time.sleep(3)


#Programa principal y Definicion de archivos

AFusuarios= rutaluciano + "ALusuarios.dat"
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

AFlocales= rutaluciano + "ALlocales.dat"
if not os.path.exists(AFlocales):
    ALlocales = open(AFlocales, "w+b")
else:
    ALlocales = open(AFlocales, "r+b")

AFpromo= rutaluciano + "ALpromo.dat"
if not os.path.exists(AFpromo):
    ALpromo = open(AFpromo,"w+b")
else:
    ALpromo = open(AFpromo,"r+b")

AFusopromo= rutaluciano + "ALusopromo.dat"
if not os.path.exists(AFusopromo):
    ALusopromo = open(AFusopromo,"w+b")
else:
    ALusopromo = open(AFusopromo,"r+b")

AFnovedades= rutaluciano + "ALnovedades.dat"
if not os.path.exists(AFnovedades):
    ALnovedades = open(AFnovedades,"w+b")
else:
    ALnovedades = open(AFnovedades,"r+b")

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


"""regloc.codloc=1
regloc.nomloc="apple"
regloc.ubiloc="rosario"
regloc.rubloc="perfumeria"
regloc.codus=4
regloc.estado="A" #Tipo Char

formateo_locales()
pickle.dump(regloc, ALlocales)
ALlocales.flush()"""

sistema()

"""
class pruebo():
    def init(self):
        self.prueba = ""

prueba = pruebo()
afprueba = "D:\\Familia\\Escritorio\\TP 3 py\\tp3archivos\\prueba.dat"
if not os.path.exists(afprueba):
    alprueba = open(afprueba, "w+b")
    for i in range (0,5):
        prueba.prueba= input("ingresa algo")
        alprueba.seek(0,2)
        prueba.prueba = prueba.prueba.ljust(10, " ")
        pickle.dump(prueba, alprueba)
        alprueba.flush()
else:
    alprueba = open(afprueba, "r+b")


alprueba.seek(0,0)
for i in range (0,5):
    prueba = pickle.load(alprueba)
    print(prueba.prueba)
x = input("presionar para seguir")


tamreg = tamreg(afprueba,alprueba)
tamarch= os.path.getsize(afprueba)
cantreg= int(tamarch/tamreg)
print("tamaño arch:",tamarch,"tamaño reg:",tamreg,"cant reg",cantreg)
for i in range (0,cantreg-1):
    for j in range (i+1, cantreg):
        alprueba.seek(i*tamreg, 0)
        xi = pickle.load(alprueba)
        alprueba.seek(j*tamreg, 0)
        xj = pickle.load(alprueba)
        print ("tam arch:",os.path.getsize(afprueba),"posicion i:",i,"posicion j:",j,"el tell:",alprueba.tell())
        if xi.prueba.strip() > xj.prueba.strip():
            alprueba.seek(i*tamreg, 0)
            pickle.dump(xj, alprueba)
            alprueba.seek(j*tamreg, 0)
            pickle.dump(xi, alprueba)
            print("ya dumpeo con tamaño:",os.path.getsize(afprueba))
        else:
            print("no dumpeo con tamaño:",os.path.getsize(afprueba))

alprueba.seek(0,0)
for i in range (0,5):
    prueba = pickle.load(alprueba)
    print(prueba.prueba)"""