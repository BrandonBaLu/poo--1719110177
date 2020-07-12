print("**-Bienvenidos al cifrado de cesar-**")
class cesar: #


    def _init_(self):#
        pass


    def cifrados(self): 
        repetir = "S"
        while repetir == "s" or repetir == "S":
            texto = input("Inserta tu texto: ")
            n = 5
            tipo=int(input("Ingrese el tipo de trabajo a realizar \n|1:Encriptar 2:Desencriptar|\ningrese numero\n")) 
            abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            cifrado = ''
            texto = texto.upper()
            for s in texto:
                if s in abecedario:
                    num = abecedario.find(s) 
                    if tipo==1:
                        num = num + n
                    elif tipo==2:
                        num = num - n
                    if num >= len(abecedario):
                        num = num - len(abecedario)
                    elif num < 0:
                        num = num + len(abecedario)
                    cifrado = cifrado + abecedario[num]
                else:
                    cifrado = cifrado + s
            print("el texto cifrado o descifrado es:\n",cifrado)
            repetir = input("Desea ingresar una nueva cadena de texto? \nS/N\n ")
            if repetir == "n" or repetir == "N":
              print("*-gracias por usar el codigo cesar-*")
              break 

objetoCesar = cesar()
objetoCesar.cifrados()