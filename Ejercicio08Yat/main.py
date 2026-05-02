from competidor import Competidor
from observador import Observador
def main():
    print("\n...Competidora...\n")
    competidor = Competidor(
        "Ary Gameplays",
        "89111214",
        "Avanzado",
        "Los Polinesios"
    )
    competidor.mostrar_perfil()
    print()

    competidor.ganar_puntos(50)
    competidor.perder_puntos(20)

    print("\n...Observadora...\n")

    observador = Observador(
        "Alexandra Cruz",
        "81142018",
        "Principiante",
    )
    observador.ver_partida()
    observador.ver_partida()

    print()
    observador.mostrar_perfil()

if __name__ == "__main__":
    main()
