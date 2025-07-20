from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Goal
from datetime import date

User = get_user_model()

class GoalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="isk", password="123")
        self.goal = Goal.objects.create(
            user=self.user,
            title="Réussir l'exam",
            deadline=date.today(),
            completed=False
        )

    def test_goal_str(self):
        self.assertEqual(str(self.goal), "Réussir l'exam")

    def test_goal_completion(self):
        self.assertFalse(self.goal.completed)