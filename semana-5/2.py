cifrado.py

# Cifrado Cesar



TAM_MAX_CLAVE = 26

       

def obtenerModo():

while True:
print('¿Deseas encriptar o desencriptar un mensaje?')
modo = input().lower()
if modo in 'encriptar e desencriptar d'.split():
  return modo
  else:
    print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')
    def obtenerMensaje():
      print('Ingresa tu mensaje:')
      return input()
    def obtenerClave():
      clave = 0
      while True:
        print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
          return clave
    def obtenerMensajeTraducido(modo, mensaje, clave):
      if modo[0] == 'd':
        clave= -clave
        traduccion = ''
        for simbolo in mensaje:
          if simbolo.isalpha():
            num = ord(simbolo)
            num += clave
            if simbolo.isupper():
              if num > ord('Z'):
                num -= 26
                elif num < ord('A'):
                  num += 26
                  elif simbolo.islower():
                    if num > ord('z'):
                      num -= 26
                      elif num < ord('a'):
                        num += 26
                        traduccion += chr(num)
          else:

49.             traduccion += simbolo

50.     return traduccion

51.

52. modo = obtenerModo()

53. mensaje = obtenerMensaje()

54. clave = obtenerClave()

55.

56. print('Tu texto traducido es:')

57. print(obtenerMensajeTraducido(modo, mensaje, clave))