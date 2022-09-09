from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

# Create your tests here.


class HomepageTets(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "home page")

    def test_homepage_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "Hi, there I should  not be on this page")

    def test_homepageurl_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
