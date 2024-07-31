import math
import re
def registrarPolinomio(cantidadTerminos):
    listaPolinomio = []
    print("\n-----------------------------------------------------------------------\n")
    print("\t\tAhora digitaremos cada uno de los terminos y algunas reglas que tenemos que tomar son: ")
    print("\n\t\t1- Si queremos elevar la variable x se hara de la siguiente manera : x^4, x^2, -x^8 ")
    print("\n\t\t2- Si queremos representar el numero de Euler se hara de la siguiente manera : exp(-x), exp(2*x)")
    print("\n\t\t3- Si queremos multiplicar la variable x se hara de la siguiente manera : 3*x, 5*x^4")
    print("\n\t\t4- Si queremos ingresar un numero entero solo debemos escribirlo normalmente, si este es positivo solo el numero y si es negativo con su signo : 2,3,-5,-7")
    print("\n\t\tOJO: Al momento de escribir el polinomio verifique que este bien escrito, si no de lo contrario su respuesta no sera la adecuada\n")
    print("\n-----------------------------------------------------------------------\n")
    for i in range(cantidadTerminos):
        polinomio = input(f"Digite termino {i+1}: ")
        listaPolinomio.append(polinomio)
    
    return listaPolinomio

def calculoXR(a,b):
    calculoXR = (a+b)/2
    return calculoXR

def calcularLimite(polinomio,x):
    #instanciamos listas en donde guardaremos el resultado de cada termino para luego enviar una respuesta
    resultadoTerminosPolinomio = []
    respuestaTermino = 0
    #expresion regular para verificar si algun termino es solo el numero
    patron = re.compile(r'^-?\d+(\.\d+)?$')
    #variable que retornara el resultado del polinomio
    resultadoDevolver = 0
    
    for termino in polinomio:
        
        if "exp" in termino: # verificamos si contiene un numero de euler el ejercicio
            if "*" in termino: #verificamos si este numero es multplicado por otro
                for i,char in enumerate(termino):
                    if char == "*": #se le coloca 4 para llegar a la parte del * por q no necesitamos exp() si no, pues no hara el proceso
                        numeroMultiplicar = termino[i-1]
                        break
                
                if "^" in termino: #verificamos si la x que vamos a multiplicar por el entero no este elevada
                    for i, char in enumerate(termino):
                        if char == "^":
                            numeroElevar2 = termino[i+1]
                            break
                    
                    if "-" in termino: #ahora verificamos si el exponente enviado es negativo
                        xE = x*-1
                        respuestaTermino = math.exp(int(numeroMultiplicar)*pow(xE,int(numeroElevar2)))
                    else:
                        respuestaTermino = math.exp(int(numeroMultiplicar)*pow(x,int(numeroElevar2)))
                    
                else:
                    if "-" in termino: #ahora verificamos si el exponente enviado es negativo
                        xE = x*-1
                        respuestaTermino = math.exp(int(numeroMultiplicar)*xE)
                    else:
                        respuestaTermino = math.exp(int(numeroMultiplicar)*x)
                    
                resultadoTerminosPolinomio.append(respuestaTermino)
                
            elif "^" in termino: #verificaremos si esta elevado a algun exponente
                
                for i, char in enumerate(termino):
                    if char == "^":
                        numeroElevar = termino[i+1]
                        break
                
                if "-" in termino: #ahora verificamos si el exponente enviado es negativo
                    xE = x*-1
                    respuestaTermino = math.exp(pow(xE,int(numeroElevar)))
                else:
                    respuestaTermino = math.exp(pow(x,int(numeroElevar)))
                    
                resultadoTerminosPolinomio.append(respuestaTermino)
            else: # si no contiene ninguna elevacion y solo se eleva a x pues se vendra a este punto
              if "-" in termino: #ahora verificamos si el exponente enviado es negativo
                    xE = x*-1 #se coloca esto para poder multiplicar multiplicar los signos, dado que aqui en esta ocaso no tenemos con quien multiplicar ya sea 2,3, etc necesitamos determinar como quedara para elevalor al numero euler
                    respuestaTermino = (math.exp(xE))
              else:
                respuestaTermino = math.exp(x)
                
              resultadoTerminosPolinomio.append(respuestaTermino)
              
              #NO IMPORTANTE!!! ACTUALMENTE SOLO SE PUEDEN RESOLVER ELEVACIONes A X^nNumero O UNA MULTIPLCACION con una X elevada o no 3*X^nNumero
        else:
            if "*" in termino: #verificamos si este numero es multplicado por otro
                for i,char in enumerate(termino):
                    if char == "*": #se le coloca 4 para llegar a la parte del * por q no necesitamos exp() si no, pues no hara el proceso
                        numeroMultiplicar = termino[i-1]
                        break
                
                if "^" in termino: #verificamos si la x que vamos a multiplicar por el entero no este elevada
                    for i, char in enumerate(termino):
                        if char == "^":
                            numeroElevar2 = termino[i+1]
                            break
                    
                    if "-" in termino: #ahora verificamos si el exponente enviado es negativo
                        respuestaTermino = ( int(numeroMultiplicar)* pow(x,int(numeroElevar2))) * -1
                    else:
                        respuestaTermino = ( int(numeroMultiplicar)* pow(x,int(numeroElevar2)))
                    
                else:
                    if "-" in termino: #ahora verificamos si el exponente enviado es negativo
                        respuestaTermino = (int(numeroMultiplicar) * x) * -1
                    else:
                        respuestaTermino = (int(numeroMultiplicar) * x)
                    
                resultadoTerminosPolinomio.append(respuestaTermino)
                
            elif "^" in termino: #verificaremos si esta elevado a algun exponente
                
                for i, char in enumerate(termino):
                    if char == "^":
                        numeroElevar = termino[i+1]
                        break
                
                if "-" in termino: #ahora verificamos si el exponente enviado es negativo
                    respuestaTermino = (pow(x,int(numeroElevar))) * -1
                else:
                    respuestaTermino = pow(x,int(numeroElevar))
                    
                resultadoTerminosPolinomio.append(respuestaTermino)
                
            elif patron.match(termino): #entrara a esta condicion si es un numero normal que no tiene q ser sustituido
                
                respuestaTermino = int(termino) 
                resultadoTerminosPolinomio.append(respuestaTermino)
                
            else:# si no contiene ninguna elevacion y ni se multiplica por nada solo se vendra aqui
                
                if "-" in termino: #ahora verificamos si el exponente enviado es negativo
                    respuestaTermino = x * -1
                else:
                    respuestaTermino = x
                    
                resultadoTerminosPolinomio.append(respuestaTermino)
    
    resultadoDevolver = sumarPolinomio(resultadoTerminosPolinomio)
    
    return resultadoDevolver

def sumarPolinomio(listaResultados):
    polinomioSumado = 0
    
    for i,resultado in enumerate(listaResultados):
        
        if i == 0:
            polinomioSumado = resultado
        else:
            if resultado > 0:
                polinomioSumado += resultado
            else:
                polinomioSumado -= (resultado*-1)
    
    return polinomioSumado


    
    