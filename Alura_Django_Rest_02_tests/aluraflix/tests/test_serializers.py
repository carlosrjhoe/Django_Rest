from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializersTestCase(TestCase):

    def setUp(self) -> None:
        self.programa = Programa(
            titulo = 'Procurando ninguém',
            tipo = 'F',
            data_lancamento = '2024-07-04',
            likes = 2345,
            dislikes = 40,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verica_campos_serializados(self):
        """Teste que verifica campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEquals(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica os conteudos dos campos serializados"""
        data = self.serializer.data
        self.assertEquals(data['titulo'], self.programa.titulo)
        self.assertEquals(data['tipo'], self.programa.tipo)
        self.assertEquals(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEquals(data['likes'], self.programa.likes)