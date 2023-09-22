
### Validar una entrada como numero entero positivo inclyendo el cero ###  
### isdigit() o isnumeric()  ###
### No funciona para negativos ni para reales porque no acepta el - ni el . ###

def validaRangoDigitos(nro, desde, hasta):
	validaRango = nro.isdigit()  #para validar que un string tenga solo digitos, devuelve true o false
	if validaRango:
		if int(nro) >= desde and int(nro) <= hasta:
			return False   #validación correcta, retorna falso para que salga del while que valida
	return True  #validación incorrecta, retorna verdadero para que siga en el while que valida

def validaRangoNumeros(nro, desde, hasta):
	validaRango = nro.isnumeric()  #para validar que un string tenga solo digitos, devuelve true o false
	if validaRango:
		if int(nro) >= desde and int(nro) <= hasta:
			return False   #validación correcta, retorna falso para que salga del while que valida
	return True  #validación incorrecta, retorna verdadero para que siga en el while que valida




