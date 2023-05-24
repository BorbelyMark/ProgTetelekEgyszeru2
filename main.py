import random

#0
adatok = []
darabszam = 100
for db in range(darabszam):
    adatok.append(random.randint(50, 150))
print(adatok)

#Összegzés tétele
#sum - határozza meg az adatok lista elemét
sum = 0
for item in adatok:
    sum += item

print(f'sum(lista) - {sum}')

#átlag - az adatok lista elemeinek átlagának meghatározása
sum = 0
for item in adatok:
    sum += item
atlag = sum / len(adatok)

print(f'átlag(lista) - {atlag}')

#prod - az adatok lista elemeinek szorzatának meghatározása
prod = 1
for item in adatok:
    prod *= item

print(f'prof(lista) - {prod}')

#min - max tétel
#min - határozza meg a lista legkissebb elemét 

min = adatok[0]
for item in adatok:
    if item < min:
        min = item

print(f'min(lista) - {min}')

#max - határozza meg a lista legnagyobb elemét 
max = adatok[0]
for item in adatok:
    if item > max:
        max = item

print(f'max(lista) - {max}')

#megszámlalas tétele
#hatérozza meg a 120nál nagyobb elemek számát
#
db1 = 0
for item in adatok:
    if item > 120:
        db += 1

print(f'db1(lista) - {db1}')

#határozzuk meg hogy az adatok lista hány darab 100 elemet tartalmaz
#
db2 = 0
for item in adatok:
    if item == 100:
        db += 1

print(f'db2(lista) - {db2}')
#eldöntés tétele
#Legalabb egy elem teljesiti a feltételt
#döntse el hogy az adatok lista között van-e 50-es elem

vanE_50 = False
for item in adatok:
    if item == 50:
        vanE_50 = True
        break
if vanE_50:
    print("A lista tartalmaz legalább egy olyan elemet, amely értéke 50")
else:
    print("A lista nem tartalamz 50-es értékü")

#minden elem teljesíti 
#döntse el hogy az adatok lista minden eleme kisebb mint 150

mindenE_kisebb150 = True
for item in adatok:
    if not (item< 150):
        mindenE_kisebb150 = False
        break
if mindenE_kisebb150:
    print("A lista összes eleme kissebb mint 150 ")
else:
     print("A lista nem összes eleme kissebb mint 150 ")

#kiválasztás tétele
#határozza meg a lista 50es érték  első előfordulását
#!!!!!!!!!!!!!!!!!!!!!
#előfordul hogy amit szeretnénk kiválasztani olyan nincs is
elem50 = None
for item in adatok:
    if item == 50:
        elem50 = item
        break

if elem50 != None:
    print(f"van megfelelő elem amelyik értéke: {elem50}")
else:
    print("nincs ilyen elem") 

#Keresés tétele
#!!!!!!! ha nincs megfelelő elem, akkor nincs index
#határozza meg az adatok listába a 100As értékü elem helyét  (előfordulását, indexét)
   
index100 = None
for i in range(len(adatok)):
    if adatok[i] == 100:
        index100 = i
        break
if index100 != None:
    print("Van megefelelő (100-as értékü), amely indexe: {index100}")
else:
    print("Nincs megfelelő elem (100-as értékü)")



#buborékos rendezés
#rendezzük az adatpl éistát növekvő sorrenbe
for i in range(len(adatok)-1, 0, -1):
    for j in range(i):
        if adatok[j] > adatok[j+1]:
            adatok[j], adatok[j+1] = adatok[j+1], adatok[j]


print(adatok)