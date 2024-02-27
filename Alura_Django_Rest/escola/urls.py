from rest_framework.routers import DefaultRouter
from escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet

app_name = 'escola'

router = DefaultRouter(trailing_slash = False)
router.register(r'alunos', AlunoViewSet, basename = 'Aluno')
router.register(r'cursos', CursoViewSet, basename = 'Cursos')
router.register(r'matriculas', MatriculaViewSet, basename = 'Matriculas')
urlpatterns = router.urls
