from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post
# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret',
        )

        self.post = Post.objects.create(
            title = 'A good title', 
            author = self.user,
            text = 'Nice body text'
        )
    
    def test_string_representation(self):
        post = Post(title = 'A sample title')
        self.assertEqual(str(post), post.title) # model string return 

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", 'A good title')
        self.assertEqual(f"{self.post.author}", 'testuser')
        self.assertEqual(f"{self.post.text}", 'Nice body text')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body text')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/1000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), { # use post because you need to create a new variables
            'title': 'New title', 
            'user': self.user,
            'text': 'New text'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_edit_view(self):
        response = self.client.post(reverse('post_edit', args='1'), { # use post since variables still needed
            'title': 'Updated title', 
            'text': 'Updated text',
        })
        self.assertEqual(response.status_code, 302) # use 302 for check redirect status

    def test_post_delete_view(self):
        response = self.client.get(reverse(
            'post_delete', args='1')) # use get since there is no variable needed to check, just the page
        self.assertEqual(response.status_code, 200)