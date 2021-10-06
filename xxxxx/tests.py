from django.test import TestCase

# for some reason, we have to use get_user_model and not settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from .models import Xxxxx


class XxxxxTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(email="test@gmail.com", password="pass")
        testuser1.save()
        test_xxxxx = Xxxxx.objects.create(
            author=testuser1, title="Green Eggs and Ham", body="I do not like green eggs and ham, Sam I  am."
        )
        test_xxxxx.save()

    def test_blog_content(self):
        xxxxx = Xxxxx.objects.get(id=1)
        self.assertEqual(str(xxxxx.author), "test@gmail.com")
        self.assertEqual(str(xxxxx.title), "Green Eggs and Ham")
        self.assertEqual(str(xxxxx.body), "I do not like green eggs and ham, Sam I  am.")
