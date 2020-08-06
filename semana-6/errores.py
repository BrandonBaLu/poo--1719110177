import cmath#importe mi librería para poder realizar las raíces cuadradas
class errores() :#definí mi clase
   
    def __init__(self):#definívmi constructor 
        pass 
       
    def operaciones(self) :#definí mi metodo para realizar todas las operaciones 
        lista=[]#declare mi variable global donde se guardaran los numeros ingresados 
        print("******Bienvenido a esta tu app******")
        try:#evalúa los valores que el usuario ingrsa y devuelve una excepción 
            cantidad=int(input("¦**¿Cuantos numeros desea evaluar?:***¦ "))#pido al usuario cuantos valores desea ingresar 
            cont=0 #inicio mi contador en 0 para incrementar el valor de los números que desee evaluar el usuario 
            i=1 #inicie mi contador en 1 que es el primer valor que solicitara al usuario 
            while (cantidad>0):#ingreso mi condición que mientras el número de veces que el usuario sea mayor a 0 realice y ejecute las operaciones 
                cont+=1 #aumento mi contador  
                numero=int(input("Número: " +str(i)+":" )) #solicita el número a evaluar 
                if numero == 0:#genero la condición que si el numero es igual a 0 es par
                    print ("===¦¡¡¡Este número es par!!!===¦")
                elif numero%2 == 0:#evalua los reciduos de todos loz números ingresados 
                    print ("===¦¡¡¡Este número es par!!!===¦")
                else:#de no ser así, el número es impar
                    print ("===¦¡¡¡Este numero es impar!!!===")
                    
                resultado=cmath.sqrt(numero) #saca raíz al número ingresado
                print ("===¦La raíz cuadrada es: "+str(resultado)+"===¦" ) #Imprime el resultado de la raíz 
                lista.append(numero) #guarda los valores agregados en la lista 
                i=i+1#aumenta el contador del número de veces que se solicito
                cantidad=cantidad-1
                cubo=(numero**3) #Elevo los valores ingresados al cubo
                print ("===¦El cubo del numero agregado es: "+str(cubo)+"===¦" )#imprimo el cubo
                print (lista.index) #imprimo el index de la lista
            print ("===¦los números agregados fueron:===¦\n", lista)  #Imprime todos los números guardados 
                 
        except Exception as error:#devuelve la excepción e imprime que el valor qur ingreso no es correcto
            print("¡¡¡solo se aseptan numero!!!")
      
objeto= errores()#igualó mi objeto 
repetir ="s" 
while True:#mientras sea verdad la respuesta del usuario repetira el proceso de leer los valores que ingrese el usuario 
    if repetir == "S" or repetir =="s" :
        objeto.operaciones()#se ejecuta el metodo leer.
        repetir =input("===¦¿Deseas realizar otro calculó?:===¦\nS/N\n") #pregunto si el usuario desea agregar otro usuario si la respuesta es si, vuelve a pedir los valores
    if repetir=="n" or repetir =="N":#si la respuesta es no, ejecuta el metodo imprimir, e imprime los resultados 
        #ejecuta el metodo impromir. 
        print ("===¦🤣🍺Gracias por usar tu app calculando ando🍺🤣===¦") 
        print ("posdata: perdón profe, lo tenía que hacer 🤣🤣🍺") 
        break   
    
