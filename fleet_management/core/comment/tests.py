from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Comment
from .serializers import CommentSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_vehicle(table_name=None, table_id="", comments="", user=None):
        if table_name != "" and table_id != "" and comments != "" and user:
            Comment.objects.create(table_name=table_name, table_id=table_id, comments=comments, user=user)

    def setUp(self):
        # add test data
        user = User.objects.first()

        self.create_vehicle("core_fleet", "1", "available", user)
        self.create_vehicle("core_fleet", "2", "available", user)
        self.create_vehicle("core_fleet", "3", "available", user)
        self.create_vehicle("core_fleet", "4", "available", user)


class GetAllVehicleTest(BaseViewTest):

    def test_get_all_vehicle(self):
        """
        This test ensures that all vehicle added in the setUp method
        exist when we make a GET request to the vehicle/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("core:comment")
        )
        # fetch the data from db
        expected = Comment.objects.all()
        serialized = CommentSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
