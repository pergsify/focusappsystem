from django.contrib import admin

from .models import(Teacher, SchoolYear, Faculty)

class TeacherAdmin(admin.ModelAdmin):
	list_display = ['first_Name', 'last_Name']

class SchoolYearAdmin(admin.ModelAdmin):
	list_display = ['start_Year']

class FacultyAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Faculty, FacultyAdmin)