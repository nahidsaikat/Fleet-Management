from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Vehicle
from .serializers import VehicleSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_vehicle(serial="", status=""):
        if serial != "" and status != "":
            Vehicle.objects.create(serial=serial, status=status)

    def setUp(self):
        # add test data
        self.create_vehicle("1230", "available")
        self.create_vehicle("1231", "available")
        self.create_vehicle("1232", "available")
        self.create_vehicle("1233", "available")


class GetAllVehicleTest(BaseViewTest):

    def test_get_all_vehicle(self):
        """
        This test ensures that all vehicle added in the setUp method
        exist when we make a GET request to the vehicle/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("core:vehicle")
        )
        # fetch the data from db
        expected = Vehicle.objects.all()
        serialized = VehicleSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
