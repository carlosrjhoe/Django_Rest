from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse

class CursosTestCase(APITestCase):
    
    def setUp(self) -> None:
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo='CTT1', descricao='Curso de teste 1', nivel='A'
        )
        self.curso_2 = Curso.objects.create(
            codigo='CTT2', descricao='Curso de teste 2', nivel='I'
        )

    def test_falhador(self):
        self.fail('Teste falhou')