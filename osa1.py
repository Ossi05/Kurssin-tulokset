# tee ratkaisu tänne

opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")


opiskelija = []

with open (opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        tiedot = rivi.strip().split(";")
        opnro = tiedot[0]


        #Nimet
        if opnro != "opnro":
            nimi = [tiedot[0], tiedot[1] + " " + tiedot[2]]
            opiskelija.append(nimi)

with open (tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        tiedot = rivi.strip().split(";")
        opnro = tiedot[0]

        if opnro != "opnro":
            
            for lista in opiskelija:
                pisteet = 0
                if opnro == lista[0]:
                    for luku in tiedot[1:]:
                        pisteet += int(luku)

                    lista.append(pisteet)
                    
    
#Tulostus
for lista in opiskelija:
    
    print(lista[1], lista[2])
    
