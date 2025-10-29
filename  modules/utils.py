import os

def validar_carpeta(path, crear_si_no=True):
    if not os.path.exists(path):
        if crear_si_no:
            os.makedirs(path)
        else:
            raise FileNotFoundError(f"La carpeta {path} no existe.")
    if not os.access(path, os.W_OK):
        raise PermissionError(f"No se puede escribir en {path}.")

def validar_imagen(path):
    ext = os.path.splitext(path)[1].lower()
    return ext in [".jpg", ".jpeg", ".png"]
