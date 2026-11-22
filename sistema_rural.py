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

    citas.append([dni, fecha, hora])
    print("Cita registrada correctamente.")
