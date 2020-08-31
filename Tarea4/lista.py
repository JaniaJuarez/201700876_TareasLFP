
import webbrowser
webbrowser.open("file:///C:/Users/jania/OneDrive/Escritorio/Laboratorio/Repositorio/201700876_TareasLFP/Tarea4/templates/template.html", new=2, autoraise=True)

def creador_usuario(nombre, edad, activo,saldo):

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "activo": activo,
        "saldo": saldo,
        
    }
    return usuario