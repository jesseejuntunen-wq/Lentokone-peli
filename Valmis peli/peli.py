import mysql.connector
import random

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="Jesse",
    password="Jesse0802",
    autocommit=True
)

kursori = yhteys.cursor()

aika = 30
pisteet = 0

# PELIN OHJEET

print()
print("========================")
print("       PELIN OHJEET")
print("========================")
print()
print("Tavoitteena on matkustaa lentokentältä toiselle")
print("ja kerätä mahdollisimman paljon pisteitä.")
print()
print("Pelin alussa sinulla on 30 päivää aikaa.")
print()
print("Jokaisella kierroksella saat kolme lentokenttää:")
print("1 = lento vie 1 päivän")
print("2 = lento vie 2 päivää ja se kertaa pisteesi 0.2 kertoimella")
print("3 = lento vie 3 päivää ja se kertaa pisteesi 0.3 kertoimella")
print()
print("Laskeutumisen jälkeen voi tapahtua")
print("positiivinen tai negatiivinen tapahtuma.")
print("Tapahtumat vaikuttavat pisteisiisi.")
print("Mitä suurempi kerroin sitä suurempi vaikutus pisteisiisi.")
print()
print("Peli päättyy, kun 30 päivää on mennyt.")
print("Yritä saada mahdollisimman paljon pisteitä!!!")
print()
print("========================")
input("Paina Enter aloittaaksesi pelin")
print()

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


# VALITAAN ALOITUSMAANOSA

print("Valitse näistä maanosista aloituspisteesi")
print("1: EU, 2: NA, 3: SA, 4: AS, 5: AF")

valinta = int(input("Valitse maanosa: "))

maanosat = {
    1: "EU",
    2: "NA",
    3: "SA",
    4: "AS",
    5: "AF"
}

maanosa = maanosat.get(valinta)


# ARVOTAAN ALOITUSLENTOKENTTÄ

sql = """
SELECT airport.name, country.name
FROM airport
JOIN country
ON airport.iso_country = country.iso_country
WHERE country.continent = %s
ORDER BY RAND()
LIMIT 1
"""

kursori.execute(sql, (maanosa,))
paikka = kursori.fetchone()

print()
print("Aloituspaikkasi on:", paikka[0])
print("Maa:", paikka[1])
print("Aikaa:", aika, "päivää")
print("Pisteet:", pisteet)


# PELI

while aika > 0:

    print()
    print("------------------------")
    print("Valitse seuraava lentokenttä:")


    # HAETAAN 3 SATUNNAISTA LENTOKENTTÄÄ

    sql = """
    SELECT airport.name, country.name
    FROM airport
    JOIN country
    ON airport.iso_country = country.iso_country
    ORDER BY RAND()
    LIMIT 3
    """

    kursori.execute(sql)
    paikat = kursori.fetchall()


    # NÄYTETÄÄN VAIHTOEHDOT

    print("1:", paikat[0][0], "-", paikat[0][1], "(-1 päivä)")
    print("2:", paikat[1][0], "-", paikat[1][1], "(-2 päivää)")
    print("3:", paikat[2][0], "-", paikat[2][1], "(-3 päivää)")

    valinta = int(input("Valitse 1, 2 tai 3 : "))


    # PELAAJAN VALINTA

    if valinta == 1:

        paikka = paikat[0]
        aika = aika - 1

    elif valinta == 2:

        paikka = paikat[1]
        aika = aika - 2

    elif valinta == 3:

        paikka = paikat[2]
        aika = aika - 3

    else:

        print("Valitse 1, 2 tai 3!")
        continue


    # LASKEUTUMINEN

    print()
    print("Laskeuduit:", paikka[0])
    print("Maa:", paikka[1])
    print("Aikaa jäljellä:", aika, "päivää")
    print("Pisteet:", pisteet)


    # TAPAHTUMA

    if aika > 0:

        print()
        print("----- TAPAHTUMA -----")

        tapahtuma_tyyppi = random.randint(1, 2)

        if tapahtuma_tyyppi == 1:

            positiivinen = positiivinen_tapahtuma()

            if positiivinen:
                vaikutus = float(positiivinen[1])
                tulos = tapahtuman_pisteytys(vaikutus, valinta)
                pisteet = pisteet + tulos

                print("Lopullinen vaikutus pisteisiin:", tulos)
                print(f"Pisteet yhteensä: {pisteet:.2f}")

        else:

            negatiivinen = negatiivinen_tapahtuma()

            if negatiivinen:
                vaikutus = float(negatiivinen[1])
                tulos = tapahtuman_pisteytys(vaikutus, valinta)
                pisteet = pisteet + tulos

                print("Lopullinen vaikutus pisteisiin:", tulos)
                print(f"Pisteet yhteensä: {pisteet:.2f}")


# PELI LOPPUU

print()
print("========================")
print("Aika loppui!")
print("Peli päättyi.")
print("Lopulliset pisteet:", pisteet)
print("========================")

yhteys.close()