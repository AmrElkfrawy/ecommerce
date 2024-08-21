import pytest
from api.services import update_profile
from api.models import Profile


@pytest.mark.django_db
def test_update_profile(user):
    profile = Profile.objects.get(user=user)

    update_data = {
        "address": "Cairo",
        "phone": "01234567890",
        "preferred_currency": "USD",
    }

    updated_profile = update_profile(profile, update_data)

    assert updated_profile.address == "Cairo"
    assert updated_profile.phone == "01234567890"
    assert updated_profile.preferred_currency == "USD"