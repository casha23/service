import pytest

from model_bakery import baker
from django.contrib.auth import get_user_model

from request.models import Invoice, Request

User = get_user_model()


@pytest.fixture(scope='session')
def user(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        user_data = {
            'phone_number': '+380000000001',
            'email': '',
            'password': '12345'
        }
        user = User._default_manager.create_user(**user_data)
        return user


@pytest.fixture(scope='session')
def master(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        user_data = {
            'phone_number': '+380000000001',
            'email': '',
            'password': '12345'
        }
        user = User._default_manager.create_user(**user_data)
        user.is_master = True
        user.save()
        return user


@pytest.fixture()
def model_request(user):
    return baker.make(Request, phone_model='Iphone 14', user=user)
