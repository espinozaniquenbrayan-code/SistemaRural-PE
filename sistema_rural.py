pacientes = []
citas = []
historias = []
medicamentos = []

def registrar_paciente():
    nombre = input("Nombre: ")
    dni = input("DNI: ")

    pacientes.append([nombre, dni])
    print("Paciente registrado correctamente.")

def registrar_cita():
    dni = input("DNI del paciente: ")
    fecha = input("Fecha de la cita: ")
    hora = input("Hora: ")

    if dni not in [p[1] for p in pacientes]:
        print("Paciente no encontrado.")
        return

    for cita in citas:
        if cita[1] == fecha and cita[2] == hora:
            print("Horario ocupado.")
            return

    citas.append([dni, fecha, hora])
    print("Cita registrada correctamente.")

def registrar_historia():
    dni = input("DNI del paciente: ")
    diagnostico = input("Diagnóstico: ")

    if dni not in [p[1] for p in pacientes]:
        print("Paciente no encontrado.")
        return

    historias.append([dni, diagnostico])
    print("Historia clínica guardada.")

def controlar_medicamentos():
    nombre = input("Medicamento: ")
    cantidad = int(input("Cantidad disponible: "))

    medicamentos.append([nombre, cantidad])

    if cantidad < 5:
        print("¡ALERTA! Stock bajo.")
    else:
        print("Stock suficiente.")

def menu():
    while True:
        print("\n--- SISTEMA RURAL-PE ---")
        print("1. Registrar paciente")
        print("2. Registrar cita")
        print("3. Historia clínica")
        print("4. Controlar medicamentos")
        print("0. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            registrar_cita()
        elif opcion == "3":
            registrar_historia()
        elif opcion == "4":
            controlar_medicamentos()
        elif opcion == "0":
            print("Sistema finalizado.")
            break
        else:
            print("Opción incorrecta.")

menu()
