from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationsUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('admin', password='admin')

    def test_authenticacao_user_com_credenciais_corretas(self):
        """Test que verificar authenticação de user com credenciais corretas"""
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_GET_nao_autorizada(self):
        """Test que verifica uma requisição GET não autorizada"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticacao_de_user_com_username_incorreto(self):
        """Test que verifica authenticação de user com username incorreto"""
        user = authenticate(username='admi', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authenticacao_de_user_com_password_incorreto(self):
        """Test que verifica authenticação de user com password incorreto"""
        user = authenticate(username='admin', password='administracao')
        self.assertFalse((user is not None) and user.is_authenticated)