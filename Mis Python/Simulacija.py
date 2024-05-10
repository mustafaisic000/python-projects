#Kratki program za simulaciju dolaska 100 kupaca u vremenu od 1-10 minuta ako je prosjek dolaska 5, a obrada svakog zahtjeva kupca traje 3-9 minute.
#Ova simulacija koristi FIFO (prvi došao, prvi poslužen) metodu čekanja, s redovima koji se poslužuju prema principu ko prvi dođe, prvi poslužen. Dodatno, 
#model uključuje Nonstationary Poissonov proces koji bilježi dinamiku dolazaka kupaca tokom vremena.
#Kod je napravljen za moj rad "Simuliranje rada kase u trgovini" za predmet "Modeliranje i Simulaciju" 
from scipy.stats import poisson
import numpy as np

# Broj dolazaka
broj_dolazaka = 100

# Generiranje vremena dolazaka
prosjek_dolazaka = 5
distribucija_dolazaka = poisson(mu=prosjek_dolazaka)
vremena_dolazaka = distribucija_dolazaka.rvs(size=broj_dolazaka)
ogranicena_vremena_dolazaka = np.clip(vremena_dolazaka, 1, 10)

# Generiranje vremena obrade zahtjeva
prosjek_obrade = 6
distribucija_obrade = poisson(mu=prosjek_obrade)
vremena_obrade = distribucija_obrade.rvs(size=broj_dolazaka)
ogranicena_vremena_obrade = np.clip(vremena_obrade, 3, 9)

# Ispis rezultata
print("Vremena dolazaka:")
print(ogranicena_vremena_dolazaka)
print()
print("Vremena obrade:")
print(ogranicena_vremena_obrade)
