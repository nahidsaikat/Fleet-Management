from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import RequisitionLog, Requisition
from .serializers import RequisitionLogSerializer
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
    def create_requisition(vehicle=None, from_date="", from_time="", to_date="", to_time="", status="", requisition_by=None):
        if vehicle != "" and from_date != "":
           return  Requisition.objects.create(vehicle=vehicle, from_date=from_date, from_time=from_time, to_date=to_date, to_time=to_time, status=status, requisition_by=requisition_by)

    @staticmethod
    def create_log(requisition=None, from_status="", to_status="", date_time=None, user=None):
        if requisition and from_status and to_status and date_time and user:
            return RequisitionLog.objects.create(requisition=requisition, from_status=from_status, to_status=to_status, date_time=date_time, user=user)

    def setUp(self):
        # add test data
        user = User.objects.create(username='nahid', password='123456789', email='nahidsaikatft40@gmail.com')
        fleet = self.create_fleet("like glue")
        vehicle = self.create_vehicle(fleet, "1230", "available", user)
        requisition = self.create_requisition(vehicle, "2018-07-27", "14:00:00", "2018-07-27", "16:00:00", "pending", user)

        self.create_log(requisition, 'pending', 'approved', '2018-07-27 14:00:00', user)

class GetAllVehicleTest(BaseViewTest):

    def test_get_all_vehicle(self):
        """
        This test ensures that all vehicle added in the setUp method
        exist when we make a GET request to the vehicle/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("core:requisition_log")
        )
        # fetch the data from db
        expected = RequisitionLog.objects.all()
        serialized = RequisitionLogSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
