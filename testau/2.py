import mysql.connector

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


# PELI

while aika > 0:

    print()
    print("------------------------")
    print("Valitse seuraava lentokenttä:")


    # HAETAAN 2 SATUNNAISTA LENTOKENTTÄÄ

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

    else:

        print("Valitse 1 tai 2!")
        continue


    # LASKEUTUMINEN

    print()
    print("Laskeuduit:", paikka[0])
    print("Maa:", paikka[1])
    print("Aikaa jäljellä:", aika, "päivää")


# PELI LOPPUU

print()
print("========================")
print("Aika loppui!")
print("Peli päättyi.")
print("========================")

yhteys.close()