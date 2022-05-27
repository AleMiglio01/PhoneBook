class Contatto:
    def __init__(self, nome, cognome, numero, rubrica ):
        self.nome = nome
        self.cognome = cognome
        self.numero = numero
        self.rubrica = rubrica
    def stringaContatto(self):
        str = self.nome +" "+ self.cognome +" "+ self.numero
        return str

