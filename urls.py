from rest_framework.routers import SimpleRouter
from DivertiCuentos import views

from knox import views as knox_views
#from .views import LoginAPI
from .views import *
from django.urls import path , re_path, reverse

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url, include
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_complete, password_reset_confirm
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView

from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.conf import settings
from django.conf.urls.static import static
from .views import home, send_push


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

decorated_logout_view = \
   swagger_auto_schema(
      'Authorization :: header for token authentication'
      #request_body={AuthTokenSerializer}
   )(knox_views.LogoutView.as_view())
#app_name = 'DivertiCuentos'  
#https://www.ordinarycoders.com/blog/article/django-password-reset reset password
urlpatterns = [
    
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/',decorated_logout_view, name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),#cuando inicia sesion en varios browser y quiere salir de todos

    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
       template_name='password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
       template_name="password_reset/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
       template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),      
    

   path('s', home),
   path('send_push', send_push),
   path('webpush/', include('webpush.urls')),

    path('searchbyName/<str:args>/', searchbyName.as_view()),
    path('searchEmail/<str:args>/', searchEmail.as_view()),
    path('searchStoryGroup/<int:pk>/', searchStoryGroup.as_view()),
    path('searchStoryUser/<int:pk>/', searchStoryUser.as_view()),
    path('searchGroups/<int:pk>/', searchGroups.as_view()),
    path('searchMembers/<int:pk>/', searchMembers.as_view()),
    path('mailer/', mailer.as_view()),

    path('userbyToken/', UserAPI.as_view()),

    re_path(r'^swagger(<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path('sw.js', TemplateView.as_view(template_name='./sw.js', content_type='application/x-javascript')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

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


'''search   re_path(r'^password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(
       template_name='resetAccount/password_reset_complete.html'), name='password_reset_complete'),     '''