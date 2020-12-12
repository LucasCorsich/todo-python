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

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce una contraseña: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(
                    f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"Login incorrecto, intenta nuevamente")


def proximasAcciones(self, usuario):
    return None
