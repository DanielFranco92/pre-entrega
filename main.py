def registro(bd):
    nombre = input("Ingrese el nombre de usuario: ")
    contrasenia = input("Ingrese la contraseña: ")
    bd[nombre] = contrasenia

def leerData(bd):
    print("La informacion almacenada en la base de datos es: ")
    for usu, contra in bd.items():
        print(f"{usu}: {contra}")
        
def guardarArchivo(bd):
    f = open("datos.txt", "wt") 
    f.write("{\n")
    for usu, contra in bd.items():
        f.write("\t")
        f.write(f'"{usu}"')
        f.write(": ")
        f.write(f'"{contra}"')
        f.write(",")
        f.write("\n")
    f.write("}")    

def login(bd):
    usuario = input("Ingrese su usuario: ")
    try:
        contra = bd[usuario]
        contrasenia =  input("Ingrese su contraseña: ")
        if(contra == contrasenia): 
            print("Has iniciado sesión")
        else:
            print("Contraseña incorrecta")         
    except:
        print("No se ha encontrado el usuario")
            
    
BD = {}

registro(BD)
leerData(BD) 
guardarArchivo(BD)  
login(BD) 