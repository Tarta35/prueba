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
from rutas import rutaluciano as ruta

class Usuarios:
    def __init__(self):
        self.codus=0
        self.nomus=" "
        self.claveus=" "
        self.tipous=" "

regus = Usuarios()

def formateo_usuarios():
    regus.codus= str(regus.codus)
    regus.codus= regus.codus.ljust(3, ' ')
    regus.nomus= regus.nomus.ljust(100, ' ')
    regus.claveus= regus.claveus.ljust(8, ' ')
    regus.tipous= regus.tipous.ljust(1, ' ')

AFusuarios= ruta + "ALusuarios.dat"
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


def archnull():
    return os.path.getsize(AFusuarios) > 0

def tamreg():
    if archnull():
        ALusuarios.seek(0,0)
        aux = pickle.load(ALusuarios)
        t = ALusuarios.tell()
        return t

def cantregus():
    if archnull():
        tamReg = tamreg()
        tamArch = os.path.getsize(AFusuarios)
        t = round(tamArch/tamReg)
        return t
    else:
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
    if regus.claveus.strip() == contra:
        return pos
    else:
        return -1
    
def guardauser(codus, nomus, claveus, tipous):          #Guarda un usuario en el archivo
    ALusuarios.seek(0,2)
    regus.codus = codus
    regus.nomus = nomus
    regus.claveus = claveus
    regus.tipous = tipous
    formateo_usuarios()
    pickle.dump(regus, ALusuarios)
    ALusuarios.flush()

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
