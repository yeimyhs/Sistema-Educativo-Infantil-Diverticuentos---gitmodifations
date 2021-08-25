from rest_framework.routers import SimpleRouter
from DivertiCuentos import views

from knox import views as knox_views
#from .views import LoginAPI
from .views import *
from django.urls import path , re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import include

from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer

schema_view = get_schema_view(
   openapi.Info(
      title="Lonccosv3 API",
      default_version='v3',
      description="Diverticuentos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
'''
decorated_login_view = \
   swagger_auto_schema(
      method='post',
      request_body={AuthTokenSerializer}
   )(LoginAPI.as_view())
   '''
urlpatterns = [
    
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),#cuando inicia sesion en varios browser y quiere salir de todos


    path('searchbyName/<str:args>/', searchbyName.as_view()),
    path('searchEmail/<str:args>/', searchEmail.as_view()),
    path('searchStoryGroup/<int:pk>/', searchStoryGroup.as_view()),
    path('searchStoryUser/<int:pk>/', searchStoryUser.as_view()),
    path('searchGroups/<int:pk>/', searchGroups.as_view()),
    path('searchMembers/<int:pk>/', searchMembers.as_view()),

    path('userbyToken/', UserAPI.as_view()),

    re_path(r'^swagger(<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
router = SimpleRouter()

router.register(r'answer', views.AnswerViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'dictionary', views.DictionaryViewSet)
router.register(r'examplesdictionay', views.ExamplesdictionayViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'history', views.HistoryViewSet)
router.register(r'preference', views.PreferenceViewSet)
router.register(r'readinglist', views.ReadinglistViewSet)
router.register(r'story', views.StoryViewSet)
router.register(r'suggestion', views.SuggestionViewSet)
router.register(r'userp', views.UserPViewSet)
router.register(r'usergroup', views.UsergroupViewSet)

urlpatterns += router.urls
