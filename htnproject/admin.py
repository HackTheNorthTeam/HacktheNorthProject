from django.contrib import admin
from .models import User, School, Course
from django.forms import ModelForm, PasswordInput

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass