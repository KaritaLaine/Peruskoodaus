import v3

class VakioHetu:
    def __init__(self):
        pass

    def __str__(self):
        return 'HETU42'

    def ika(self):
        return 42

def main():
    ht = v3.Henkilotunnus('130603A680X')
    ht2 = VakioHetu()
    nayta_ika(ht)
    nayta_ika(ht2)

def nayta_ika(h):
    print(f'Henkilötunnuksen {h} ikä on {h.ika()} vuotta.')

if __name__ == '__main__':
    main()