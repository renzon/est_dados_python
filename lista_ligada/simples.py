from unittest.case import TestCase


class Nó:
    def __init__(self):
        self.valor = None
        self.proximo_noh = None


class ListaLigadaSimples:
    def __init__(self):
        self.inicio = None  # aponta para o Nó inicial
        self.tamanho = 0


class TestesDeAdicaoEmListaSimples(TestCase):
    def testar_inicializar(self):
        lista = ListaLigadaSimples()
        self.assertIsNone(lista.inicio)
        self.assertEqual(0, lista.tamanho)

    def testar_adiciao_de_um_elemento(self):
        lista = ListaLigadaSimples()
        adicionar(lista, 'A')
        noh_inicial = lista.inicio
        self.assertIsNotNone(noh_inicial)
        self.assertEqual('A', noh_inicial.valor)
