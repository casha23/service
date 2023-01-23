import pytest

from rest_framework import status


@pytest.mark.django_db
def test_registration(client):
    data = {
        "username": "+380000000000",
        "password1": "test12345",
        "password2": "test12345"
    }
    response = client.post('/rest-auth/registration/', data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_registration_with_bad_number(client):
    data = {
        "username": "+3800000000",
        "password1": "test12345",
        "password2": "test12345"
    }
    response = client.post('/rest-auth/registration/', data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
