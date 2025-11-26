import pytest
from django.contrib.auth.models import User
from rest_framework import status
from .models import Post
from rest_framework.test import APIClient

@pytest.fixture
def test_user():
    return User.objects.create_user(username='pytestuser', password='pytestpassword')

@pytest.fixture
def test_post(test_user):
    return Post.objects.create(
		    author=test_user, 
		    title='Pytest Test Ataması', 
		    content='Pytest Test Mazmunı'
    )


@pytest.mark.django_db
def test_list_posts(client, test_post):
    client = APIClient()
    response = client.get('/api/v1/posts/')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['title'] == 'Pytest Test Ataması'

@pytest.mark.django_db
def test_create_post_auth(client, test_user):
    client = APIClient()
    client.force_authenticate(user=test_user)

    data = {'title': 'Pytest Jańa post', 'content': 'Pytest Jańa mazmun'}
    response = client.post('/api/v1/posts/', data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.count() == 1 
    assert Post.objects.first().title == 'Pytest Jańa post'