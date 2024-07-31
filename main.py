#Importamos las funciones necesarias
from funciones import registrarPolinomio,calculoXR,calcularLimite
#definimos las variables
a = 0 # la usaremos para definir el punto a
b = 0 # la usaremos para definir el punto b
aImprimir = 0
bImprimir = 0
fA = 0 # la usaremos para obtener el valor de f(a)
fB = 0 # la usaremos para obtener el valor de f(b)
xR = 0 # la usaremos para almacenar el valorde xr
xRanterior = 0 # la usaremos para almacenar el xR anterior
fXR = 0 # la usaremos para almacenar el valor de f(xr)
fAxfR = 0 # la para comprobar la interacion siguiente
errorPorcentualUser = 0 # la usaremos para saber cual es el margen de error que quiere el usuario
errorPorcentualObtenido = 0
iteraciones = 1
#estas listas las ocuparemos para almacenar el polinomio
terminos = 0
polinomio = []

#Solicitaremos el valor del intervalo a, b y el margen de error que busca el usuario
print("\n-----------------------------------------------------------------------\n")
print("Bienvenido al programa para poder encontrar la raiz de un Polinomio !!!")
print("\n-----------------------------------------------------------------------\n")
#verificaremos si la persona ingreso valores numericos
while True:
    try:
        a = float(input("Digita el inveralo A: "))
        b = float(input("\nDigita el invervalo B: "))
        errorPorcentualUser = int(input("\nDigita el error aproximado (en entero): "))
        
        if errorPorcentualUser >= 0 and errorPorcentualUser < 100:
            print("\n-----------------------------------------------------------------------\n")
            print("\t\tLos datos fueron guardados exitosamente...")
            print("\n-----------------------------------------------------------------------")
            break
        else:
            print("\nError!!! el porcentaje de error debe ser mayor a 0 y menos de 100. Inténtalo de nuevo.\n")
            
    except ValueError:
        print("\nError!!! por favor digita un valor numerico. Inténtalo de nuevo.\n")

#Ahora lo que haremos sera agarrar el polinomio del usuario

# contaremos el numero de terminos a ocupar
print("\nAhora digitaremos nuestro polinomio...")
while True:
    try:
        
        terminos = int(input("\nDigite la cantidad de terminos del polinomio: "))
        if terminos > 0:
          #registramos el polinomio
          polinomio = registrarPolinomio(terminos)

          print("\n-----------------------------------------------------------------------\n")
          for indice,x in enumerate(polinomio):
            if "-" in x:
                print(f"{x}",end='')
            elif indice > 0:
                print(f" + {x}",end='')
            else:
                print(f"{x}",end='')

          print("\n-----------------------------------------------------------------------\n")
          verificar = input("¿El polinomio esta escrito correctamente? (S/N): ").lower()
          if verificar == "s":
            break
          else:
            polinomio.clear()
            
        else:
            print("\nla cantidad de terminos debe ser mayor a 0\n")
    except ValueError:
        print("Digite un valor numerico!!!")

# Imprimeremos el encabezado de la tabla
print("\n+-----+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+")
while True:
    #calcular el valor de Xr
    xR = calculoXR(a,b)

    #encontraremos los limites de f(a), f(b), f(xr) y resolveremos hasta encontrar el margen de error solicitado
    fA = calcularLimite(polinomio,a)
    fB = calcularLimite(polinomio,b)
    fXR = calcularLimite(polinomio,xR)
    
    #verificaremos como sera siguiente interacion para encontrar el error minimo solicitado
    if fA > 0 and fB > 0: #verificamos si existe la posibilidad de una raiz dado que tiene que haber un cambio de signo entre estas 2
        print("\n-----------------------------------------------------------------------\n")
        print(f"no podemos afirmar que hay una raíz en el intervalo [{a},{b}] utilizando el Teorema del Valor Intermedio dado que los dos resultados de f() son del mismo signo (f(a): {fA} y f(b): {fB}) y no existe cambio se signo.")
        print("\n-----------------------------------------------------------------------\n")
        break
    else:
        #sacamos el valor de f(a) por f(xr)
        fAxfR = fA * fXR
        
         #Ahora calcularemos el error porcentual
        errorPorcentualObtenido = ((xR - xRanterior)/xR)*100
        #realizaremos el proceso de evaluar para verificar si ahi esta la raiz o cambiaremos algun intervalo
        if fAxfR == 0:
            print(f"|  {iteraciones}  | {a} | {b} | {xR} | {fA} | {fB} | {fXR} | {fAxfR} | {errorPorcentualObtenido} % |")
            break
        
        
            
        #este proceso lo realizo por que hay ocasiones en que por ejemplo tenemos un error del 11% pero nos lo da -0.11 entonces necesitamos verificar eso mejor asi q por eso lo volvemos positivo
        if errorPorcentualObtenido < 0:
            errorPorcentualObtenido *= -1
        
        #aqui guardaremos el xR actual para q sea el anterior para las proximas iteraciones
        xRanterior = xR
        
        #una vez se sobrepase el % que se desea o aproximado se terminara el proceso
        if errorPorcentualObtenido < errorPorcentualUser or errorPorcentualObtenido == 0:
            break
        else: #si no continuara
            #Ahora Imprimiremos la tabla en donde se llevara el registro del numero de iteracines hechas
            print(f"\n| interacion: {iteraciones} | a: {a} | b:{b} | xr: {xR} | f(a): {fA} | f(b): {fB} | f(xr): {fXR} | f(a)*f(xr):{fAxfR} | error%: {errorPorcentualObtenido} % |\n")
            
            #realizaremos el proceso de evaluar para verificar si ahi esta la raiz o cambiaremos algun intervalo
            if fAxfR < 0:
                b = xR
            else:
                a = xR
            iteraciones+=1  

print("+-----+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+")
print("\nFin del programa...\n")

        
        
        
        
        


        




