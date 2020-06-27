from django.test import TestCase
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test-model-user", last_name="test-model-user")

    def test_user_is_create_with_profile_values(self):
        """Test create user"""
        user = User.objects.get(username="test-model-user")
        self.assertNotEqual(user.profile.id, None)

    def test_profile_is_updated(self):
        """Test update user profile related one-to-one model"""
        # do test update
        user = User.objects.get(username="test-model-user")
        user.profile.location = "Test location"
        user.save()

        # test saved data
        userTest = User.objects.get(username="test-model-user")
        self.assertEqual(userTest.profile.location, "Test location")
