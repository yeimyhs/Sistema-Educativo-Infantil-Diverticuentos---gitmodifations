from rest_framework.serializers import ModelSerializer
from DivertiCuentos.models import Answer, Comment, Dictionary, Examplesdictionay, Group, History, Preference, Readinglist, Story, Suggestion, UserP, Usergroup

from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 
        'username', 
        'email' ,
        )

from datetime import datetime
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 
        'username',  
        'email', 
        'password',
        #'last_name'
        )

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], 
            validated_data['email'], 
            validated_data['password'],
            )
        UserPf= UserP()                              
        UserPf.iduser = user
        UserPf.datecreationuser=datetime.now()
        UserPf.datecreationuser=datetime.now()
        print(UserPf.datecreationuser)
        UserPf.save()
        return user


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class DictionarySerializer(ModelSerializer):

    class Meta:
        model = Dictionary
        fields = '__all__'


class ExamplesdictionaySerializer(ModelSerializer):

    class Meta:
        model = Examplesdictionay
        fields = '__all__'


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class HistorySerializer(ModelSerializer):

    class Meta:
        model = History
        fields = '__all__'


class PreferenceSerializer(ModelSerializer):

    class Meta:
        model = Preference
        fields = '__all__'


class ReadinglistSerializer(ModelSerializer):

    class Meta:
        model = Readinglist
        fields = '__all__'


class StorySerializer(ModelSerializer):

    class Meta:
        model = Story
        fields = '__all__'


class SuggestionSerializer(ModelSerializer):

    class Meta:
        model = Suggestion
        fields = '__all__'


class UserPSerializer(ModelSerializer):

    class Meta:
        model = UserP
        fields = '__all__'


class UsergroupSerializer(ModelSerializer):

    class Meta:
        model = Usergroup
        fields = '__all__'
