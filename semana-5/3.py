import os
TAM_MAX_CLAVE = 26
repetir="s"
def menuPrincipal():
 while True:
  print("================================== ")
  print("========= CIFRADO CESAR ========== ")
  print("======== Utec Tulancingo ========= ")
  print("=========***************========== ")
  print("================================== ")
  print("== 1) |Cifrar  |                   == ")
  print("== 2) |Decifrar|                 == ")
  print("== 3) |Decifrar por fuerza bruta| == ")
  print("== 4) |Salir   |                 == ")
  print("==== BRANDON BALDERAS LUCAS ====== ")
  print("================================== ")
  opcion = input().lower();
  if opcion in "1,2,3,4".split(','):
   return opcion

def obtenerMensaje():
 print('Ingresa tu mensaje:')
 return input()

def obtenerClave():
    clave = 0
    while True:
     print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
     clave = int(input())
     if(clave >= 1 and clave <= TAM_MAX_CLAVE):
      return clave

def traducirMensaje(opcion, mensaje, clave):
 if opcion == '2':
  clave = -clave
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
   traduccion += simbolo
 return traduccion

def main():
  opcion = menuPrincipal()
  #if opcion == '4':
   # break
  mensaje = obtenerMensaje()
  if opcion == '3':
   print('Tu texto traducido es:')
   for clave in range(1, TAM_MAX_CLAVE):
    print(clave, traducirMensaje(opcion, mensaje, clave));
  else:
   clave = obtenerClave()
   print("================================== ")
   print('El texto ingresado es:',mensaje)
   print('El texto codificado es:',traducirMensaje(opcion, mensaje, clave));
   print("================================== ")
   print("********************************** ")
if __name__ == "__main__":
  main()