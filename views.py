from rest_framework.viewsets import ModelViewSet
from DivertiCuentos.serializers import AnswerSerializer, CommentSerializer, DictionarySerializer, ExamplesdictionaySerializer, GroupSerializer, HistorySerializer, PreferenceSerializer, ReadinglistSerializer, StorySerializer, SuggestionSerializer, UserPSerializer, UsergroupSerializer
from DivertiCuentos.models import Answer, Comment, Dictionary, Examplesdictionay, Group, History, Preference, Readinglist, Story, Suggestion, UserP, Usergroup
from .serializers import *
#----------------------------------------------------------------------service imports
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, permissions
#----------------------------------------------------------------------Register imports
from .serializers import RegisterSerializer , UserSerializer
from knox.models import AuthToken, User
#----------------------------------------------------------------------Login imports
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
#----------------------------------------------------------------------token imports
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
#----------------------------------------------------------------------swagger imports
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from drf_yasg import openapi
#https://drf-yasg.readthedocs.io/en/stable/custom_spec.html
#----------------------------------------------------------------------token
class UserObtainAuthTokeno(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(UserObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        #user = User.objects.get(iduser=1)
        #UserSerializer(user, context=self.get_serializer_context()).data
        return JsonResponse({'token': token.key, 'id': token.user_id})

class UserObtainAuthToken(APIView):
    def get(self, request, *args, **kwargs):
        
        try :
            token = request.GET.get('token')
            print (token)
            token = Token.objects.filter(key=token).first()
            print (token)
            print ("------------")
            if token :
                user = token.user
                return JsonResponse({'id': user})
        except:
            return Response({'error': 'No se ha encontrado'})


#----------------------------------------------------------------------Register

# Register API
class RegisterAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
#----------------------------------------------------------------------Login
class LoginAPI(KnoxLoginView):
    
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema( request_body=AuthTokenSerializer)

    def post(self, request, format=None):
        print(request)
        serializer = AuthTokenSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



#----------------------------------------------------------------------service

      #bytoken

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserPSerializer
    def get_object(self):
        try :
            user = self.request.user
            queryset = UserP.objects.filter(id=user.id).first()
            return queryset
        except:
            return Response({'error': 'No se ha encontrado'})


      #anotherservices

class searchbyName(generics.GenericAPIView):
    queryset =''
    @swagger_auto_schema(responses={200: UserPSerializer(many=True)},)
    def get(self,request,args):
        '''-description: search by Name '''
        queryset = UserP.objects.filter(username__icontains=args)
        data = UserPSerializer(queryset, many=True).data
        return Response(data)

class searchEmail(generics.GenericAPIView):
    queryset =''
    @swagger_auto_schema(responses={200: UserSerializer(many=True)})
    def get(self,request,args):
        '''search by Email'''
        queryset = UserP.objects.filter(email__istartswith=args)
        data = UserSerializer(queryset, many=True).data
        return Response(data)

class searchStoryGroup(generics.GenericAPIView):
    queryset =''
    
    @swagger_auto_schema(responses={200: StorySerializer(many=True)})
    def get(self, request, pk, *args, **kwargs):
        '''story search by group id '''
        queryset = Story.objects.filter(idgroup=pk)
        data = StorySerializer(queryset, many=True).data
        return Response(data)

class searchStoryUser(generics.GenericAPIView):
    queryset =''
    @swagger_auto_schema(responses={200: StorySerializer(many=True)})
    def get(self, request, pk, *args, **kwargs):
        '''story search by user id '''
        queryset = Story.objects.filter(iduser=pk)
        data = StorySerializer(queryset, many=True).data
        return Response(data)

class searchGroups(generics.GenericAPIView):
    queryset =''
    @swagger_auto_schema(responses={200: UsergroupSerializer(many=True)})
    def get(self,request,pk):
        '''search for groups by user id'''
        queryset = Usergroup.objects.filter(iduser=pk)
        data = UsergroupSerializer(queryset, many=True).data
        return Response(data)

class searchMembers(generics.GenericAPIView):
    queryset =''
    @swagger_auto_schema(responses={200: UsergroupSerializer(many=True)})
    def get(self,request,pk):
        '''search for members by group id'''
        queryset = Usergroup.objects.filter(idgroup=pk)
        data = UsergroupSerializer(queryset, many=True).data
        return Response(data)
#----------------------------------------------------------------------mailer
from django.core.mail import send_mail
from django.conf import settings

class mailer(generics.GenericAPIView):
    queryset =''
    #@swagger_auto_schema(responses={200: UsergroupSerializer(many=True)})
    def post(self,request):
        #if request.method == "POST":
        #s="test laclolala final server"
        #m="test service api hci final server, ya salio :D"
        #e="verajulio823@gmail.com"
        subject= request.POST["subject"]
        message= request.POST["message"] + " " + request.POST["email"]
        email_from= settings.EMAIL_HOST_USER
        recipient_list= request.POST["email"]
        send_mail(subject,message,email_from,[recipient_list], fail_silently=False)

        return Response("gracias.html")
        #return Response(request, "contacto.html")

## notificaciones realtime
#----------------------------------------------------------------------password reset imports
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
#----------------------------------------------------------------------password reset
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "resetAccount/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':settings.DOMAIN,
					'site_name': 'Diverticuentos',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("./password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="resetAccount/password_reset.html", context={"password_reset_form":password_reset_form})
#----------------------------------------------------------------------generate
class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.order_by('pk')
    serializer_class = AnswerSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.order_by('pk')
    serializer_class = CommentSerializer


class DictionaryViewSet(ModelViewSet):
    queryset = Dictionary.objects.order_by('pk')
    serializer_class = DictionarySerializer


class ExamplesdictionayViewSet(ModelViewSet):
    queryset = Examplesdictionay.objects.order_by('pk')
    serializer_class = ExamplesdictionaySerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.order_by('pk')
    serializer_class = GroupSerializer


class HistoryViewSet(ModelViewSet):
    queryset = History.objects.order_by('pk')
    serializer_class = HistorySerializer


class PreferenceViewSet(ModelViewSet):
    queryset = Preference.objects.order_by('pk')
    serializer_class = PreferenceSerializer


class ReadinglistViewSet(ModelViewSet):
    queryset = Readinglist.objects.order_by('pk')
    serializer_class = ReadinglistSerializer


class StoryViewSet(ModelViewSet):
    queryset = Story.objects.order_by('pk')
    serializer_class = StorySerializer


class SuggestionViewSet(ModelViewSet):
    queryset = Suggestion.objects.order_by('pk')
    serializer_class = SuggestionSerializer


class UserPViewSet(ModelViewSet):
    queryset = UserP.objects.order_by('pk')
    serializer_class = UserPSerializer


class UsergroupViewSet(ModelViewSet):
    queryset = Usergroup.objects.order_by('pk')
    serializer_class = UsergroupSerializer
