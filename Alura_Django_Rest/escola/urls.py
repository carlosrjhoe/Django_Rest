from rest_framework.routers import DefaultRouter
from escola.views import AlunoViewSet, CursoViewSet

app_name = 'escola'

router = DefaultRouter(trailing_slash = False)
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
urlpatterns = router.urls
