from unittest.case import TestCase


class Noh:
    def __init__(self):
        self.valor = None
        self.proximo_noh = None


class ListaLigadaSimples:
    def __init__(self):
        self.inicio = None  # aponta para o Noh inicial


def adicionar(lista, valor):
    noh = Noh()
    noh.valor = valor
    if lista.inicio is None:
        lista.inicio = noh
    else:
        ultimo_noh = lista.inicio
        while ultimo_noh.proximo_noh != None:
            ultimo_noh = ultimo_noh.proximo_noh
        ultimo_noh.proximo_noh = noh


class TestesDeAdicaoEmListaSimples(TestCase):
    def testar_inicializar(self):
        lista = ListaLigadaSimples()
        self.assertIsNone(lista.inicio)

    def testar_adição_de_um_elemento(self):
        lista = ListaLigadaSimples()
        adicionar(lista, 'A')
        noh_inicial = lista.inicio
        self.assertIsNotNone(noh_inicial)
        self.assertEqual('A', noh_inicial.valor)

    def testar_adição_de_dois_elementos(self):
        lista = ListaLigadaSimples()
        adicionar(lista, 'A')
        noh_inicial = lista.inicio
        adicionar(lista, 'B')
        noh_final = noh_inicial.proximo_noh
        self.assertIsNotNone(noh_final)
        self.assertEqual('B', noh_final.valor)
        self.assertIsNone(noh_final.proximo_noh)
