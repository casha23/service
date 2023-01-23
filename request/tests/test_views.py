import pytest

from request.models import Request
from rest_framework import status


@pytest.mark.django_db
def test_user_create_request(client, user):
    client.force_login(user)

    data = {
        "phone_model": "Iphone 14",
        "problem_description": "Broken screen"
    }
    response = client.post('/request/requests/', data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_user_get_request(client, user, model_request):
    client.force_login(user)
    response = client.get(f'/request/requests/{model_request.pk}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['phone_model'] == 'Iphone 14'


@pytest.mark.django_db
def test_user_put_request(client, user, model_request):
    client.force_login(user)
    response = client.get(f'/request/requests/{model_request.pk}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['phone_model'] == 'Iphone 14'

    data = {
        "phone_model": "Iphone 13",
        "problem_description": "",
    }
    response = client.put(f'/request/requests/{model_request.pk}/', data, content_type='application/json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['phone_model'] == 'Iphone 13'


@pytest.mark.django_db
def test_user_patch_request(client, user, model_request):
    client.force_login(user)
    response = client.get(f'/request/requests/{model_request.pk}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['phone_model'] == 'Iphone 14'

    data = {
        "phone_model": "Iphone 13"
    }
    response = client.patch(f'/request/requests/{model_request.pk}/', data, content_type='application/json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['phone_model'] == 'Iphone 13'


@pytest.mark.django_db
def test_user_delete_request(client, user, model_request):
    client.force_login(user)
    response = client.delete(f'/request/requests/{model_request.pk}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_user_delete_request_with_status_in_work(client, user, model_request):
    client.force_login(user)
    model_request.status = Request.IN_WORK
    model_request.save()
    response = client.delete(f'/request/requests/{model_request.pk}/')
    assert response.status_code == status.HTTP_403_FORBIDDEN
