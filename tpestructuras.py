# ============================
# TP INTEGRADOR PROGRAMACIÓN 
# ============================

# ----------------------------
# EJERCICIO 1 - CAJA KIOSCO
# ----------------------------
print("\n=== EJERCICIO 1 - CAJA KIOSCO ===")

while True:
    nombre = input("Nombre del cliente: ")
    if nombre.isalpha():
        break
    else:
        print("Error: solo letras.")

while True:
    cantidad = input("Cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error: número válido mayor a 0.")

total_sin_desc = 0
total_con_desc = 0

for i in range(1, cantidad + 1):
    while True:
        precio = input(f"Producto {i} - Precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error: solo números.")

    while True:
        desc = input("¿Tiene descuento? (S/N): ").lower()
        if desc in ["s", "n"]:
            break
        else:
            print("Error: ingresar S o N.")

    total_sin_desc += precio

    if desc == "s":
        precio_desc = precio * 0.9
    else:
        precio_desc = precio

    total_con_desc += precio_desc

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# ----------------------------
# EJERCICIO 2 - LOGIN
# ----------------------------
print("\n=== EJERCICIO 2 - LOGIN ===")

usuario_ok = "alumno"
clave_ok = "python123"
intentos = 0
acceso = False

while intentos < 3:
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_ok and clave == clave_ok:
        acceso = True
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:
    while True:
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: fuera de rango.")
            continue

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            while True:
                nueva = input("Nueva clave: ")
                if len(nueva) < 6:
                    print("Error: mínimo 6 caracteres.")
                    continue
                confirmar = input("Confirmar clave: ")
                if nueva == confirmar:
                    clave_ok = nueva
                    print("Clave cambiada.")
                    break
                else:
                    print("Error: no coinciden.")

        elif opcion == 3:
            print("¡Seguí adelante, vas bien!")

        elif opcion == 4:
            break


# ----------------------------
# EJERCICIO 3 - AGENDA
# ----------------------------
print("\n=== EJERCICIO 3 - AGENDA ===")

lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

while True:
    operador = input("Nombre del operador: ")
    if operador.isalpha():
        break
    else:
        print("Error: solo letras.")

while True:
    print("\n1.Reservar 2.Cancelar 3.Ver día 4.Resumen 5.Salir")
    op = input("Opción: ")

    if not op.isdigit():
        print("Error.")
        continue

    op = int(op)

    if op == 5:
        break

    if op == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            nombre = input("Paciente: ")
            if nombre.isalpha():
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("Sin cupo.")
        elif dia == "2":
            nombre = input("Paciente: ")
            if nombre.isalpha():
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("Sin cupo.")

    elif op == 2:
        dia = input("Día: ")
        nombre = input("Paciente: ")

        if dia == "1":
            if lunes1 == nombre: lunes1 = ""
            elif lunes2 == nombre: lunes2 = ""
            elif lunes3 == nombre: lunes3 = ""
            elif lunes4 == nombre: lunes4 = ""
        elif dia == "2":
            if martes1 == nombre: martes1 = ""
            elif martes2 == nombre: martes2 = ""
            elif martes3 == nombre: martes3 = ""

    elif op == 3:
        dia = input("Día: ")
        if dia == "1":
            print(lunes1 or "(libre)")
            print(lunes2 or "(libre)")
            print(lunes3 or "(libre)")
            print(lunes4 or "(libre)")
        elif dia == "2":
            print(martes1 or "(libre)")
            print(martes2 or "(libre)")
            print(martes3 or "(libre)")

    elif op == 4:
        ocup_lunes = sum([lunes1!="", lunes2!="", lunes3!="", lunes4!=""])
        ocup_martes = sum([martes1!="", martes2!="", martes3!=""])
        print(f"Lunes: {ocup_lunes}/4")
        print(f"Martes: {ocup_martes}/3")


# ----------------------------
# EJERCICIO 4 - BOVEDA
# ----------------------------
print("\n=== EJERCICIO 4 - BÓVEDA ===")

energia = 100
tiempo = 12
cerraduras = 0
alarma = False
codigo = ""
racha_forzar = 0

while True:
    nombre = input("Agente: ")
    if nombre.isalpha():
        break

while energia > 0 and tiempo > 0 and cerraduras < 3 and not (alarma and tiempo <= 3):
    print(f"Energía:{energia} Tiempo:{tiempo} Cerraduras:{cerraduras}")
    print("1.Forzar 2.Hackear 3.Descansar")
    op = input("Opción: ")

    if not op.isdigit():
        continue

    op = int(op)

    if op == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            alarma = True
            print("Alarma activada.")
            continue

        if energia < 40:
            riesgo = input("Elegir 1-3: ")
            if riesgo == "3":
                alarma = True

        if not alarma:
            cerraduras += 1

    elif op == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        for _ in range(4):
            codigo += "A"

        if len(codigo) >= 8 and cerraduras < 3:
            cerraduras += 1

    elif op == 3:
        energia = min(100, energia + 15)
        tiempo -= 1
        racha_forzar = 0
        if alarma:
            energia -= 10

if cerraduras == 3:
    print("VICTORIA")
else:
    print("DERROTA")


# ----------------------------
# EJERCICIO 5 - GLADIADOR
# ----------------------------
print("\n=== EJERCICIO 5 - GLADIADOR ===")

while True:
    nombre = input("Nombre: ")
    if nombre.isalpha():
        break

vida_j = 100
vida_e = 100
pociones = 3

while vida_j > 0 and vida_e > 0:
    print(f"{nombre} HP:{vida_j} | Enemigo HP:{vida_e} | Pociones:{pociones}")
    print("1.Ataque 2.Ráfaga 3.Curar")

    op = input("Opción: ")

    if not op.isdigit():
        continue

    op = int(op)

    if op == 1:
        daño = 15
        if vida_e < 20:
            daño *= 1.5
        vida_e -= daño
        print(f"Daño: {daño}")

    elif op == 2:
        for _ in range(3):
            vida_e -= 5
            print("Golpe 5 daño")

    elif op == 3:
        if pociones > 0:
            vida_j += 30
            pociones -= 1
        else:
            print("Sin pociones")

    if vida_e > 0:
        vida_j -= 12
        print("Enemigo ataca 12")

if vida_j > 0:
    print("VICTORIA")
else:
    print("DERROTA")