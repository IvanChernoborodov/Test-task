import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post
from ..serializers import PostSerializer


client = Client()


class GetAllPostsTest(TestCase):
    """
    Test module for GET all posts API
    """


    def setUp(self):
        self.one = Post.objects.create(
            title='Test1', url='www.google.com')
        self.two = Post.objects.create(
            title='Test2', url='www.google.com')
        self.three = Post.objects.create(
            title='Test3', url='www.google.com')
        self.four = Post.objects.create(
            title='Test4', url='www.google.com')
        self.five = Post.objects.create(
            title='Test5', url='www.google.com')


    def test_get_all_posts(self):
        response = client.get(reverse('posts-list'))
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data.get('results'), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_single_post(self):
        response = client.get(reverse('posts-detail', kwargs={'pk':self.four.pk}))
        post = Post.objects.get(pk=self.four.pk)
        serializer = PostSerializer(post)
        self.assertEqual(response.data, serializer.data)


    def test_get_invalid_single_post(self):
        response = client.get(
            reverse('posts-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)