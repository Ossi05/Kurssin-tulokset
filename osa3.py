# tee ratkaisu tänne

opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")


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
                    

    
#Koepisteet
with open (koepisteet) as tiedosto:
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

#arvosana
for tulokset in opiskelija:       

    harjoitus_pisteet = 40
    harjoitukset = tulokset[2] / 40 * 100 // 10
    tulokset.append(harjoitukset)
    piste_maara = harjoitukset + tulokset[3]
    tulokset.append(piste_maara)

    if piste_maara in range(0, 15):
        arvosana = 0
    elif piste_maara in range(15, 18):
        arvosana = 1
    elif piste_maara in range(18, 21):
        arvosana = 2 
    elif piste_maara in range(21, 24):
        arvosana = 3 
    elif piste_maara in range(24, 28):
        arvosana = 4
    else:
        arvosana = 5

    tulokset.append(arvosana)
    

#Tulostus
print(f'{"nimi":<30}{"teht_lkm":<10}{"teht_pist":<10}{"koe_pist":<10}{"yht_pist":<10}{"arvosana":<10}')
for lista in opiskelija:
    
    nimi = lista[1]
    teht_lkm = lista[2]
    teht_pist = int(lista[4])
    koe_pist = lista[3]
    yht_pist = int(lista[3]) + int(lista[4])
    arvosana = lista[6]

    print(f"{nimi:<30}{teht_lkm:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana:<10}")
