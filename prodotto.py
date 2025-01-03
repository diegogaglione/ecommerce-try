class Prodotto():
    def __init__(self, nome_prodotto=None, quantita_prodotto=None, prezzo_prodotto=None):
        self.prodotti = {}
        self.nome_prodotto = nome_prodotto
        self.quantita_prodotto = quantita_prodotto
        self.prezzo_prodotto = prezzo_prodotto
    def registra_prodotto(self):
        nome_prodotto = input("Inserisci il nome del prodotto: \n")
        quantita_prodotto = int(input("Inserisci il quantita del prodotto: \n"))
        prezzo_prodotto = float(input("Inserisci il prezzo del prodotto: \n"))
        self.prodotti[len(self.prodotti) + 1] = Prodotto(nome_prodotto, quantita_prodotto, prezzo_prodotto)
    def mostra_prodotti(self):
        for prodotto in self.prodotti:
            print(f"Nome: {self.prodotti[prodotto].nome_prodotto}\n   Quantità: {self.prodotti[prodotto].quantita_prodotto}\n   Prezzo: {self.prodotti[prodotto].prezzo_prodotto}$\n")
    def elimina_prodotto(self):
        del self.prodotti[input("Inserisci il nickname del prodotto da eliminare")]
    def cerca_articolo_nome(self):
        for prodotto in self.prodotti:
            if input("Inserisci il nome del prodotto da trovare: \n") == self.prodotti[prodotto].nome_prodotto:
                print(f"Nome: {self.prodotti[prodotto].nome_prodotto}\n   Quantità: {self.prodotti[prodotto].quantita_prodotto}\n   Prezzo: {self.prodotti[prodotto].prezzo_prodotto}$\n")
                break
classe_prodotto = Prodotto()
        