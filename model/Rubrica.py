from model.Contatto import Contatto

class Rubrica():
    def __init__(self):
        self.contatti = []

    def aggiungiContatto(self, nome, cognome, numero):
        con = Contatto(nome, cognome, numero, self)
        self.contatti.append(con)
        print("Contatto inserito", nome, cognome, numero)

    def getContatto(self, position):
        print("Posizione:" , self.contatti[position].stringaContatto())

    def eliminaContatto(self, position):
        #print("Rubrica:", self.contatti)
        del self.contatti[position]

    # restituisce una stringa con l'elenco delle voci della rubrica separate
    # da ", "; l'elenco inizia con "(" e termina con ")"
    def elencoContatti(self):
        str = "("
        for contatto in self.contatti:
            str += contatto.nome + " " + contatto.cognome + " " + contatto.numero + ","
        str=str[:len(str)-1] + ")"
        print(str)

    def __len__(self):
        return len(self.contatti)

    #restituisce la stringa corrispondente alla prima voce che contiene
    # il parametro key come nome, cognome oppure telefono.
    def cercaContatto(self, key):
        for contatto in self.contatti:
            if contatto.nome == key or contatto.cognome == key or contatto.numero == key:
             #print(contatto)
              return contatto.stringaContatto()
            #raise ContattoNotFound()