#FUNCIÓN PARA PEDIR HORAS DE CADA DÍA
def pedir_horas(dia):
    while True:
        try:
            horas = int(input(f"Ingrese las horas trabajadas el {dia}: "))
            if horas >= 0:
                return horas
            else:
                print("Error: las horas no pueden ser negativas.")
        except ValueError:
            print("Error: ingrese un número válido.")

# FUNCIÓN PARA CALCULAR TOTAL Y CLASIFICACIÓN
def calcular_horas_y_clasificacion(horas_dias):
    total = sum(horas_dias)

    if total > 40:
        return total, "Sobretiempo"
    else:
        return total, "Horario estándar"

#FUNCIÓN PARA PEDIR NOMBRE DEL TRABAJADOR
def pedir_nombre():
    while True:
        nombre = input("Ingrese el nombre: ").strip()

        if nombre == "":
            print("Error: no puede estar vacío.")
        elif not nombre.replace(" ", "").isalpha():
            print("Error: solo letras.")
        else:
            return nombre


# CREAR MATRIZ CON DATOS INGRESADOS POR USUARIO
horas_trabajadas = []

for i in range(4):  # 4 recursos
    print(f"\n--- Trabajador {i+1} ---")
    
    
    nombre = pedir_nombre()

    lunes = pedir_horas("lunes")
    martes = pedir_horas("martes")
    miercoles = pedir_horas("miércoles")
    jueves = pedir_horas("jueves")
    viernes = pedir_horas("viernes")

    horas_trabajadas.append([nombre, lunes, martes, miercoles, jueves, viernes])

# PROCESO PRINCIPAL
print("\n=== REPORTE DE HORAS TRABAJADAS ===\n")

for trabajador in horas_trabajadas:
    nombre = trabajador[0]
    horas = trabajador[1:]

    total, clasificacion = calcular_horas_y_clasificacion(horas)

    print(f"Trabajador: {nombre}")
    print(f"Total de horas: {total}")
    print(f"Clasificación: {clasificacion}")
    print("-----------------------------")

