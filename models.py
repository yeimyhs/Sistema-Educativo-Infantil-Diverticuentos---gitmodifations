from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import auth


class Answer(models.Model):
    idanswer = models.BigAutoField(db_column='idAnswer', primary_key=True)  # Field name made lowercase.
    comentanswer = models.CharField(db_column='comentAnswer', max_length=8192)  # Field name made lowercase.
    stateanswer = models.BigIntegerField(db_column='stateAnswer', blank=True, null=True)  # Field name made lowercase.
    datecreationanswer = models.DateTimeField(db_column='dateCreationAnswer')  # Field name made lowercase.
    idcomment = models.ForeignKey('Comment', models.DO_NOTHING, db_column='idComment')  # Field name made lowercase.
    iduser = models.BigIntegerField(db_column='idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Answer'


class Comment(models.Model):
    idcomment = models.BigAutoField(db_column='idComment', primary_key=True)  # Field name made lowercase.
    idstory = models.ForeignKey('Story', models.DO_NOTHING, db_column='idStory')  # Field name made lowercase.
    datecreationcomment = models.DateTimeField(db_column='dateCreationComment')  # Field name made lowercase.
    contentcomment = models.CharField(db_column='contentComment', max_length=8192)  # Field name made lowercase.
    statecomment = models.BigIntegerField(db_column='stateComment', blank=True, null=True)  # Field name made lowercase.
    iduser = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='idUser', blank=True, null=True)
    #models.ForeignKey('User', models.DO_NOTHING,db_column='idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comment'
        unique_together = (('idcomment', 'iduser'),)


