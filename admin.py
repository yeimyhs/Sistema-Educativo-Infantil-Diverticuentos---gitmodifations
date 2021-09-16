from django.contrib import admin

# Register your models here.
from .models import *
#admin.site.register(Usuario)
admin.site.register(UserP)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Dictionary)
admin.site.register(Examplesdictionay)
admin.site.register(Group)
admin.site.register(History)
admin.site.register(Preference)
admin.site.register(Readinglist)
admin.site.register(Story)
admin.site.register(Suggestion)
admin.site.register(Usergroup)

