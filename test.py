class Negozio():
    def __init__(self):
        self.nome_negozio = "Negozio PCTO"


class Articolo():
    def __init__(self, id_articolo=None, nome_articolo=None, prezzo_articolo=None):
        self.articoli = {}
        self.id_articolo = id_articolo
        self.nome_articolo = nome_articolo
        self.prezzo_articolo = prezzo_articolo

    def aggiungi_articolo(self):
        print("Inserisci: \n")
        id_articolo = input("Id dell'articolo: \n")
        nome_articolo = input("Nome dell'articolo: \n")
        prezzo_articolo = input("Prezzo dell'articolo: \n")
        self.articoli[nome_articolo] = Articolo(id_articolo, nome_articolo, prezzo_articolo)
        print(f"Articolo aggiunto con successo:\n {self.articoli[nome_articolo]}")
    def __str__(self):
        return f"Articolo: {self.id_articolo}\n Nome: {self.nome_articolo}\n Prezzo: {self.prezzo_articolo}$\n"
    def mostra_articoli(self):
        for articolo in self.articoli:
            print(self.articoli[articolo])
    def rimuovi_articolo(self):
        rimuovi_articolo = input("Inserisci il nome dell'articolo da eliminare: ")
        del self.articoli[rimuovi_articolo]
        

class Carrello():
    def __init__(self):
        self.carrello = {}

class Utente():
    def __init__(self, id_utente=None, nome_utente=None):
        self.utenti = {}
        self.id_utente = id_utente
        self.nome_utente = nome_utente

    def aggiungi_utente(self):
        print("Inserisci: \n")
        id_utente = input("Id dell'utente: \n")
        nome_utente = input("Nome dell'utente: \n")
        self.utenti[nome_utente] = Articolo(id_utente, nome_utente)
        print(f"Utente aggiunto con successo:\n {self.utenti[nome_utente]}")
    def __str__(self):
        return f"Utente: {self.id_utente}\n Nome: {self.nome_utente}\n"
    def mostra_utenti(self):
        for utente in self.utenti:
            print(self.utenti[utente])
    def rimuovi_utente(self):
        rimuovi_utente = input("Inserisci il nome dell'utente da eliminare: ")
        del self.utenti[rimuovi_utente]
articolo_classe = Articolo()
utente_classe = Utente()
