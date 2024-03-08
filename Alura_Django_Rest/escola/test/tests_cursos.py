from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import  reverse
from rest_framework import status
from django.contrib.auth.models import User

class CursosTestCase(APITestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(username='admin', password='admin')
        self.client.force_authenticate(user=self.usuario)
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo = 'CTT1', descricao='Curso teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo='CTT2', descricao='Curso teste 2', nivel='A'
        )

    def test_requisicao_GET_para_listar_cursos(self):
        """Teste para verificar se a requisição GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    # def test_requisicao_POST_para_criar_cursos(self):
    #     """Teste para verificar se a requisição POST para criar um curso"""
    #     data = {'codigo': 'CTT3', 'descricao': 'Curso teste 3', 'nivel': 'A'}
    #     response = self.client.post(self.list_url, data=data)
    #     self.assertEquals(response.status_code, status.HTTP_201_CREATED)