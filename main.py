class Libro:
    def _init_(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def _str_(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nCategoría: {self.categoria}\nISBN: {self.isbn}"


class Usuario:
    def _init_(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def _str_(self):
        return f"Nombre: {self.nombre}\nID de Usuario: {self.user_id}\nLibros prestados: {', '.join([libro.titulo for libro in self.libros_prestados])}"


class Biblioteca:
    def _init_(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def cargar_inventario(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                datos = line.strip().split(',')
                titulo = datos[0]
                autor = datos[1]
                categoria = datos[2]
                isbn = datos[3]
                libro = Libro(titulo, autor, categoria, isbn)
                self.agregar_libro(libro)

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("Libro eliminado exitosamente.")
        else:
            print("El libro no está en la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario)

    def dar_de_baja_usuario(self, usuario):
        if usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario)
            print("Usuario dado de baja exitosamente.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, isbn, usuario):
        if usuario in self.usuarios_registrados:
            if isbn in self.libros_disponibles:
                libro = self.libros_disponibles[isbn]
                usuario.libros_prestados.append(libro)
                del self.libros_disponibles[isbn]
                print(f"Se prestó el libro '{libro.titulo}' a '{usuario.nombre}'.")
            else:
                print("El libro no está disponible.")
        else:
            print("El usuario no está registrado.")

    def devolver_libro(self, isbn, usuario):
        if usuario in self.usuarios_registrados:
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Se devolvió el libro '{libro.titulo}'.")
                    return
            print("El usuario no tiene prestado ese libro.")
        else:
            print("El usuario no está registrado.")

    def buscar_libros(self, criterio, valor):
        libros_encontrados = []
        if criterio == 'titulo':
            libros_encontrados = [libro for libro in self.libros_disponibles.values() if
                                  valor.lower() in libro.titulo.lower()]
        elif criterio == 'autor':
            libros_encontrados = [libro for libro in self.libros_disponibles.values() if
                                  valor.lower() in libro.autor.lower()]
        elif criterio == 'categoria':
            libros_encontrados = [libro for libro in self.libros_disponibles.values() if
                                  valor.lower() in libro.categoria.lower()]

        if libros_encontrados:
            for libro in libros_encontrados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio de búsqueda.")

    def listar_libros_prestados(self, usuario):
        if usuario in self.usuarios_registrados:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados en este momento.")
        else:
            print("El usuario no está registrado.")

    def ver_inventario(self):
        if self.libros_disponibles:
            print("Inventario de la biblioteca:")
            for libro in self.libros_disponibles.values():
                print(libro)
        else:
            print("No hay libros en el inventario.")

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Añadir libro")
            print("2. Eliminar libro")
            print("3. Registrar usuario")
            print("4. Dar de baja usuario")
            print("5. Prestar libro")
            print("6. Devolver libro")
            print("7. Buscar libros")
            print("8. Listar libros prestados")
            print("9. Ver inventario")
            print("10. Salir")
            opcion = input("Ingrese el número de la opción que desea: ")

            if opcion == '1':
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                categoria = input("Ingrese la categoría del libro: ")
                isbn = input("Ingrese el ISBN del libro: ")
                libro_nuevo = Libro(titulo, autor, categoria, isbn)
                self.agregar_libro(libro_nuevo)
            elif opcion == '2':
                isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
                self.quitar_libro(isbn)
            elif opcion == '3':
                nombre = input("Ingrese el nombre del usuario: ")
                user_id = input("Ingrese el ID del usuario: ")
                nuevo_usuario = Usuario(nombre, user_id)
                self.registrar_usuario(nuevo_usuario)
            elif opcion == '4':
                user_id = input("Ingrese el ID del usuario que desea dar de baja: ")
                usuario = next((usuario for usuario in self.usuarios_registrados if usuario.user_id == user_id), None)
                self.dar_de_baja_usuario(usuario)
            elif opcion == '5':
                isbn = input("Ingrese el ISBN del libro que desea prestar: ")
                user_id = input("Ingrese el ID del usuario: ")
                usuario = next((usuario for usuario in self.usuarios_registrados if usuario.user_id == user_id), None)
                self.prestar_libro(isbn, usuario)
            elif opcion == '6':
                isbn = input("Ingrese el ISBN del libro que desea devolver: ")
                user_id = input("Ingrese el ID del usuario: ")
                usuario = next((usuario for usuario in self.usuarios_registrados if usuario.user_id == user_id), None)
                self.devolver_libro(isbn, usuario)
            elif opcion == '7':
                criterio = input("Ingrese el criterio de búsqueda (titulo/autor/categoria): ")
                valor = input("Ingrese el valor a buscar: ")
                self.buscar_libros(criterio, valor)
            elif opcion == '8':
                user_id = input("Ingrese el ID del usuario: ")
                usuario = next((usuario for usuario in self.usuarios_registrados if usuario.user_id == user_id), None)
                self.listar_libros_prestados(usuario)
            elif opcion == '9':
                self.ver_inventario()
            elif opcion == '10':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número del 1 al 10.")


# Ejemplo de uso:
if_name_== "_main_":
    biblioteca = Biblioteca()
    biblioteca.cargar_inventario("inventario_libros.txt")
    biblioteca.menu()
