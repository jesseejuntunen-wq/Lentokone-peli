import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="Jesse",
    password="Jesse0802",
    autocommit=True
)

print("Valitse näistä maanosista aloituspisteesi")
print("1: EU, 2: NA, 3: SA, 4: AS, 5: AF")

aloitus_valinta = int(input("Valitse mistä maanosasta haluat aloittaa: "))

maanosat = {
    1: "EU",
    2: "NA",
    3: "SA",
    4: "AS",
    5: "AF"
}

valittu_maanosa = maanosat.get(aloitus_valinta)


def aloituspaikan_luonti(maanosa):

    sql = """
    SELECT airport.name, country.name
    FROM airport
    JOIN country
    ON airport.iso_country = country.iso_country
    WHERE country.continent = %s
    ORDER BY RAND()
    LIMIT 1
    """

    kursori = yhteys.cursor()

    kursori.execute(sql, (maanosa,))
    tulos = kursori.fetchone()

    if tulos:
        print()
        print(f"Aloituspaikkasi on: {tulos[0]}")
        print(f"Maa: {tulos[1]}")

        return tulos[0]


aloituspaikan_luonti(valittu_maanosa)

yhteys.close()