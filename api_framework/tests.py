from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from clothing.models import ClothingModel,TypeModel
# Create your tests here.
class ClothingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.type=TypeModel.objects.create(name='T-shirt')
        self.clothing=ClothingModel.objects.create(
                                                   name='Cool-T-shirt',
                                                   manufacturer='Nike',
                                                   price=10,
                                                   type=self.type
                                                   )
        self.list_url=reverse('api_clothing_list')
        self.detail_url=reverse('api_clothing_detail',args=[self.clothing.pk])
    def test_list_clothes(self):
        response=self.client.get(self.list_url)
        self.assertEqual(response.status_code,200)
        self.assertGreaterEqual(len(response.json()),1)
    def test_create_clothing(self):
        data={
            'name':'New T-shirt',
            'manufacturer':'ZARS',
            'price':10,
            'type':self.type.id
        }
        response=self.client.post(self.list_url,data=data,format='json')
        self.assertEqual(response.status_code,201)
        self.assertEqual(ClothingModel.objects.count(),2)
    
    def test_delete_clothing(self):
        response=self.client.delete(self.detail_url)
        self.assertEqual(response.status_code,204)
        self.assertFalse(ClothingModel.objects.filter(pk=self.clothing.pk).exists())
    
    def test_retrieve_clothing_item(self):
        url = reverse('api_clothing_detail', kwargs={'pk': self.clothing.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], self.clothing.pk)
        self.assertEqual(response.json()['name'], self.clothing.name)