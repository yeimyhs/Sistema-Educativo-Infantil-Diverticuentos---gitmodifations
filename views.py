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
class UserObtainAuthToken(ObtainAuthToken):
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
    '''
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['Users'],
    )
    '''
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
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

      #anotherservices

class searchbyName(generics.GenericAPIView):
    queryset =''
    """search by Name"""
    @swagger_auto_schema(responses={200: UserSerializer(many=True)})
    def get(self,request,args):
        queryset = User.objects.filter(username__icontains=args)
        data = UserSerializer(queryset, many=True).data
        return Response(data)

class searchEmail(generics.GenericAPIView):
    queryset =''
    """search by Email"""
    @swagger_auto_schema(responses={200: UserSerializer(many=True)})
    def get(self,request,args):
        queryset = User.objects.filter(email__istartswith=args)
        data = UserSerializer(queryset, many=True).data
        return Response(data)

class searchStoryGroup(generics.GenericAPIView):
    queryset =''
    """story search by group id """
    @swagger_auto_schema(responses={200: StorySerializer(many=True)})
    def get(self, request, pk, *args, **kwargs):
        queryset = Story.objects.filter(idgroup=pk)
        data = StorySerializer(queryset, many=True).data
        return Response(data)

class searchStoryUser(generics.GenericAPIView):
    queryset =''
    """story search by user id """
    @swagger_auto_schema(responses={200: StorySerializer(many=True)})
    def get(self, request, pk, *args, **kwargs):
        queryset = Story.objects.filter(iduser=pk)
        data = StorySerializer(queryset, many=True).data
        return Response(data)

class searchGroups(generics.GenericAPIView):
    queryset =''
    """search for groups by user id"""
    @swagger_auto_schema(responses={200: UsergroupSerializer(many=True)})
    def get(self,request,pk):
        queryset = Usergroup.objects.filter(iduser=pk)
        data = UsergroupSerializer(queryset, many=True).data
        return Response(data)

class searchMembers(generics.GenericAPIView):
    queryset =''
    """search for members by group id"""
    @swagger_auto_schema(responses={200: UsergroupSerializer(many=True)})
    def get(self,request,pk):
        queryset = Usergroup.objects.filter(idgroup=pk)
        data = UsergroupSerializer(queryset, many=True).data
        return Response(data)
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
