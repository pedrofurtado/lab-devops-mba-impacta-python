from main import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.result = self.app.get('/')
        self.soma = self.app.get('/soma')

    def test_requisicao(self):
        self.assertEqual(self.result.status_code, 200)
        self.assertEqual(self.soma.status_code, 200)

    def test_conteudo(self):
        self.assertEqual(self.result.data.decode('utf-8'), "Hello World - Pedro Furtado - Lab DevOps Impacta")
        self.assertEqual(self.soma.data.decode('utf-8'), "Sua soma de 10+10=20")
