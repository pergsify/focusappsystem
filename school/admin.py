from django.contrib import admin

from .models import(Teacher, SchoolYear)

class TeacherAdmin(admin.ModelAdmin):
	list_display = ['first_Name', 'last_Name']

class SchoolYearAdmin(admin.ModelAdmin):
	list_display = ['start_Year']

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)