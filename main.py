import sys
import getpass

def salir():
    sys.exit(0)

def sep():
    return print("-"*70)

user = "administrador"
contraseña = "12345"


inicio = input("Bienvenido estimado, ¿le interesaría ingresar al programa? (conteste con 'Si' o 'No'): ")

respuesta = inicio.lower()


intentos = 0
terminar = False

if respuesta == "si" or respuesta == "sí":
    while not terminar:
        login_user = input("Ingrese su nombre de usuario: ")
        login_pass = getpass.getpass("Ingrese su contraseña: ")
        
        if user == login_user and contraseña == login_pass:
            print("Felicidades, has podido ingresar!")
            terminar = True
        
        else:
            intentos += 1
            if intentos < 3:
                print("Usuario o contraseña incorrectos. Intenta nuevamente.")
            
        if intentos == 3:
            input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
            salir()

else: 
    input("Entonces que tenga un buen día, hasta luego: ")
    salir()


sep()


menú = {
    1: "Gestion de locales",
    2: "Crear cuentas de dueños de locales",
    3: "Aprobar / Denegar solicitud de descuento",
    4: "Gestión de novedades",
    5: "Reporte de utilización de descuentos",
    0: "Salir"
}

gestión_menú = {
    "a": "Crear locales",
    "b": "Modificar local",
    "c": "Eliminar local",
    "d": "Volver"
}

print("Aquí se le mostrará el menú principal: ")

for clave, valor in menú.items():
    print(clave, ":", valor)

comida = 0
indumentaria = 0
perfumería = 0


while True:
    terminar = False
    elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    
    if elección == 2 or elección == 3 or elección == 4 or elección == 5:
        print("Lo lamentamos pero esta sección está en construcción")
        
    elif elección == 0: 
        salir()    
    
    elif elección != 1:
        sep()
        print("Opción inválida. Eliga una de las opciones disponibles.")
        
    else:
        for clave, valor in gestión_menú.items():
            print(clave, ":", valor)
        
        while not terminar:
            sub_menú = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
            sep()
            if sub_menú == "b" or sub_menú == "c":
                print("Lo lamentamos pero esta sección está en construcción")
            
            elif sub_menú == "a":
                sep()
                print("Ingrese los datos de los locales que desee crear (máximo tres)")
                nombres = nombre1, nombre2, nombre3 = input("Ingrese los nombres separados por comas, por favor: ").split(",")
                rubros = rubro1, rubro2, rubro3 = input("Ingrese los rubros separados por espacios acorde al orden de su nombre: ").split()
                ubicaciones = ubi_1, ubi_2, ubi_3 = input("Ingrese las ubicaciones separadas por comas acorde al orden de su rubro: ").split(",")
                
                for rubro in rubros:
                    if rubro == "comida":
                        comida += 1
                    elif rubro == "indumentaria":
                        indumentaria += 1
                    elif rubro == "perfumería":
                        perfumería += 1
                        
                if comida == indumentaria and comida == perfumería:
                    print("Ningún rubro tiene más locales que los demás.")
                elif comida > indumentaria and comida > perfumería:
                    print(f"El rubro con más locales es 'comida', con {comida} locales")
                elif indumentaria > comida and indumentaria > perfumería:
                    print(f"El rubro con más locales es 'indumentaria', con {indumentaria} locales")
                elif perfumería > indumentaria and perfumería > comida:
                    print(f"El rubro con más locales es 'perfumería', con {perfumería} locales")
                    
                menor_local = min(comida, indumentaria, perfumería)
                if menor_local == comida:
                    menor_local_nombre = "comida"
                elif menor_local == indumentaria:
                    menor_local_nombre = "indumentaria"
                else:
                    menor_local_nombre = "perfumería"
                    print(f"El rubro con menos locales es '{menor_local_nombre}' con {menor_local} locales")
            
            elif sub_menú != "d":
                print("Opción inválida. Eliga una de de las opciones disponibles.")
            
            else:
                print("Volviendo...")
                terminar = True
