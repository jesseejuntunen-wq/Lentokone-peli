import mysql.connector
import random
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="301105",
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
print("1 = lähellä oleva lentokenttä (-1 päivä)")
print("2 = kauempana oleva lentokenttä (-2 päivää)")
print("3 = todella kaukana oleva lentokenttä (-3 päivää)")
print()
print("Laskeutumisen jälkeen voi tapahtua")
print("positiivinen tai negatiivinen tapahtuma.")
print("Tapahtumat vaikuttavat pisteisiisi.")
print()
print("Peli päättyy, kun 30 päivää on käytetty.")
print("Yritä saada mahdollisimman paljon pisteitä!")
print()
print("========================")
input("Paina Enter aloittaaksesi pelin...")
print()


def positiivinen_tapahtuma():
    sql = "SELECT nimi, vaikutus FROM pos_tapahtumat ORDER BY RAND() LIMIT 1"
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if tulos:
        print("Tapahtuma:", tulos[0])
        return tulos


def negatiivinen_tapahtuma():
    sql = "SELECT nimi, aika_muutos FROM tapahtumat ORDER BY RAND() LIMIT 1"
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if tulos:
        print("Tapahtuma:", tulos[0])
        return tulos


def tapahtuman_pisteytys(vaikutus, valinta):
    if valinta == 1:
        return round(vaikutus, 2)

    elif valinta == 2:
        return round(vaikutus * 1.2, 2)

    elif valinta == 3:
        return round(vaikutus * 1.3, 2)


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
SELECT airport.name, country.name,
airport.latitude_deg, airport.longitude_deg
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
    SELECT airport.name, country.name,
    airport.latitude_deg, airport.longitude_deg
    FROM airport
    JOIN country
    ON airport.iso_country = country.iso_country
    WHERE airport.latitude_deg IS NOT NULL
    AND airport.longitude_deg IS NOT NULL
    ORDER BY RAND()
    LIMIT 100
    """

    kursori.execute(sql)
    lentokentat = kursori.fetchall()

    nykyinen_sijainti = (paikka[2], paikka[3])

    lahella = []
    kaukana = []
    tosi_kaukana = []

    for lentokentta in lentokentat:

        lentokentan_sijainti = (
            lentokentta[2],
            lentokentta[3]
        )

        etaisyys = geodesic(
            nykyinen_sijainti,
            lentokentan_sijainti
        ).km

        if 100 <= etaisyys < 1000:
            lahella.append(lentokentta + (etaisyys,))

        elif 1000 <= etaisyys < 4000:
            kaukana.append(lentokentta + (etaisyys,))

        elif etaisyys >= 4000:
            tosi_kaukana.append(lentokentta + (etaisyys,))


    # VALITAAN YKSI JOKAISESTA ETÄISYYDESTÄ

    paikka1 = random.choice(lahella)
    paikka2 = random.choice(kaukana)
    paikka3 = random.choice(tosi_kaukana)

    paikat = [paikka1, paikka2, paikka3]


    # NÄYTETÄÄN VAIHTOEHDOT

    print("1:", paikat[0][0], "-", paikat[0][1],
          "-", round(paikat[0][4]), "km (-1 päivä)")

    print("2:", paikat[1][0], "-", paikat[1][1],
          "-", round(paikat[1][4]), "km (-2 päivää)")

    print("3:", paikat[2][0], "-", paikat[2][1],
          "-", round(paikat[2][4]), "km (-3 päivää)")

    valinta = int(input("Valitse 1, 2 tai 3: "))


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

            tapahtuma = positiivinen_tapahtuma()

        else:

            tapahtuma = negatiivinen_tapahtuma()

        if tapahtuma:

            vaikutus = float(tapahtuma[1])

            tulos = tapahtuman_pisteytys(
                vaikutus,
                valinta
            )

            pisteet = pisteet + tulos

            print("Vaikutus pisteisiin:", tulos)
            print("Pisteet yhteensä:", pisteet)


# PELI LOPPUU

print()
print("========================")
print("Aika loppui!")
print("Peli päättyi.")
print("Lopulliset pisteet:", pisteet)
print("========================")

yhteys.close()