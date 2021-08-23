# HENKILÖTUNNUKSEN TARKISTUSSOVELLUS

# Kysytään käyttäjältä henkilötunnus - merkkijono (string)
henkilotunnus = input('Anna henkilötunnus: ')

# Muutetaan henkilötunnus isoihin kirjaimiin
henkilotunnus = henkilotunnus.upper()

# Sanakirja vuosisatakoodin selvittämiseen
vuosisata = {'+': 1800, '-': 1900, 'A': 2000}

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

# Muutetaan merkkijonot numeroiksi
paivat = int(paivatString)
kuukaudet = int(kuukaudetString)
vuodet = int(vuodetString)

# Tulostetaan eri henkilötunnuksen osat (päivä, kuukausi, vuosi)
print('Päivät:', paivatString, 'Kuukaudet:',
      kuukaudetString, 'Vuosi:', vuodetString)

# Tulostetaan syötetty henkilötunnus koneen ruudulle
# print('Antamasi henkilötunnus oli', henkilotunnus)