class Dictionary(models.Model):
    worddictionary = models.CharField(db_column='wordDictionary', max_length=128)  # Field name made lowercase.
    audiodictionary = models.BinaryField(db_column='audioDictionary', blank=True, null=True)  # Field name made lowercase.
    iddictionary = models.BigAutoField(db_column='idDictionary', primary_key=True)  # Field name made lowercase.
    traslatedictionary = models.CharField(db_column='traslateDictionary', max_length=128)  # Field name made lowercase.
    pronunciationdictionary = models.CharField(db_column='pronunciationDictionary', max_length=128)  # Field name made lowercase.
    descriptiondictionary = models.CharField(db_column='descriptionDictionary', max_length=256)  # Field name made lowercase.
    idexamplesdictionary = models.ForeignKey('Examplesdictionay', models.DO_NOTHING, db_column='idExamplesDictionary', blank=True, null=True)  # Field name made lowercase.
    resourcedictionary = models.CharField(db_column='resourceDictionary', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dictionary'


class Examplesdictionay(models.Model):
    idexamplesdictionay = models.BigIntegerField(db_column='idExamplesDictionay', primary_key=True)  # Field name made lowercase.
    sentencesexamplesdictionay = models.TextField(db_column='sentencesExamplesDictionay')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ExamplesDictionay'


class Group(models.Model):
    idgroup = models.BigAutoField(db_column='idGroup', primary_key=True)  # Field name made lowercase.
    imagecovergroup = models.BinaryField(db_column='imageCoverGroup', blank=True, null=True)  # Field name made lowercase.
    namegroup = models.CharField(db_column='nameGroup', max_length=128)  # Field name made lowercase.
    descriptiongroup = models.CharField(db_column='descriptionGroup', max_length=256)  # Field name made lowercase.
    datecreationgroup = models.DateTimeField(db_column='dateCreationGroup')  # Field name made lowercase.
    stategroup = models.IntegerField(db_column='stateGroup', blank=True, null=True)  # Field name made lowercase.
    typegroup = models.IntegerField(db_column='typeGroup', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group'

    def __str__(self):
        return f'{self.namegroup}'


class History(models.Model):
    idhistory = models.BigAutoField(db_column='idHistory', primary_key=True)  # Field name made lowercase.
    datemodificationhistory = models.DateTimeField(db_column='dateModificationHistory')  # Field name made lowercase.
    contentstringhistory = models.TextField(db_column='contentStringHistory')  # Field name made lowercase.
    idstory = models.ForeignKey('Story', models.DO_NOTHING, db_column='idStory')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'History'


class Preference(models.Model):
    questionpreference = models.CharField(db_column='questionPreference', max_length=256)  # Field name made lowercase.
    answerpreference = models.CharField(db_column='answerPreference', max_length=128, blank=True, null=True)  # Field name made lowercase.
    idpreference = models.BigAutoField(db_column='idPreference', primary_key=True)  # Field name made lowercase.
    idstory = models.ForeignKey('Story', models.DO_NOTHING, db_column='idStory')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preference'


class Readinglist(models.Model):
    iduser = models.OneToOneField(User, models.DO_NOTHING, db_column='idUser', primary_key=True)
    #iduser = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  # Field name made lowercase.
    idstory = models.ForeignKey('Story', models.DO_NOTHING, db_column='idStory')  # Field name made lowercase.
    datecreationreadinglist = models.BigIntegerField(db_column='dateCreationReadingList')  # Field name made lowercase.
    namereadinglist = models.BigIntegerField(db_column='nameReadingList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReadingList'
        unique_together = (('iduser', 'idstory'),)


class Story(models.Model):
    idstory = models.BigAutoField(db_column='idStory', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
#    iduser = models.ForeignKey('User', models.DO_NOTHING,db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    idgroup = models.ForeignKey('Group', models.DO_NOTHING,db_column='idGroup', blank=True, null=True)  # Field name made lowercase.
    titlestory = models.CharField(db_column='titleStory', max_length=128)  # Field name made lowercase.
    descriptionstory = models.CharField(db_column='descriptionStory', max_length=2048)  # Field name made lowercase.
    imagecoverstory = models.BinaryField(db_column='imageCoverStory', blank=True, null=True)  # Field name made lowercase.
    likesstory = models.IntegerField(db_column='likesStory', blank=True, null=True)  # Field name made lowercase.
    contentstringstory = models.TextField(db_column='contentStringStory')  # Field name made lowercase.
    datecreationstory = models.DateTimeField(db_column='dateCreationStory')  # Field name made lowercase.
    statestory = models.IntegerField(db_column='stateStory', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Story'

    def __str__(self):
        return f'{self.titlestory}'


class Suggestion(models.Model):
    idsuggestion = models.BigAutoField(db_column='idSuggestion', primary_key=True)  # Field name made lowercase.
    suggestion = models.TextField(db_column='Suggestion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Suggestion'


class UserP(models.Model):
    id = models.OneToOneField(auth.models.User,related_name='user_profile', on_delete=models.CASCADE,db_column='idUser', primary_key=True)
    #iduser = models.BigAutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='emailUser', max_length=512)  # Field name made lowercase.
    password = models.CharField(db_column='passwordUser', max_length=64)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstnameUser', max_length=128)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastnameUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    imagecover = models.BinaryField(db_column='imageCoverUser', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='countryUser', max_length=512, blank=True, null=True)  # Field name made lowercase.
    phone = models.IntegerField(db_column='phoneUser', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='usernameUser', max_length=128)  # Field name made lowercase.
    adress = models.CharField(db_column='adressUser', max_length=512, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='cityUser', max_length=512, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='stateUser', blank=True, null=True, default = 1)  # Field name made lowercase.
    datecreation = models.DateTimeField(db_column='dateCreationUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'

    def __str__(self):
        return f'{self.firstname}'


class Usergroup(models.Model):
    iduser = models.OneToOneField(User, models.DO_NOTHING, db_column='idUser', primary_key=True)  # Field name made lowercase.
    idgroup = models.ForeignKey(Group, models.DO_NOTHING, db_column='idGroup')  # Field name made lowercase.
    staterequestusergroup = models.IntegerField(db_column='stateRequestUserGroup')  # Field name made lowercase.
    rolusergroup = models.IntegerField(db_column='rolUserGroup')  # Field name made lowercase.
    dateusergroup = models.DateTimeField(db_column='dateUserGroup', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserGroup'
        unique_together = (('iduser', 'idgroup'),)