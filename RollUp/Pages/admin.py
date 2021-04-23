from django.contrib import admin
from .models import Classes, Participants
# Register your models here.

# admin.site.register(Classes)
# admin.site.register(Participants)

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('id','type','date','time','size','num_signed_up','instructor','gi')
    # list_filter = ('type')

@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('participant_id','email','name')
