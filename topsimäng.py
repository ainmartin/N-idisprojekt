import random
import time
a=3

#Algus, sissejuhatus.



print("Tere tulemast Topsimängu!")
print("Mängujuhend: Valida tuleb kolme topsi vahel, millest ühte on peidetud münt. Kui arvad, millise topsi all on münt, oled mängu võitnud.")

#Mängu kaasatakse mängija.

vastus=input("Kas soovite mänguga alustada(Jah/Ei)?")

#Mängija otsus.

if vastus.lower()=="jah":
    print("Palun oota, segan topse!")
    time.sleep(5)
    print("Topsid on segatud! Arva, millise topsi all on münt!")
else:
    print("Mäng lõpetatakse!")
    time.sleep(1)
    quit()

#Jah vastuse tagajärg.

int(random.randint(1,a))
arvamus=int(input("Sisestage number ühest kolmeni."))

#Sisestatud numbri tagajärg.


if((arvamus<1) or (arvamus>a)):
    print("Sisestatud number peab olema: 1, 2 või 3. Mäng lõpetatakse.")
    time.sleep(1)
    quit()

elif(arvamus==random.randint(1,a)):
    print("Palju õnne, arvasid õige topsi ära!")
else:
    print("Kahjuks teie pakutud number osutus valeks.")

teineVastus=input("Kas soovite uuesti mängida (Jah/Ei)?")

#Tsükkel

while teineVastus.lower()== "jah" :
    print("Palun oota, segan topse!")
    time.sleep(5)
    print("Topsid on segatud! Arva, millise topsi all on münt!")
    int(random.randint(1,a))
    arvamus=int(input("Sisestage number ühest kolmeni."))
    if((arvamus<1) or (arvamus>a)):
        print("Sisestatud number peab olema: 1, 2 või 3. Mäng lõpetatakse.")
        time.sleep(1)
        quit()
    elif(arvamus==random.randint(1,a)):
        print("Palju õnne, arvasid õige topsi ära!")
    else:
        print("Kahjuks teie pakutud number osutus valeks.")
        
    teineVastus=input("Kas soovite uuesti mängida (Jah/Ei)?")
else:
    print("Mäng lõpetatakse!")
    time.sleep(1)
    quit()

#Lõpp.
