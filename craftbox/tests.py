from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django.conf import settings

from .models import Link


# Create your tests here.
class LinkTests(TestCase):

    def setUp(self):
        c = Client()
        c.login(username="testuser", password="Secrets")
        self.link = Link.objects.create(
            link_name='Chocolate Chip Cookies',
            link_path='recipe.com',
            image='image.com',
            notes='yummy',
            user_id=get_user_model().objects.create(
                username="testuser",
                first_name="test",
                last_name="user",
                email="test@email.com",
                password="Secrets"
            )
        )
        # TODO: Test tags and if user_id matches 'logged in' user.

    def test_link_listing(self):
        self.assertEqual(f'{self.link.link_name}', 'Chocolate Chip Cookies')
        self.assertEqual(f'{self.link.link_path}', 'recipe.com')
        self.assertEqual(f'{self.link.image}', 'image.com')
        self.assertEqual(f'{self.link.notes}', 'yummy')

    def test_link_list_view(self):
        response = self.client.get(reverse('link_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chocolate Chip Cookies')
        self.assertTemplateUsed(response, 'links/craftbox.html')

    def test_link_detail_view(self):
        response = self.client.get(self.link.get_absolute_url())
        no_response = self.client.get('/link/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Chocolate Chip Cookies')
        self.assertTemplateUsed(response, 'link/link_detail.html')
