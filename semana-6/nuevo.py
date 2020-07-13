class temperaturas() :
    fecha=[]
    celcius=[]
    farenheit=[]
    arreglo=[] 
    
    
    
    def __inint__(self):
        pass
        
    def leer(self):
        archivo=open("temperaturas.txt","r")
       
        
        for row in archivo:
            self.arreglo.append(int(row)) 
    
    def convertir(self):
      for row in self.arreglo:
        celcius=float(input("ingresa tus temperaturas en celcius: "))
        farenheit=(celcius*1.80)+32
        print(farenheit)


    def imprimir(self):
        for row in self.arreglo:
            print(row)
        
    def promedio(self) :
        cont=0
        for row in self.arreglo:
           cont += row
        promedio_total=cont/ len(self.arreglo)
        print (promedio_total) 
        
        

repetir="si"
objeto=temperaturas() 
while repetir=="si":
  objeto.leer() 
  objeto.imprimir()
  objeto.convertir()
  if repetir=="N" or repetir =="n":
    objeto.promedio()
  repetir=input("desea repetir?" )
