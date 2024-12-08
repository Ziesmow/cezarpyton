wyb = input("oto szyfryzator do kodu cezara rozszyfrować czy zaszyrować[r/z]:")

alfabet_jawny = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alfabet_tajny = []

def alfabet(klucz, alfabet_jawny, alfabet_tajny):
    i = 0
    for i in range (0, 26 - int(klucz)):
        alfabet_tajny.append(alfabet_jawny[i+int(klucz)])
        i =+ 1
    x = 0
    for x in range(0 , int(klucz)):
        alfabet_tajny.append(alfabet_jawny[x])
        x =+ 1
    print(alfabet_tajny)



if(str(wyb) == "r" or str(wyb) == "R"):
    print("rozszyfrowanie")


elif(str(wyb) == "z" or str(wyb) == "Z"):
    print("zaszyfrowywanie")
    klucz = input("podaj klucz do szyforwania:")
    tekst = input("podaj tekst do zaszyfrowania:")
    alfabet(klucz,alfabet_jawny,alfabet_tajny)





