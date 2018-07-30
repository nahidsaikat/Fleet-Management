from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Notification
from .serializers import NotificationSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_vehicle(message="", from_employee_id=None, to_employee_id=None, table_name="", table_id=None, mark_as_read=False):
        if from_employee_id and to_employee_id and table_name != "" and table_id != "" and message != "" and mark_as_read:
            Notification.objects.create(from_employee_id=from_employee_id, to_employee_id=to_employee_id, table_name=table_name, table_id=table_id, message=message, mark_as_read=mark_as_read)

    def setUp(self):
        # add test data
        users = User.objects.add()
        first_user = users[0]
        second_user = users[1]

        self.create_vehicle("core_fleet one", first_user.id, second_user.ic, 'core_requisition', 1, False)
        self.create_vehicle("core_fleet two", first_user.id, second_user.ic, 'core_requisition', 2, False)


class GetAllVehicleTest(BaseViewTest):

    def test_get_all_vehicle(self):
        """
        This test ensures that all vehicle added in the setUp method
        exist when we make a GET request to the vehicle/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("core:notification")
        )
        # fetch the data from db
        expected = Notification.objects.all()
        serialized = NotificationSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
