from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import datetime


class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.userProfileUrl = reverse("userprofile:index")

        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@example.com', password='test-password'
        )

    def test_userprofile_logged_out_GET(self):
        response = self.client.get(self.userProfileUrl)
        self.assertEqual(response.status_code, 302)

    def test_userprofile_logged_in_GET(self):
        self.client.login(username='test', password='test-password')
        response = self.client.get(self.userProfileUrl)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')

    def test_userprofile_logged_out_POST(self):
        response = self.client.post(self.userProfileUrl, {
            "first_name": "fn",
            "last_name": "ln",
            "location": "loc"
        })
        self.assertEqual(response.status_code, 302)

    def test_userprofile_logged_in_POST(self):
        self.client.login(username='test', password='test-password')
        birth_date = datetime.date(2000, 1, 1)

        response = self.client.post(self.userProfileUrl, {
            "first_name": "fn",
            "last_name": "ln",
            "location": "loc",
            "birth_date": birth_date
        })

        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username="test")
        self.assertEqual(user.first_name, "fn")
        self.assertEqual(user.last_name, "ln")
        self.assertEqual(user.profile.location, "loc")
        self.assertEqual(user.profile.birth_date, birth_date)
        self.assertTemplateUsed(response, 'registration/profile.html')
