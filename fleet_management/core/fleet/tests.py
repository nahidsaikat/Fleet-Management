from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Fleet
from .serializers import FleetSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_fleet(name=""):
        if name != "":
            Fleet.objects.create(name=name)

    def setUp(self):
        # add test data
        self.create_fleet("like glue")
        self.create_fleet("simple fleet")
        self.create_fleet("love is wicked")
        self.create_fleet("jam rock")


class GetAllFleetTest(BaseViewTest):

    def test_get_all_fleet(self):
        """
        This test ensures that all fleet added in the setUp method
        exist when we make a GET request to the fleet/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("core:fleet")
        )
        # fetch the data from db
        expected = Fleet.objects.all()
        serialized = FleetSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
