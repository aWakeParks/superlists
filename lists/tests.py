from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageViewTest(TestCase):

    def test_home_page_uses_home_template(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_handle_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'a new item'
        response = home_page(request)
        self.assertIn('a new item', response.content.decode())

        expected_html = render_to_string('home.html',
                                         {'new_item_text': 'a new item'})
        self.assertEqual(response.content.decode(), expected_html)
