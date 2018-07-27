from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Vehicle
from .serializers import VehicleSerializer
from core.fleet.models import Fleet


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_vehicle(fleet=None, serial="", status="", user=None):
        if fleet and serial != "" and status != "" and user:
            Vehicle.objects.create(fleet=fleet, serial=serial, status=status, driver=user)

    def setUp(self):
        # add test data
        user = User.objects.create(username='saikat', password='0123456789', email='nahidsaikat@gmail.com')
        fleet = Fleet.objects.first()

        self.create_vehicle(fleet, "1230", "available", user)
        self.create_vehicle(fleet, "1231", "available", user)
        self.create_vehicle(fleet, "1232", "available", user)
        self.create_vehicle(fleet, "1233", "available", user)


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
