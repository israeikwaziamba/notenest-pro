from django.test import TestCase
from .models import Course, Category

class CourseModelTest(TestCase):
    def test_course_creation(self):
        cat = Category.objects.create(name="Mathématiques")
        course = Course.objects.create(title="Algebre", description="Cours de base", category=cat)
        self.assertEqual(course.title, "Algebre")
        self.assertEqual(course.category.name, "Mathématiques")