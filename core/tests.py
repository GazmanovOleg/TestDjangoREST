from django.test import TestCase
from rest_framework.test import APITestCase
import json
from .models import File

class APITests(APITestCase):
    
    BASE_URL = 'http://127.0.0.1:8000/api/v1/file/'

    def test_create_file(self):
        response = self.client.post(self.BASE_URL)
        #response = json.dumps(response)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['id'])
    
    def test_get_file_info(self):
        file_id = str(self.client.post(self.BASE_URL).data['id'])
        BASE_URL_ID = f"{self.BASE_URL}{file_id}/" 
        response = self.client.get(BASE_URL_ID)
        self.assertEqual(response.status_code,200)
        data =json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['id'], file_id)

        response = self.client.delete(BASE_URL_ID)
        self.assertEqual(response.status_code, 200)

        #Проверить отсутствие в списке всех id
    
    def test_delete_file(self):
        file_id = str(self.client.post(self.BASE_URL).data['id'])
        BASE_URL_ID = f"{self.BASE_URL}{file_id}/" 
        response = self.client.get(BASE_URL_ID)
        response = self.client.delete(BASE_URL_ID)
        self.assertEqual(response.status_code, 200)

         #Проверить отсутствие в списке всех id
    
    def test_change_resolution(self):
        pass

    
   


