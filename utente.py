class Utente():
    def __init__(self, nick_utente=None, pass_utente=None, nome_utente=None, cognome_utente=None, eta_utente=None):
        self.utenti = {}
        self.nick_utente = nick_utente
        self.pass_utente = pass_utente
        self.nome_utente = nome_utente
        self.cognome_utente = cognome_utente
        self.eta_utente = eta_utente
    def registra_utente(self):
        while True:
            nick_utente = input("Inserisci il nickname dell'utente: \n")
            if nick_utente in self.utenti:
                print("Nickname già utilizzato!")
            elif nick_utente not in self.utenti:    
                break
        pass_utente = input("Inserisci la password dell'utente: \n")
        nome_utente = input("Inserisci il nome dell'utente: \n")
        cognome_utente = input("Inserisci il cognome dell'utente: \n")
        eta_utente = int(input("Inserisci l'età dell'utente: \n"))
        self.utenti[len(self.utenti) + 1] = Utente(nick_utente, pass_utente, nome_utente, cognome_utente, eta_utente)
    def mostra_utenti(self):
        for utente in self.utenti:
            print(f"Nickname: {self.utenti[utente].nick_utente}\n   Nome: {self.utenti[utente].nome_utente}\n   Cognome: {self.utenti[utente].cognome_utente}\n   Età: {self.utenti[utente].eta_utente}\n")
    def elimina_utente(self):
        del self.utenti[input("Inserisci il nickname dell'utente da eliminare")]
classe_utenti = Utente()