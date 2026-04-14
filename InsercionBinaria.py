#busqueda binaria
import math

myprintMessages=False

class Resultado():
    exito=True
    def __init__(self,indice):
        self.indice=indice

    def setExito(self,exito):
        self.exito=exito

    def setIndex(self,index):
        self.indice=index
        
    def wasNumberFounded(self):
        return self.exito

    def getIndex(self):
        return self.indice

def myprint(*args):
    if(not myprintMessages):
        return
    print(args)
    
def preguntarNumero():
    while (True):
        try:
            numero=(input('Ingrese un Numero para Ejecutar la busqueda Binaria:'))
            if(numero=='SALIR'):
                return None

            numero=int(numero)
            
            return numero
        except:
            myprint('ERROR EN EL INGRESO DEL NUMERO')

class OrdenamientoBinario:
    elementos=[]
    def BuscarCoincidencia(self,numeroABuscar,centro,izq,derecha,repeticiones):

        if(len(self.elementos)==0 or numeroABuscar<self.elementos[0]):
            # el elemento se ubica al principio de la lista
            return 'F0'

        if(numeroABuscar>self.elementos[len(self.elementos)-1]):
            # el elemento se ubica al final de la lista
            return f'F{len(self.elementos)}'
        
        if(numeroABuscar==self.elementos[centro]):
            #el elemento se ubica en el centro de la lista
            return centro

        if(numeroABuscar==self.elementos[izq]):
            #el elemento se ubica en el lado izquierdo del segmento actual
            return izq

        if(numeroABuscar==self.elementos[derecha]):
            #el elemento se ubica en el lado derecho del segmento actual
            return derecha

        if((derecha-izq)==1):
            #el elemento se encuentra entre las posiciones derecha e izquierda
            return -1

        if(repeticiones>len(self.elementos)):
            #ctm, no sirvio el algoritmo. Entrar aqui debería ser imposible
            return -2

    def busquedaBinaria(self,numeroABuscar):
        #terminar=False

        repeticiones=1
        izq=0
        derecha=len(self.elementos)-1

        while(True):
            
            centro=math.ceil((derecha-izq)/2)+izq

            resultado=self.BuscarCoincidencia(numeroABuscar,centro,izq,derecha,repeticiones)

            if(resultado!=None):
                try:
                    #el numero se encontro entre las opciones
                    #       o al menos esta dentro del rango de las opciones
                    resultado=int(resultado)
                    res=Resultado(resultado)
                    
                    if(resultado==-1):
                        #el elemento deberia estar en la posicion del la derecha
                        #   en el contexto de los limites establecidos de la busqueda
                        #   (no se refiere a la derecha absoluta del array sino a la
                        #    relativa de la comparacion actual)
                        res.setIndex(derecha)
                        res.setExito(False)
                    myprint('Numero de repeticiones:',repeticiones)
    
                except Exception:
                    #no se encontro pero esta fuera de los limites del array
                    resultado=int(resultado[1:])
                    res=Resultado(resultado)
                    res.setExito(False)

                return res
            
            if(numeroABuscar>self.elementos[centro]):
                #debe estar en el lado derecho a partir del centro
                izq=centro
            else:
                #debe estar en el lado izquierdo a partir del centro
                derecha=centro

            repeticiones+=1

    def MensajesDePosicion(self,resultado):
        if(resultado==0):
            myprint('AL INICIO DEL ARRAY')
            return 
        if(resultado==len(self.elementos)):
            myprint('AL FINAL DEL ARRAY')
            return 
        myprint(f'EN MEDIO DE    {self.elementos[resultado-1]}   y   {self.elementos[resultado]}')        
        
    def makeBinarySearch(self,numero):
        # print("self.elementos en makeBinarySearch=",self.elementos)
        res=self.busquedaBinaria(numero)
        resultado=res.getIndex()

        self.elementos.insert(resultado,numero)
        
        if(res.wasNumberFounded()):
            myprint(f'EL NUMERO ESTA EN LA POSICION[{resultado}]={self.elementos[resultado]}')
            return
        
        myprint(f'NO SE ENCONTRO EL NUMERO, SIN EMBARGO, DEBERIA OCUPAR EL LUGAR:  {resultado}')
        self.MensajesDePosicion(resultado)
        
        
        #myprint('HUBO UN ERROR EN MI ALGORITMO')

    def ordenar_lista(self,lista=[9,82,3,122,34,51,10]):
        # print(self.elementos)
        # self.elementos = []
        # print("self.elementos en ordenar_lista",self.elementos)
        for nivel in lista:
            self.makeBinarySearch(nivel)

            myprint('\n=======\n')

        print(self.elementos)
        return self.elementos

if(__name__=="__main__"):
    #estaturas=(167,161,172,182,154,168,172,161,152,163,158,181,159,181,166,176,173,173,173,166,165,157,154,169,179,162,166,178,159,165,176,179,166,176,191,173,170,173,157,182,188,171,163, 165,170,180,174,178,160,165)
    estaturas=[176, 162, 163, 179, 155, 166, 166, 169, 169, 176, 182, 159, 157, 179, 175, 186, 175, 166, 163, 184, 177, 168, 166, 163, 171, 167, 170, 162, 194, 160, 182, 177, 162, 160, 180, 165, 167, 173, 169, 186, 172, 163, 162, 156, 164, 172, 166, 160, 172, 181, 170, 171, 163, 177, 165, 174, 154, 170, 167, 152, 170, 158, 164, 169, 164, 171, 168, 165, 179, 167, 181, 162, 177, 167, 162, 173, 170, 163, 166, 173, 163, 165, 178, 174, 159, 174, 163, 174, 174, 162, 166, 163, 179, 177, 168, 163, 166, 179, 179, 163, 167, 161, 172, 182, 154, 168, 172, 161, 152, 163, 158, 181, 159, 181, 166, 176, 173, 173, 173, 166, 165, 157, 154, 169, 179, 162, 166, 178, 159, 165, 176, 179, 166, 176, 191, 173, 170, 173, 157, 182, 188, 171, 163, 165, 170, 180, 174, 178, 160, 165]

    ob=OrdenamientoBinario()
    ob.ordenar_lista(estaturas)