from django.test import TestCase
from ..models import Post


class PostTest(TestCase):
    """
    Testing model instance creating and getting
    """

    def setUp(self):
        Post.objects.create(title='test_title', url='www.google.com')


    def test_post_get(self):
        test_title = Post.objects.get(title='test_title')
        self.assertEqual(test_title.title, 'test_title')
