# HENKILÖTUNNUKSEN TARKISTUSRUTIINI

# Kirjastojen ja modulien lataukset
import datetime

# Globaalit muuttujat

# Sanakirja, jossa vuotisatakoodit
vuosisadat = {
    '+': 1800,
    '-': 1900,
    'A': 2000
}

# Sanakirja, jossa jakojäännösten koodit
tarkisteet = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
              5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H', 17: 'J', 18: 'K', 19: 'L', 20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S', 25: 'T', 26: 'U', 27: 'V', 28: 'W', 29: 'X', 30: 'Y'}

# Muuttuja, jossa on kuluva päivä ja kellonaika
nyt = datetime.datetime.now()

# Modulin funktiot


def onko_hetu_oikeanlainen(hetu):
    """Tarkistaa, että henkilötunnus on oikein muodostettu
    käyttäen modulo 31 tarkistetta

    Args:
        hetu (string): Suomalainen henkilötunnus merkkijonona

    Returns:
        boolean: True, jos oikein, False, jos väärin
    """

    # Muutetaan henkilötunnus isoihin kirjaimiin
    hetu = hetu.upper()

    tarkisteet = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                  5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H', 17: 'J', 18: 'K', 19: 'L', 20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S', 25: 'T', 26: 'U', 27: 'V', 28: 'W', 29: 'X', 30: 'Y'}

    paivatString = hetu[0] + hetu[1]
    kuukaudetString = hetu[2:4]
    vuodetString = hetu[4:6]
    vuosisatakoodiString = hetu[6]
    jarjestysnumeroString = hetu[7:10]
    tarkisteString = hetu[10]

    # Yhdistetään merkkijonot luvuksi tarkisteen laskentaa varten 130 728 478
    luvutString = paivatString + kuukaudetString + \
        vuodetString + jarjestysnumeroString

    # Muutetaan se numeroksi (int)
    luvut = int(luvutString)

    # Lasketaan jakojäännös 31:llä jaettuna (130829478 % 31) eli modulo 31
    jakojaannos = luvut % 31

    # Haetaan jakojäännöstä vastaava kirjain tarkisteet-sanakirjasta
    uusiLaskettuTarkiste = tarkisteet[jakojaannos]

    # Tarkistetaan onko laskettu tarkiste sama kuin syötetty tarkiste
    if uusiLaskettuTarkiste == tarkisteString:
        oikein = True
    else:
        oikein = False

    return oikein


def onko_pituus_oikein(hetu):
    """Tarkistaa henkilötunnuksen pituuden

    Args:
        hetu (string): Henkilötunnus

    Returns:
        boolean: True: pituus oikein, False: pituus väärin
    """

    # Lasketaan henkilötunnuksen pituus
    pituus = len(hetu)

    # tapa 1
    if pituus == 11:
        pituus_ok = True
    else:
        pituus_ok = False

    # vaihtoehtoinen tapa
    # pituus_ok = (pituus == 11)

    return pituus_ok


def selvita_sukupuoli(hetu):
    """Selvittää järjestysnumeron perusteella sukupuolen: parillinen -> nainen, pariton -> mies

    Args:
        hetu (string): Henkilötunnus

    Returns:
        string: Nainen tai mies
    """



    # Otetaan hetusta järjestysnumero-osa
    jarjestysnumeroString = hetu[7:10]

    # Muutetaan se luvuksi
    jarjestysnumero = int(jarjestysnumeroString)

    # Lasketaan jakojäännös modulo 2
    jakojaannos = jarjestysnumero % 2

    # Jos jakojäännös on 0 -> nainen, muutoin mies
    if jakojaannos == 0:
        sukupuoli = 'Nainen.'
    else:
        sukupuoli = 'Mies.'
    return sukupuoli


def syntymapaiva(hetu):
    """Hakee henkilötunnuksesta syntymäajan

    Args:
        hetu (string): henkilötunnus

    Returns:
        string: syntymäaika
    """

    paivatString = hetu[0] + hetu[1] # = hetu[0:2]
    kuukaudetString = hetu[2:4]
    vuodetString = hetu[4:6]
    vuosisatakoodiString = hetu[6]

    vuosisata = vuosisadat[vuosisatakoodiString]
    syntymavuosi = vuosisata + int(vuodetString)
    syntymavuosiString = str(syntymavuosi)

    syntymaika = paivatString + '.' + kuukaudetString + '.' + syntymavuosiString

    return syntymaika


def laske_ika(hetu):
    paivatString = hetu[0] + hetu[1]
    paivat = int(paivatString)
    kuukaudetString = hetu[2:4]
    kuukaudet = int(kuukaudetString)
    vuodetString = hetu[4:6]
    vuosisatakoodiString = hetu[6]

    vuosisata = vuosisadat[vuosisatakoodiString]
    syntymavuosi = vuosisata + int(vuodetString)

    syntymapaiva_datetime = datetime.datetime(syntymavuosi, kuukaudet, paivat)

    paivienero = nyt - syntymapaiva_datetime

    return round(paivienero.days / 365)


# Testataan erilaisia toimintoja kun tämä tiedosto ajetaan suoraan
if __name__ == '__main__':
    print(nyt)
    print('Ikä on', laske_ika('130728-478N'), 'vuotta.')
