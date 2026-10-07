import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="00000",
    autocommit=True
)

kursori = yhteys.cursor()
sql = "SELECT nimi, vaikutus FROM pos_tapahtumat ORDER BY RAND() LIMIT 1 "
kursori.execute(sql)
tulos = kursori.fetchone()


def positiivinen_tapahtuma():
    sql = "SELECT nimi, vaikutus FROM pos_tapahtumat ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if tulos:
        print(f"Tapahtuma: {tulos[0]} ja vaikutus {tulos[1]}")
        return tulos


def negatiivinen_tapahtuma():
    sql = "SELECT nimi, aika_muutos FROM tapahtumat ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if tulos:
        print(f"Tapahtuma: {tulos[0]} ja vaikutus {tulos[1]}")
        return tulos


def tapahtuman_pisteytys(vaikutus, valinta):
    if valinta == 1:
        return round(vaikutus, 2)
    elif valinta == 2:
        return round(vaikutus + (vaikutus * 0.2), 2)
    elif valinta == 3:
        return round(vaikutus + (vaikutus * 0.3), 2)

#Tästä etenpäin testaan vaan, että se toimii
# TESTI: positiivinen tapahtuma 

print("POSITIIVINEN TAPAHTUMA")

positiivinen = positiivinen_tapahtuma()

if positiivinen:
    vaikutus = float(positiivinen[1])
    valinta = int(input("Valitse 1, 2 tai 3: "))
    tulos = tapahtuman_pisteytys(vaikutus, valinta)
    print("Lopullinen vaikutus:", tulos)


# TESTI: negatiivinen tapahtuma

print()
print("NEGATIIVINEN TAPAHTUMA")

negatiivinen = negatiivinen_tapahtuma()

if negatiivinen:
    vaikutus = float(negatiivinen[1])
    valinta = int(input("Valitse 1, 2 tai 3: "))
    tulos = tapahtuman_pisteytys(vaikutus, valinta)
    print("Lopullinen vaikutus:", tulos)