import prodotto
class Carrello():
    def __init__(self, nome_prodotto=None, quantita_prodotto=None, prezzo_prodotto=None):
        self.carrello = {}
        self.nome_prodotto = nome_prodotto
        self.quantita_prodotto = quantita_prodotto
        self.prezzo_prodotto = prezzo_prodotto
    def aggiungi_al_carrello(self):
        while True:
            nome_prodotto = input("Inserisci il nome del prodotto: \n")
            for oggetto in prodotto.classe_prodotto.prodotti:
                if nome_prodotto == prodotto.classe_prodotto.prodotti[oggetto].nome_prodotto:
                    prodotto.classe_prodotto.prodotti[oggetto].quantita_prodotto -= 1
                    quantita_prodotto = prodotto.classe_prodotto.prodotti[oggetto].quantita_prodotto
                    prezzo_prodotto = prodotto.classe_prodotto.prodotti[oggetto].prezzo_prodotto
                    self.carrello[oggetto] = Carrello(nome_prodotto, quantita_prodotto, prezzo_prodotto)
                    break
                break
            break

    def mostra_carrello(self):
        for prodotto in self.carrello:
            print(f"Nome: {self.carrello[prodotto].nome_prodotto}\n   Quantità: {self.carrello[prodotto].quantita_prodotto}\n   Prezzo: {self.carrello[prodotto].prezzo_prodotto}$\n")
    def elimina_prodotto(self):
        eliminare = input("Inserisci il nome del prodotto da eliminare dal carrello: \n")
        for elemento in self.carrello:
            if elemento.nome_prodotto == eliminare:
                del self.carrello[elemento]
                prodotto.classe_prodotto.prodotti[elemento].quantita_prodotto += 1
                break
            break
classe_carrello = Carrello()