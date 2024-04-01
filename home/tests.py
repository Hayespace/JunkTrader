from django.test import TestCase
from django.urls import reverse

class HomePageTestCase(TestCase):
    
    def test_main_page_response(self):
        # Send a GET request to the main page
        response = self.client.get(reverse('home:index'))
        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)


