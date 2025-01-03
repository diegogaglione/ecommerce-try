import utente, prodotto, carrello
while True:
    print("""Inserisci:
1 se vuoi registrare un prodotto, 
2 se vuoi mostrare tutti i prodotti,
3 se vuoi aggiungere un prodotto al carrello, 
4 se vuoi mostrare il carrello,
5 se vuoi eliminare un prodotto dal carrello,
6 se vuoi eliminare un prodotto.
    """)
    scelta = input()
    if scelta == "1":
        prodotto.classe_prodotto.registra_prodotto()
    elif scelta == "2":
        prodotto.classe_prodotto.mostra_prodotti()
    elif scelta == "3":
        carrello.classe_carrello.aggiungi_al_carrello()
    elif scelta == "4":
        carrello.classe_carrello.mostra_carrello()
    elif scelta == "5":
        carrello.classe_carrello.elimina_prodotto()
    elif scelta == "6":
        prodotto.classe_prodotto.elimina_prodotto()