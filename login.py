import utente
def login():
    while True:
                nome_prodotto = input("Inserisci il nickname dell'utente \n")
                for oggetto in utente.classe_utenti.utenti:
                    if nome_prodotto == utente.classe_utenti.utenti[oggetto].nick_utente:
                        password = input("Inserisci la password: ")
                        if password == utente.classe_utenti.utenti[oggetto].pass_utente:
                            return 1
                        break
                    break
                break