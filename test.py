from main import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.result = self.app.get('/')

    def test_requisicao(self):
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        self.assertEqual(self.result.data.decode('utf-8'), "Hello World - Pedro Furtado - Lab DevOps Impacta")
