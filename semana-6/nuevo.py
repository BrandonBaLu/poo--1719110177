class temperaturas() :
    #fecha=[]
    #celcius=[]
    #farenheit=[]
    arreglo=[] 
    
    
    
    def __inint__(self):
        pass
        
    def leer(self):
        
        archivo= input("*Escribe el nombre del archivo:*\n========++++++++++++++++========\n") #se solicita el nombre del archivo para llamarlo
        abrir= open(archivo, "r") #abre el archivo para leerlo
        leer= abrir.read() #lee el archivo
        print(leer) #lo imprime
        
        for row in archivo:
            self.arreglo.append(int(row)) 
   
    def imprimir(self):
        for row in self.arreglo:
            print(row)
        
    def promedio(self) :
        cont=0
        for row in self.arreglo:
           cont += row
        promedio_total=cont/ len(self.arreglo)
        print (promedio_total) 
        
        

#repetir="si"
objeto=temperaturas() 
#while repetir=="si":
objeto.leer() 
objeto.imprimir()
objeto.promedio()
#if repetir=="N" or repetir =="n":
#objeto.promedio() 
#repetir=input("desea repetir?" )
