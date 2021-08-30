# PÄÄOHJELMA

# Modulien ja kirjastojen lataukset
import hetutarkistus as ht

hetu_jarkeva = False
while hetu_jarkeva == False:
    # Kysytään käyttäjältä henkilötunnus
    kysytty_hetu = input('Anna henkilötunnus: ')

    # Tarkistetaan, että hetu on oikean pituinen
    pituus_oikein = ht.onko_pituus_oikein(kysytty_hetu)
    if pituus_oikein:
    
    # Tarkistetaan onko hetu oikein
        try:
            oli_oikein = ht.onko_hetu_oikeanlainen(kysytty_hetu)

            # Ilmoitetaan käyttäjälle onko hetu oikein
            if oli_oikein:
                print('Henkilötunnus OK.')
                print('Sukupuoli:', ht.selvita_sukupuoli(kysytty_hetu))
                print('Syntymäaika:', ht.syntymapaiva(kysytty_hetu))
                hetu_jarkeva = True
            else:
                print('Henkilötunnus väärin, tarkista!')
                hetu_jarkeva = False
        except:
            print('Virheellinen merkki henkilötunnuksessa, tarkista!')
            hetu_jarkeva = False
    else:
        print('Henkilötunnuksen pituus on väärä, syötä uudelleen!')
        hetu_jarkeva = False
