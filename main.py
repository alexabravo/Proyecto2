#Cristopher Jose Rodolfo Barrios Solis 18207
#Proyecto 2 Algoritmos
#Recomendar restaurantes
from Connectar import *
print("O _ 0 Bienvenido a nuestra aplicacion RESTAUNATOS O _ 0\n")
inicio = ("\n""Que desea hacer?  (Ingrese numero)\n\n"
             "1. Iniciar Sesion\n"
             "2. Comer Ya!\n"
             "3. Administrador\n"
             "4. Salir")
print(inicio)
menu =str(input(": "))
while (menu!="4"):
    if menu =="1":
        nombre = str(raw_input("Ingrese su nombre: "))
        edad = str(raw_input("Ingrese su edad: "))
        agregarCliente(nombre,edad)

        preguntaEstilo =str(input("\n""Que estilo y precio de comida prefiere? (Ingrese numero)\n"
                                   "1. Comida rapida, Accesible\n"
                                   "2. Comida elegante, Alto\n"
                                   "3. Comida saludable, Regular\n"
                                   "4. Comida casera, Accesible\n\n"
                                   ": "))
        if preguntaEstilo=="1":
            style = "Comida Rapida"
        if preguntaEstilo=="2":
            style = "Comida Elegante"
        if preguntaEstilo=="3":
            style = "Comida Saludable"
        if preguntaEstilo=="4":
            style = "Comida Casera"
        clienteEstilo(nombre,style)
        preguntaPreferencia =str(input("\n""Que le da mas importancia a un restaurante? (Ingrese numero)\n"
                                   "1. Ambiente del lugar\n"
                                   "2. Sabor de la comida\n"
                                   "3. Precio de la comida\n"
                                   "4. Compania al ir a comer\n\n"
                                   ": "))
        if preguntaEstilo=="1":
            preferencia = "Ambiente del lugar"
        if preguntaEstilo=="2":
            preferencia = "Sabor de la comida"
        if preguntaEstilo=="3":
            preferencia = "Precio de la comida"
        if preguntaEstilo=="4":
            preferencia = "Compania al ir a comer"
        clientePreferencia(nombre,preferencia)
        print(inicio)
        menu =str(input(": "))
    if menu =="2":
        nombre = str(raw_input("Ingrese su nombre: "))
        reco = recomendar(nombre,Preferencias(),nombre,Preferencias())
        print(reco)
        print(inicio)
        menu =str(input(": "))
    if menu =="3":
        nombreRestaurante = str(raw_input("Ingrese nombre de restaurante: "))
        agregarRestaurante(nombreRestaurante)

        preguntaEstilo =str(input("\n""Que estilo y precio de comida pertenece? (Ingrese numero)\n"
                                   "1. Comida rapida, Accesible\n"
                                   "2. Comida elegante, Alto\n"
                                   "3. Comida saludable, Regular\n"
                                   "4. Comida casera, Accesible\n\n"
                                   ": "))
        if preguntaEstilo=="1":
            styleRes = "Comida Rapida"
        if preguntaEstilo=="2":
            styleRes = "Comida Elegante"
        if preguntaEstilo=="3":
            styleRes = "Comida Saludable"
        if preguntaEstilo=="4":
            styleRes = "Comida Casera"
        restauranteEstilo(nombreRestaurante,styleRes)
        preguntaPreferencia =str(input("\n""Que le da mas importancia a su restaurante? (Ingrese numero)\n"
                                   "1. Ambiente del lugar\n"
                                   "2. Sabor de la comida\n"
                                   "3. Precio de la comida\n"
                                   "4. Compania al ir a comer\n\n"
                                   ": "))
        if preguntaEstilo=="1":
            preferenciaRes = "Ambiente del lugar"
        if preguntaEstilo=="2":
            preferenciaRes = "Sabor de la comida"
        if preguntaEstilo=="3":
            preferenciaRes = "Precio de la comida"
        if preguntaEstilo=="4":
            preferenciaRes = "Compania al ir a comer"
        restaurantePreferencia(nombreRestaurante,preferenciaRes)
        print(inicio)
        menu =str(input(": "))
print("Buen provecho!!!!")
        
    
