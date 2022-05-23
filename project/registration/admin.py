from django.contrib import admin
from . models import *
# Register your models here.
class Registration(admin.ModelAdmin):
    list_display = ['FullName','StudentID','Gpa','Department','Status','StudentLevel']
    list_display_links =  ['FullName','StudentID','Gpa','Department']
    list_filter = ['Status','Department']
class Contact(admin.ModelAdmin):
    list_display = ['FullName','Email','Mobile']
    list_display_links = ['FullName','Email','Mobile']
    list_filter = ['FullName']
    
        
admin.site.register(AddStudent,Registration)
admin.site.register(ContactUs,Contact)
