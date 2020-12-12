import usuarios.usuario as modelo


class Acciones:
    def registro(self):
        print("\nOk, vamos a registrarte en el sistema")

        nombre = input("Cual es tu nombre?: ")
        apellido = input("Cual es tu apellido?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce una contraseña: ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nOk, identificate en el sistema")

        email = input("Introduce tu email: ")
        password = input("Introduce una contraseña: ")
