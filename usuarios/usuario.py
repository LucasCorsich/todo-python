import datetime
import hashlib
import usuarios.conexiones as conexiones

connect = conexiones.conectar()
database = connect[0]
cursor = connect[1]


class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar la contraseña
        cifrado = hashlib.sha256()
        # tengo que pasarle la contraseña en bites
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido,
                   self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)

            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identificar(self):
        # Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrar la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
