import hashlib

#Con listas
# Defino una lista para almacenar usuarios y contraseñas
usuarios_lista = []

# Función para agregar un usuario y su contraseña a la lista con formato hash
def agregar_usuario(usuario, contraseña):
    # Aplico hash a la contraseña
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    
    # Agrego usuario y contraseña a la lista
    usuarios_lista.append({'usuario': usuario, 'contraseña': hash_contraseña})

# Ejemplo
agregar_usuario('usuario1', 'contraseña123')
agregar_usuario('usuario2', 'contraseña456')
agregar_usuario('usuario3', 'contraseña789')
agregar_usuario('usuario4', 'password098')
agregar_usuario('usuario5', 'password765')

print("Usuarios y contraseñas (formato hash) almacenados en la lista:")
print(usuarios_lista)

# Con diccionarios
# Defino un diccionario para almacenar usuarios y contraseñas
usuarios_diccionario = {}

# Función para agregar un usuario y su contraseña al diccionario con formato hash
def agregar_usuario_diccionario(usuario, contraseña):
    # Aplico hash a la contraseña
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    
    # Agrego usuario y contraseña al diccionario
    usuarios_diccionario[usuario] = hash_contraseña

# Ejemplo
agregar_usuario('usuario1', 'contraseña123')
agregar_usuario('usuario2', 'contraseña456')
agregar_usuario('usuario3', 'contraseña789')
agregar_usuario('usuario4', 'password098')
agregar_usuario('usuario5', 'password765')

print("Usuarios y contraseñas (formato hash) almacenados en el diccionario:")
print(usuarios_diccionario)

