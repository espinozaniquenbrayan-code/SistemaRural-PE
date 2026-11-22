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
    print("Historia
