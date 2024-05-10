#Kategorisanje studenata po broju položenih predmeta i prosjeku koji su ostvarili kad su prvi put bili prva godina
#Prvo sam podatke preuzeo i pripremio za obradu koristeći Excel file. Nakon pripreme, otkucao sam Python kod
#kako bih dobio kategorije studenata u ispisu
import pandas as pd
from datetime import datetime

df = pd.read_excel('GotoviPodaciStudenata.xlsx')

# Funkcija za kategorizaciju studenata
def kategorizacija(row):
    # Ako student nije položio 5 ispita, kategorija je 0
    if row['BrojPoloženih'] != 5:
        return 0
    # Ako je zadnji ispit položen nakon novembra sljedeće godine, kategorija je 0
    zadnji_ispit_datum = row['ZadnjiPolozenIspitPrvogSemestra']
    novembar_naredne_godine = datetime(row['GodinaUpisa'] + 1, 11, 1)
    if zadnji_ispit_datum > novembar_naredne_godine:
        return 0
    # Ako je prosjek ocjena manji od 8, kategorija je 1, inače je 2
    prosjek_ocjena = row['Grand Total'] 
    if prosjek_ocjena < 8.0:
        return 1
    else:
        return 2

# Dodavanje nove kolone "Kategorija"
df['Kategorija'] = df.apply(kategorizacija, axis=1)


pd.set_option('display.max_rows', None)

print(df)
