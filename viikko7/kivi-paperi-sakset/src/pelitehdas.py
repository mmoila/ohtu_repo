from kivi_paperit_sakset import KpsPelaajaVsPelaaja, KpsTekoaly, KpsParempiTekoaly


def luo_peli(tyyppi):
    match tyyppi:
        case "PvP":
            return KpsPelaajaVsPelaaja()
        case "Tekoaly":
            return KpsTekoaly()
        case "Parempi_tekoaly":
            return KpsParempiTekoaly()
