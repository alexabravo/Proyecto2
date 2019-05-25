#Cristopher Jose Rodolfo Barrios Solis 18207
#Proyecto 2 Algoritmos
#Recomendar restaurantes
from Connectar import *


print("Bienvenido a nuestra aplicacion RESTAUNATOS ◕ ‿‿ ◕\n")
menu = input("Que desea hacer?  (Ingrese numero)\n\n"
             "1. Comer Ya!\n"
             "2. Iniciar Sesion\n"
             "3. Administrador\n"
             "4. Salir\n\n"
             ": ")
menu = str(menu)
while (menu!="4"):
    if menu =="1":
        nombre = str(raw_input("Ingrese su nombre: "))
        edad = str(raw_input("Ingrese su edad: "))
        agregarCliente(nombre,edad)

        preguntaEstilo =str(input("Que estilo y precio de comida prefiere? (Ingrese numero)\n"
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
        preguntaPreferencia =str(input("Que le da mas importancia a un restaurante? (Ingrese numero)\n"
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
        
         
    if menu =="2":
        b = input("1. Iniciar Sesion\n"
                  "2. Registrarse\n\n")
        b = str(b)
        if b=="1":
            usuario = input("Ingrese Usuario: ")
            contrasena = input("Ingrese contrasena: ")
            usuario =str(usuario)
            contrasena = str(contrasena)
        if b=="2":
            usuarion = input("Ingrese Usuario: ")
            contrasena1 = input("Ingrese contrasena: ")
            contrasena2 = input("Ingrese contrasena nuevamente: ")
            usuarion =str(usuarion)
            contrasena1 = str(contrasena1)
            contrasena1 = str(contrasena1)
    if menu =="3":
        nombreRestaurante = str(raw_input("Ingrese nombre de restaurante: "))
        agregarRestaurante(nombreRestaurante)

        preguntaEstilo =str(input("Que estilo y precio de comida prefiere? (Ingrese numero)\n"
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
        preguntaPreferencia =str(input("Que le da mas importancia a un restaurante? (Ingrese numero)\n"
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
print("Buen provecho!!!!")
        
    
