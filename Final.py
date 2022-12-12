import re

class Persona:
    def __init__(self, legajo, nombre, apellido):
        self.Legajo = legajo
        self.Nombre = nombre
        self.Apellido = apellido
    def __str__(self):
        return self.Nombre + " " + self.Apellido

def MenuPrincipal():
    print("1-Ingresar Usuario")
    print("2-Listar Usuarios")
    print("3-Salir")
    opcion = int(input())

    while opcion < 4:
        if opcion == 1:
            IngresarPersona()
            break
        elif opcion == 2:
            ListarPersonas()
            break
        elif opcion == 3:
            exit()
        else:
            MenuPrincipal()
    else:
        MenuPrincipal()
def IngresarPersona():
            print("Ingrese Legajo")
            legajo = input()
            if not VerificarLegajo(legajo):
                print("Solo ingrese numeros.")
                MenuPrincipal()
            if not LegajoExiste(legajo):
                print("El legajo ya existe.")
                IngresarPersona()
            print("Ingrese Nombre")
            nombre = input()
            if not VerificarNombre(nombre):
                print("Solo ingrese texto.")
                MenuPrincipal()
            print("Ingrese Apellido")
            apellido = input()
            if not VerificarNombre(apellido):
                print("Solo ingrese texto.")
                MenuPrincipal()
            NuevoUsuario = Persona(legajo, nombre, apellido)
            archivo = open("archivo.txt", "a")
            archivo.write(f"{NuevoUsuario.Legajo},{NuevoUsuario.Nombre},{NuevoUsuario.Apellido},\n")
            archivo.close()
            print(f"{NuevoUsuario} se ha registrado correctamente")
            MenuPrincipal()

def ListarPersonas():
            leer = open("archivo.txt","r")
            for linea in leer:
                armapersona = linea.split(',')
                PersonaRecuperada = Persona(armapersona[0],armapersona[1],armapersona[2])
                print(PersonaRecuperada)
            leer.close()
            MenuPrincipal()

def VerificarLegajo(legajo):
    patron = re.compile(r"[\d]{1,4}")
    return re.fullmatch(patron, legajo)

def VerificarNombre(cadena):
    patron = re.compile(r"[a-zA-Z]+")
    return re.fullmatch(patron, cadena)

def LegajoExiste(legajo):
    existe = True
    try:
        leer = open("archivo.txt","r")
        for linea in leer:
            leg = linea.split(',')
            if legajo == leg[0]:
                existe = False
        leer.close()
    except:
        pass
    return existe

MenuPrincipal()