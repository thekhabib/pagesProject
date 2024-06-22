from django.test import SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_example_page_status_code(self):
        response = self.client.get('/example/')
        self.assertEqual(response.status_code, 200)

    def test_faq_page_status_code(self):
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)