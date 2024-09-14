# Bibliotecas
import json
import unittest
from unittest.mock import MagicMock, patch
from atendimento import get_atendimento, calc_predio

# Teste unitário
class TestAtendimento(unittest.TestCase):
    # Configuração inicial do Mock
    def setUp(self):
        # Carregar o JSON do arquivo
        with open("mock_atendimento.txt", 'r') as file:
            json_str = file.read()
            self.data = json.loads(json_str)
        
        # Configuração do mock para a requisição requests.get
        self.patcher = patch('atendimento.requests.get')
        self.mock_get = self.patcher.start()
        
        # Configuração padrão do mock
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = self.data
        self.mock_get.return_value = self.mock_response

    # Ainda configuração do Mock
    def tearDown(self):
        self.patcher.stop()
        
    # Início dos testes
    # ... Sucesso
    
    # Testa resultado da função que calcula a sala
    def test_calc_predio(self):
        self.assertEqual(calc_predio('1'), '1')  # Sala 1 deve resultar em predio = 1
        self.assertEqual(calc_predio('5'), '1')  # Sala 5 deve resultar em predio = 1
        self.assertEqual(calc_predio('6'), '2')  # Sala 6 deve resultar em predio = 2
        self.assertEqual(calc_predio('10'), '2')  # Sala 10 deve resultar em predio = 2
        self.assertEqual(calc_predio('11'), '3')  # Sala 11 deve resultar em predio = 3
        
    # Testa se as informações são um dicionário
    def test_get_atendimento_type(self):
        data = get_atendimento()
        self.assertIsInstance(data, dict)

    # Testa se as informações batem
    def test_get_atendimento_values(self):
        data = get_atendimento()
        self.assertEqual(data['nomeDoProfessor'], 'Christopher')
        self.assertEqual(data['horarioDeAtendimento'], 'Sexta-feira, 19:00')
        self.assertEqual(data['periodo'], 'Noturno')
        self.assertEqual(data['sala'], '6')
        
    # Testa os tipos das informações retornadas, separadamente
    def test_get_atendimento_values_type(self):
        data = get_atendimento()
        self.assertIsInstance(data['nomeDoProfessor'], str)
        self.assertIsInstance(data['sala'], str)
        self.assertIsInstance(data['periodo'], str)
        self.assertIsInstance(data['predio'], list)
        self.assertIsInstance(data['horarioDeAtendimento'], str)
        
    # Testa se as chaves chegam corretamente
    def test_get_atendimento_keys(self):
        data = get_atendimento()
        expected_keys = {'nomeDoProfessor', 'horarioDeAtendimento', 'sala', 'predio', 'periodo'}
        self.assertTrue(expected_keys.issubset(data.keys()))
        
    # Testa se o valor da sala está no alcance permitido
    def test_get_atendimento_sala_range(self):
        data = get_atendimento()
        self.assertGreaterEqual(int(data['sala']), 1)
        self.assertLessEqual(int(data['sala']), 25)
        
    # ... Falha
    
    # Testa como se comporta quando recebe um dicionário vazio do servidor
    def test_get_atendimento_empty_response(self):
        self.mock_response.json.return_value = {}
        data = get_atendimento()
        self.assertEqual(data, {})
    
# Rodar os testes
if __name__ == '__main__':
    unittest.main()
