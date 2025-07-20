from django.contrib import admin
from .models import Course, CourseFile, Category

class CourseFileInline(admin.TabularInline):
    model = CourseFile
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'upload_date')
    inlines = [CourseFileInline]

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)