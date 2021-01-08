from rest_framework.test import APITestCase

from django.urls import reverse
from faker import Faker

class TestSetup(APITestCase):

    def setUp(self):
        self.faker = Faker()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_data = {
            'email': self.faker.email(),
            'username':"smart",
            'password': self.faker.password()
        }

        # import pdb
        # pdb.set_trace()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
