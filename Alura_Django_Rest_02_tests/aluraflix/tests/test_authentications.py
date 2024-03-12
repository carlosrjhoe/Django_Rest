from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class AuthenticationsUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user('c3po', password='admin')

    def test_authenticacao_user_com_credenciais_corretas(self):
        """Test que verificar authenticação de user com credenciais corretas"""
        user = authenticate(username='c3po', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)