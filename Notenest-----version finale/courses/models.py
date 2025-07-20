from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class CourseFile(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='courses/')

    def _str_(self):
        return f"Fichier de {self.course.title}"