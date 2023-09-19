from django.test import TestCase, Client
from main.models import Item

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_html_details(self):
        response = Client().get('/main/')
        self.assertContains(response, 'bp-mart')
        self.assertContains(response, 'Reza Apriono') 
        self.assertContains(response, 'PBP D')

    def setUp(self):  # Test pengecekan initiate suatu object model item
        Item.objects.create(name="Doritos",amount="1",
                            description=
                            "Nacho Cheese flavoured tortilla chips",
                            price=13000)
        Item.objects.create(name="Kejucake",amount="3",
                            description=
                            "A soft cake with cream cheese",
                            price=5000)
        
    def test_items_can_created(self): # Test apakah attribute setelah inisiasi benar
        doritos = Item.objects.get(name="Doritos")
        kejucake = Item.objects.get(name="Kejucake")
        self.assertEqual(doritos.name, "Doritos")
        self.assertEqual(kejucake.name, "Kejucake")
        self.assertEqual(doritos.amount, 1)
        self.assertEqual(kejucake.amount, 3)
        self.assertEqual(doritos.description, "Nacho Cheese flavoured tortilla chips")
        self.assertEqual(kejucake.description, "A soft cake with cream cheese")
        self.assertEqual(doritos.price, 13000)
        self.assertEqual(kejucake.price, 5000)