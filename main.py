
alfabet_jawny = "abcdefghijklmnopqrstuvwxyz"
alfabet_tajny = ""
klucz = 3
def alfabet(alfabet_jawny, alfabet_tajny, klucz):
    x = 0
    i =0
    for letter in alfabet_jawny :
        alfabet_tajny = alfabet_tajny + alfabet_jawny[i+klucz]
        i += 1
        print (letter)
    while (x < klucz):
        alfabet_tajny = alfabet_tajny + alfabet_jawny[x]
    return alfabet_tajny


alfabet(alfabet_jawny, alfabet_tajny, 3)
print(alfabet_tajny)



