# HENKILÖTUNNUKSEN TARKISTUSSOVELLUS

# Modulien ja kirjastojen lataukset
import winsound # Windows äänet käyttöön

# Kysytään käyttäjältä henkilötunnus - merkkijono (string)
henkilotunnus = input('Anna henkilötunnus: ')

# Muutetaan henkilötunnus isoihin kirjaimiin
henkilotunnus = henkilotunnus.upper()

# Sanakirja vuosisatakoodin selvittämiseen
vuosisadat = {'+': 1800, '-': 1900, 'A': 2000}

# Sanakirja tarkisteiden hakemiseen
tarkisteet = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
              5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
              11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H',
              17: 'J', 18: 'K', 19: 'L', 20: 'M', 21: 'N', 22: 'P',
              23: 'R', 24: 'S', 25: 'T', 26: 'U', 27: 'V', 28: 'W',
              29: 'X', 30: 'Y'}

# Erotetaan henkilötunnuksen osat omiin muuttujiin (merkkijonoja)
paivatString = henkilotunnus[0] + henkilotunnus[1]
kuukaudetString = henkilotunnus[2:4]
vuodetString = henkilotunnus[4:6]
vuosisatakoodiString = henkilotunnus[6]
jarjestysnumeroString = henkilotunnus[7:10]
tarkisteString = henkilotunnus[10]

# Yhdistetään merkkijonot luvuksi tarkisteen laskentaa varten 130 728 478
luvutString = paivatString + kuukaudetString + \
    vuodetString + jarjestysnumeroString
print('Yhdessä: ' + luvutString)

# Muutetaan se numeroksi (int)
luvut = int(luvutString)

# Lasketaan jakojäännös 31:llä jaettuna (130829478 % 31) eli modulo 31
jakojaannos = luvut % 31
print('Jakojäännös:', jakojaannos)

#Haetaan jakojäännöstä vastaava kirjain tarkisteet-sanakirjasta
uusiLaskettuTarkiste = tarkisteet[jakojaannos]
print('Laskettu tarkiste: ',uusiLaskettuTarkiste)


# Muutetaan merkkijonot numeroiksi
paivat = int(paivatString)
kuukaudet = int(kuukaudetString)
vuodet = int(vuodetString)
vuosisata = vuosisadat[vuosisatakoodiString]
syntymavuosi = vuosisata + vuodet

# Muutetaan järjestysnumero numeroksi
jarjestysnumero = int(jarjestysnumeroString)


# Muutetaan syntymäajan päivämääräarvot tekstiksi -> syntymäpäivä
syntymaaikaString = str(paivat) + '.' + \
    str(kuukaudet) + '.' + str(syntymavuosi)
print('Syntymäaika on ' + syntymaaikaString)

# Tulostetaan eri henkilötunnuksen osat (päivä, kuukausi, vuosi)
# print('Päivät:', paivatString, 'Kuukaudet:',
#       kuukaudetString, 'Vuosi:', vuodetString,
#       'Vuosisatakoodi:', vuosisatakoodiString, 'Järjestysnumero: ',
#       jarjestysnumeroString, 'Tarkiste: ', tarkisteString)

# Tulostetaan syötetty henkilötunnus koneen ruudulle
# print('Antamasi henkilötunnus oli', henkilotunnus)

# Tarkistetaan onko laskettu tarkiste sama kuin syötetty tarkiste
if uusiLaskettuTarkiste == tarkisteString:
    print('Henkilötunnus on oikein.')
else:
    print('Henkilötunnus on virheellinen.')
    winsound.Beep(1000, 1000) 