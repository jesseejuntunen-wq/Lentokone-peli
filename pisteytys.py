import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="301105",
    autocommit=True
)
def negatiivinen_tapahtuma():
    sql = "select nimi, aika_muutos from tapahtumat order by rand() limit 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchone()
    if tulos:
        print(f"Tapahtuma: {tulos[0]} ja vaikutus {tulos[1]}")
        return tulos
def positiivinen_tapahtuma():
    sql="select nimi, vaikutus from pos_tapahtumat order by rand() limit 1 "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchone()
    if tulos:
        print(f"Tapahtuma: {tulos[0]} ja vaikutus {tulos[1]}")
        return tulos
positiivinen_tapahtuma()
negatiivinen_tapahtuma()
    