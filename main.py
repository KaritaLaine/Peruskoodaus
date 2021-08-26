# PÄÄOHJELMA

# Modulien ja kirjastojen lataukset
import hetutarkistus as ht

# Kysytään käyttäjältä henkilötunnus
kysytty_hetu = input('Anna henkilötunnus: ')

# Tarkistetaan, että hetu on oikean pituinen
pituus_oikein = ht.tarkista_pituus(kysytty_hetu)

if pituus_oikein == True:
    # Tarkistetaan onko hetu oikein
    oli_oikein = ht.tarkista_hetu(kysytty_hetu)

    # Ilmoitetaan käyttäjälle onko hetu oikein
    if oli_oikein == True:
        print('Henkilötunnus OK.')
        print('Sukupuoli:', ht.selvita_sukupuoli(kysytty_hetu))
    else:
        print('Henkilötunnus väärin, tarkista!')
else:
    print('Henkilötunnuksen pituus on väärä, syötä uudelleen!')
