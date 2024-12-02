class Articolo():
    def __init__(self, id, nome, prezzo, quantita):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
    def __str__(self):
        return f"Articolo: {self.id}\nNome: {self.nome}, Prezzo: €{self.prezzo}, Quantità: {self.quantita}\n"
class Utente():
    def __init__(self, nick_utente, nome_utente, cognome_utente, eta_utente):
        self.nick_utente = nick_utente
        self.nome_utente = nome_utente
        self.cognome_utente = cognome_utente
        self.eta_utente = eta_utente
    def __str__(self):
        return f"Utente: {self.nick_utente}\nNome: {self.nome_utente}, Cognome: {self.cognome_utente}, Età: {self.eta_utente}\n"



class GestisciNegozio():
    def __init__(self):
        self.articoli = {}
        self.utenti = {}
    def aggiungi_articolo(self):
        nome = input("Inserisci il nome dell'articolo: ")
        id = input("Inserisci l'id dell'articolo: ")
        prezzo = float(input("Inserisci il prezzo dell'articolo: "))
        quantita = input("Inserisci la quantità dell'articolo: ")
        self.articoli[nome] = Articolo(id, nome, prezzo, quantita)
    def mostra_articoli(self):
        for articolo in self.articoli:
            print(self.articoli[articolo])
    def aggiungi_utente(self):
        nick_utente = input("Inserisci il nickname dell'utente")
        nome_utente = input("Inserisci il nome dell'utente: ")
        cognome_utente = input("Inserisci il cognome dell'utente: ")
        eta = int(input("Inserisci l'età dell'utente: "))
        self.utenti[nick_utente] = Utente(nick_utente, nome_utente, cognome_utente, eta)
    def mostra_utenti(self):
        for utente in self.utenti:
            print(self.utenti[utente])
    def login(self, nick):
        if nick in self.utenti:
            return True

gnegozio = GestisciNegozio()
def gestionale():
    while True:
        scelta = input("Inserisci 1 se vuoi aggiungere un articolo, Inserisci 2 se vuoi visualizzare il catalogo, Inserisci 3 se vuoi visualizzare un utente, Inserisci 4 se vuoi uscire")
        if scelta == "1":
            gnegozio.aggiungi_articolo()
        elif scelta == "2":
            gnegozio.mostra_articoli()
        elif scelta == "3":
            gnegozio.mostra_utenti()
        if scelta == "4":
            break
def pseudosito():
    while True: 
        scelta = input("Per iniziare ad utilizzare il sito è necessario accedere (1) o registrarsi (2)")
        if scelta == "1":
            scelta = input("Inserisci le credenziali")
            if gnegozio.login(scelta) is True:
                break
        if scelta == "2":
            gnegozio.aggiungi_utente()
pseudosito()
