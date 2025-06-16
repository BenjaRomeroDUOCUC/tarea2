#a) el nombre del comprador.
#b) el tipo de entrada solo permite "G" (General) o "V" (VIP)
#c) el codigo de confirmacion debe tener largo minimo de 6 caracteres
#debe tener al menos 1 letra mayuscula, al menos 1 numero
#y no puede tener espacio en blanco.


entradas_losiluminados=500
entradas_losfortificados=500



concierto={
    "los fortificados":{

    },
    "los iluminados":{

    }

}

def comprar_entrada_A():
    global entradas_losfortificados
    nombre = input("Ingrese su nombre: ").lower()
    if nombre in concierto["los fortificados"]:
        print("Este comprador ya existe.")
        return

    entrada = input("Tipo de entrada (G o V): ").lower()
    if entrada == "g":
        print("Su entrada es general.")
    elif entrada == "v":
        print("Su entrada es VIP.")  
    else:
        print("Seleccione una opción válida.")  
        return   
    while True:

        codigo = input("Ingrese el código de confirmación: ")
        if len(codigo) < 6 or " " in codigo:
         print("Código no válido. Intente otra vez.")
         print("Minimo 5 carácteres,al menos 1 letras mayusculas, al menos 1 número y no puede tener espacio en blanco.")
        
        if not any(c.isupper() for c in codigo) or not any(c.isdigit() for c in codigo):
            print("Código no válido. Intente otra vez.")
            print("Minimo 5 carácteres,al menos 1 letras mayusculas, al menos 1 número y no puede tener espacio en blanco.")

        else:   

            print("Código validado.")
            concierto["los fortificados"][nombre] = {
                "entrada": entrada,
                "codigo": codigo
            }
            print("¡Entrada registrada con éxito para “los Fortificados”!")
            print(concierto["los fortificados"][nombre])
            entradas_losfortificados-=1
            break

def comprar_entrada_B():
    global entradas_losiluminados
    nombre=input("Ingrese su nombre: ").lower
    if nombre in concierto["los iluminados"]:
        print("Este nombre ya existe.")
        return
    entrada=input("Ingrese su tipo de entrada (CV o PAL): ").lower()
    if entrada == "cv":
        print("Su entrada es cancha VIP.")
    elif entrada == "pal":
        print("Su entrada es palco.")
    else:
        print("Seleccione una opción válida.")
        return
    codigo=input("Ingrese su codigo de confirmación: ")
    if len(codigo) < 6 or " " in codigo:
         print("Código no válido. Intente otra vez.")
         print("Minimo 5 carácteres,al menos 3 letras mayusculas, al menos 1 número y no puede tener espacio en blanco.")
        
    if not any(c.isupper() for c in codigo) or not any(c.isdigit() for c in codigo):
            print("Código no válido. Intente otra vez.")
            print("Minimo 5 carácteres,al menos 3 letras mayusculas, al menos 1 número y no puede tener espacio en blanco.")

    else:
        concierto["los iluminados"][nombre]={
            "entrada":entrada,
            "codigo":codigo

        }   
        print("Entrada registrada con éxito para los iluminados!")
        print(concierto["los iluminados"][nombre])
        entradas_losiluminados-=1

     
def stock_de_entradas():
    print(f"Entradas disponibles en los fortificados: {entradas_losfortificados} ")
    print(f"Entradas disponibles en los iluminados: {entradas_losiluminados} ")
        
def menu():
    while True:
        print("-"*50)
        print(" "*2,"TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
        print("-"*50)
        print("1. Comprar entrada a Los Fortificados.")
        print("2. Comprar entrada a Los Iluminados.")
        print("3. Stock de entradas para ambos conciertos.")
        print("4. Salir")
        try:
            opcion=int(input("Seleccione una opción: "))
            if opcion not in [1,2,3,4]:
                print("opción no válida.")
            if opcion == 4:
                print("Saliendo del programa...")
                break
            elif opcion == 1:
                comprar_entrada_A()
            elif opcion == 2:
                comprar_entrada_B()
            elif opcion == 3:
                stock_de_entradas()
        except ValueError:
            print("Error: Ha ingresado un valor inválido.")    

menu()