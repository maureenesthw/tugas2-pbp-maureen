from django.test import TestCase
from django.urls import reverse
from mywatchlist.views import show_json, show_xml, show_html

# Create your tests here.
class UnitTest(TestCase):
    def test_html(self):
        response = self.client.get(reverse("mywatchlist:show_html"))
        self.assertEquals(response.status_code, 200)

    def test_json(self):
        response= self.client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code, 200)

    def test_xml(self):
        response = self.client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code, 200)