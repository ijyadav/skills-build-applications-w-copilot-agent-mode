from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        user = User.objects.create(username='testuser')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30)
        self.assertEqual(str(activity), 'testuser - Run')

    def test_leaderboard_creation(self):
        user = User.objects.create(username='testuser')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'testuser - 100')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Yoga', difficulty='Easy')
        self.assertEqual(str(workout), 'Yoga')
