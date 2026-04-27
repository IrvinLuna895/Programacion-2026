class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def añadir_cancion(self, titulo):
        if len(self.canciones) >= 5:
            print("Alcanzado el límite máximo de canciones por playlist")
        else:
            if titulo in self.canciones:
                print("La canción ya se encuentra en la playlist")
            else:
                self.canciones.append(titulo)
                print(f"{titulo} añadida a {self.nombre}.")

    def eliminar_cancion(self, titulo):
        if titulo in self.canciones:
            self.canciones.remove(titulo)
            print(f"{titulo} ha sido eliminado de {self.nombre}")
        else:
            print(f"{titulo} no está en {self.nombre}")

    def total_canciones(self):
        return len(self.canciones)

    def mostrar_playlist(self):
        print(f"========== Playlist: {self.nombre} ==========")
        if len(self.canciones) == 0:
            print("La Playlist está vacía actualmente")
        else:
            i = 1
            for titulo in self.canciones:
                print(i, titulo)
                i += 1

    def limpiar_playlist(self):
        self.canciones.clear()
        print("La playlist está vacía")

    def buscador(self, texto):
        resultados = []

        for cancion in self.canciones:
            if cancion.startswith(texto):
                resultados.append(cancion)

        if len(resultados) > 0:
            print(f"Canciones encontradas en {self.nombre}:")
            for cancion in resultados:
                print("-", cancion)
        else:
            print(f"No se encontraron canciones que comiencen con '{texto}' en {self.nombre}")


# Ejemplo de uso
mix_pop = Playlist("Mi musica de Pop")

mix_pop.añadir_cancion("Beat")
mix_pop.añadir_cancion("Beat1")
mix_pop.añadir_cancion("Beat2")
mix_pop.añadir_cancion("Smooth Criminal")
mix_pop.añadir_cancion("Thriller")

mix_pop.buscador("Beat")
mix_pop.mostrar_playlist()
