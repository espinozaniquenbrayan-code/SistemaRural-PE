pacientes = []
citas = []
historias = []
medicamentos = []

def registrar_paciente():
    nombre = input("Nombre: ")
    dni = input("DNI: ")

    pacientes.append([nombre, dni])
    print("Paciente registrado correctamente.")
