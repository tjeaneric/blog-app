from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title = 'A good title', 
            body = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
            author = self.user
        )


    def test_string_reprentation(self):
        post = Post(title = 'A good title')
        self.assertEqual(str(post), post.title)


    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')


    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')


    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',

        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete',args='1'))
        self.assertEqual(response.status_code, 302)


# class SignUpTests(TestCase):
#     def test_signup_status_code(self):
#         url = reverse('register')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
