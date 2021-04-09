from django.contrib import admin
from .models import Classes, Participants
# Register your models here.

# admin.site.register(Classes)
# admin.site.register(Participants)

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('id','type','date','size','full','instructor','gi')
    list_filter = ('type','full') 

@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('participant_id','class_id','email','name')
