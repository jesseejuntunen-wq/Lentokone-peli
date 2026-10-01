import mysql.connector
import random
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database='flight_game',
    user='root',
    password="301105",
    autocommit=True
)

print("Valitse näistä maanosista aloituspisteesi")
print("1: EU, 2: NA, 3: SA, 4: AS, 5: AF,  ")
aloitus_valinta=int(input("Valitse mistä maanosasta haluat aloittaa: "))
maanosat={1: "EU", 2:"NA", 3:"SA", 4:"AS", 5:"AF"}
valittu_maanosa=maanosat.get(aloitus_valinta)
def aloituspaikan_luonti(aloitus_paikka):
    sql=("select airport.name, country.name from airport join country on airport.iso_country = country.iso_country where country.continent = %s order by rand() limit 1")
    print(sql)
    kursori=yhteys.cursor() 
    kursori.execute(sql, (aloitus_paikka,))
    tulos=kursori.fetchone()
    if tulos:
        print(f"Aloituspaikkasi on: {tulos[0]}")
        return tulos[0]
    
    
    
      

aloituspaikan_luonti(valittu_maanosa)