class cadenas:
	cadena = ""

	def __init__(self, cadena):
		self.cadena = cadena

	def separado(self):

		for caracter in self.cadena:
			print(caracter)

	def tipo_dato(self):
		dato = ""
		print("La cadena por separado")
		for caracter in self.cadena:
			if caracter.isdecimal() == True:
				dato = "Numero"
			elif caracter.isalpha() == True:
				dato = "Letra"
			elif caracter.isdecimal() == False and caracter.isdigit() == False:
				dato = "Simbolo"

			print("El siguiente : " + str(caracter) + " es un: " +str(dato))

	def longiud(self):
		print("La longitud de la cadena es de :" + str(len(self.cadena)) +
		      " caracteres")

	def no_espacios(self):
		sin_espacio = self.cadena.replace(" ", "")
		print("La longitud de la cadena sin espacios es de :" +
		      str(len(sin_espacio)) + " caracteres")
		print("La cadena sin espacios: " + str(sin_espacio))


repetir = "Si"
while repetir == "Si" or repetir == "si":
	cadena = input("Ingresa la cadena a analizar :\n")
	objetocadenas = cadenas(cadena)
	print(objetocadenas.cadena)
	objetocadenas.longiud()
	objetocadenas.separado()
	objetocadenas.tipo_dato()
	objetocadenas.no_espacios()
	repetir = input("¿Desea analizar otra cadena?\nsi\nno\n")
