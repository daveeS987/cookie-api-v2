from django.test import TestCase

# for some reason, we have to use get_user_model and not settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from .models import Cookie_Stand


class Cookie_StandTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(email="test@gmail.com", password="pass")
        testuser1.save()
        test_cookie_stand = Cookie_Stand.objects.create(
            owner=testuser1,
            location="Houston",
            minimum_customers_per_hour=0,
            maximum_customers_per_hour=10,
            average_cookies_per_sale=5,
        )
        test_cookie_stand.save()

    def test_cookie_stand_content(self):
        cookie_stand = Cookie_Stand.objects.get(id=1)
        self.assertEqual(cookie_stand.owner, "test@gmail.com")
        self.assertEqual(cookie_stand.location, "Houston")
        self.assertEqual(cookie_stand.minimum_customers_per_hour, 0)
        self.assertEqual(cookie_stand.maximum_customers_per_hour, 10)
        self.assertEqual(cookie_stand.average_cookies_per_sale, 5)
