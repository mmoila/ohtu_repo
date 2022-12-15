from pelitehdas import luo_peli


def main():
    while True:
        toiminnot = {
            "a": lambda: luo_peli("PvP").pelaa(),
            "b": lambda: luo_peli("Tekoaly").pelaa(),
            "c": lambda: luo_peli("Parempi_tekoaly").pelaa(),
        }

        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        valinta = input().rstrip()[-1]

        if valinta not in toiminnot:
            break

        print(
            "\nPeli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        toiminnot[valinta]()


if __name__ == "__main__":
    main()
