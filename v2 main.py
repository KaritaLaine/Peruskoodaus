import stdnum.fi.hetu
import v2
 
def main():
     while True:
         hetu = input('Anna HETU: ')
         if stdnum.fi.hetu.is_valid(hetu):
            print('Oikeanlainen HETU')
            print(v2.sukupuoli(hetu))
            print('Syntymäpäivä:', v2.syntymapaiva(hetu))
            break
         else:
            print('Vääränlainen HETU')

if __name__== '__main__':
    main()