from django.urls import reverse
from django.test import TestCase


class ContactsViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_contacts_uses_correct_template(self):
        response = self.client.get(reverse('contacts:index'))
        self.assertTemplateUsed(response, 'contacts.html')
