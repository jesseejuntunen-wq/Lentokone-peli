import mysql.connector
import random

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    user="Jesse",
    password="Jesse0802",
    database="flight_game"
)

kursori = yhteys.cursor()

aika = 30

kursori.execute("SELECT nimi, aika_muutos FROM tapahtumat")
tapahtumat = kursori.fetchall()

while aika > 0:

    tapahtuma = random.choice(tapahtumat)

    print("Oho!", tapahtuma[0])

    aika = aika + tapahtuma[1]

    print("Aikaa jäljellä:", aika)
    print()

print("Hieno homma kaikki kuoli, Good job")

yhteys.close()