from django.test import TestCase, Client
from main.models import Item
from django.contrib.auth.models import User 
from datetime import datetime

# Get the current datetime and format it as a string
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='your_username',
            password='your_password'
        )
        self.client.login(username='your_username', password='your_password')
        self.client.cookies['last_login'] = current_datetime
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='your_username',
            password='your_password'
        )
        self.client.login(username='your_username', password='your_password')
        self.client.cookies['last_login'] = current_datetime
        response = self.client.get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_html_details(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='your_username',
            password='your_password'
        )
        self.client.login(username='your_username', password='your_password')
        self.client.cookies['last_login'] = current_datetime
        response = self.client.get('')
        self.assertContains(response, 'bp-mart')
        self.assertContains(response, 'PBP D')

    def setUp(self):  # Test initiating an object Item model
        # Create a user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )

        Item.objects.create(user=self.user,
                            name="Doritos",
                            amount="1",
                            description="Nacho Cheese flavoured tortilla chips",
                            price=13000,
                            purchased_from="Indogrosir")
        Item.objects.create(user=self.user,
                            name="Kejucake",
                            amount="3",
                            description="A soft cake with cream cheese",
                            price=5000,
                            purchased_from="Agen")
        
    def test_items_can_created(self): # Test if the attribute after initiation is correct
        doritos = Item.objects.get(name="Doritos")
        kejucake = Item.objects.get(name="Kejucake")
        self.assertEqual(doritos.user, self.user)
        self.assertEqual(kejucake.user, self.user)
        self.assertEqual(doritos.name, "Doritos")
        self.assertEqual(kejucake.name, "Kejucake")
        self.assertEqual(doritos.amount, 1)
        self.assertEqual(kejucake.amount, 3)
        self.assertEqual(doritos.description, "Nacho Cheese flavoured tortilla chips")
        self.assertEqual(kejucake.description, "A soft cake with cream cheese")
        self.assertEqual(doritos.price, 13000)
        self.assertEqual(kejucake.price, 5000)