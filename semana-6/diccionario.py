class pelis() :
    
    peliculas=[] 
    genero={} 
   

    def _init_(self ) :
        pass
        
    def leer(self) :#Definí mi metodo
        print ("===================================================")
        print ("======UNIVERSIDAD TECNOLÓGICA DE TULANCINGO======")
        print ("===================================================") 
        nombre=input("======Ingresar el nombre de la película:======\n") #pedí al usuario el nombre del alumno 
        try:
            lanzamiento =int(input("========Año de lanzamiento :=========\n"))#pedí al usuario el año de nacimiento del alumno
            genero={input("========Ingresa el genero de la película ===========\n") } #Pedí el grupo del alumno
            datos=[nombre, genero, lanzamiento ]#ocupe otro arreglo para meter mis valores pedidos
            self.peliculas.append(datos)#guarde mis valores en mi variable global
            
        except ValueError:
            print("solo se aseptan numeros ")
     
    def imprimir_llaves(self) :
        for key in self.genero:
            print(key) 
            
    def imprimir_valores(self) :
        for key in self.genero:
            print(self.genero [key]) 
           
    def insertar_valor(self, key, value):
        self.genero[key] = value
        
    def eliminar(self, key):
        self.genero.pop(key) 
        
    def imprimir(self) :#Declare mi metodo para imprimir 
        for fila in self.arreglo:#En un rango de lo que los valores de arreglos tenga imprime sus valores
            print ("=============================================") 
            print ("==¦la película es :", fila[0]+ "==¦ \n==¦Su genero es: ", fila[1 ]+" =====¦" +"\n==¦Su lanzamiento fue en el año de : "+ str(fila[2])+" ======¦" ) #Imprime los valores del arreglo de acorde a las poscisiones que se le pide. 
            print ("================. L=============================") 
    
    def buscar(self) :
        if género in datos.values():
            for genero in datos:
                if datos[genero] in datos.values():
                     print(genero) 
                
objeto=pelis() #iguale mi variable objeto a arreglos
objeto.leer() 
objeto.imprimir_llaves() 
objeto.imprimir_valores()
objeto.insertar_valor() 
objeto.eliminar()
objeto.imprimir(genero.items)
objeto.buscar(input("Ingresa el genero\n"))