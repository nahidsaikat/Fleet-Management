from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import VehicleLog
from .serializers import VehicleLogSerializer
from core.vehicle.models import Vehicle
from core.fleet.models import Fleet


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_fleet(name=""):
        if name != "":
            return Fleet.objects.create(name=name)

    @staticmethod
    def create_vehicle(fleet=None, serial="", status="", driver=None):
        if fleet and serial != "" and status != "" and driver:
            return Vehicle.objects.create(fleet=fleet, serial=serial, status=status, driver=driver)

    @staticmethod
    def create_log(vehicle=None, driver=None, from_status="", to_status="", remarks=""):
        if vehicle and driver and from_status and to_status and remarks:
            return VehicleLog.objects.create(vehicle=vehicle,driver=driver, from_status=from_status, to_status=to_status, remarks=remarks)

    def setUp(self):
        # add test data
        user = User.objects.create(username='nahid', password='123456789', email='nahidsaikatft40@gmail.com')
        fleet = self.create_fleet("like glue")
        vehicle = self.create_vehicle(fleet, "1230", "available", user)

        self.create_log(vehicle, user, 'pending', 'approved', 'something that is remarks')

class GetAllVehicleTest(BaseViewTest):

    def test_get_all_vehicle(self):
        """
        This test ensures that all vehicle added in the setUp method
        exist when we make a GET request to the vehicle/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("core:vehicle_log")
        )
        # fetch the data from db
        expected = VehicleLog.objects.all()
        serialized = VehicleLogSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
