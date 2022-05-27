from model.Rubrica import Rubrica
from model.Contatto import Contatto

rubricaAmici = Rubrica()
print(len(rubricaAmici))
rubricaAmici.aggiungiContatto("Alessandro", "Migliore", "3297979777")
rubricaAmici.aggiungiContatto("Davide", "Ferrara", "3398756289")
rubricaAmici.aggiungiContatto("Luca", "Casale", "3459167898")
rubricaAmici.aggiungiContatto("Maria", "Spinazola", "3474867581")
print(len(rubricaAmici))
rubricaAmici.getContatto(2)
rubricaAmici.elencoContatti()
rubricaAmici.eliminaContatto(1)
print(rubricaAmici.cercaContatto("Alessandro"))