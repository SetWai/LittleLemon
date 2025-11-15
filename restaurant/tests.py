from django.test import TestCase
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status
from rest_framework.test import APIClient  # Import the APIClient
from django.contrib.auth.models import User  # Import User

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances
        MenuItem.objects.create(title="Salad", price=20, inventory=10)
        
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Set up the APIClient
        self.client = APIClient()

    def test_getall(self):
        url = '/api/menu/' # This URL is from LittleLemon/urls.py and restaurant/urls.py
        
        # --- THIS IS THE FIX ---
        # Authenticate the client as the test user
        self.client.force_authenticate(user=self.user)
        # --- END OF FIX ---
        
        # Now this GET request is made by an authenticated user
        response = self.client.get(url)
        
        # Check for 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Continue with your serialization check
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.json(), serializer.data)