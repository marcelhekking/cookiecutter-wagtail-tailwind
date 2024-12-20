import pytest
from django.contrib.auth.models import User

# from tests.factories.users import UserFactory


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user("test123", "user@{{cookiecutter.project_slug}}.nl")
    assert user.pk
    assert user.email == "user@{{cookiecutter.project_slug}}.nl"
    assert not user.is_staff
    assert not user.is_superuser
