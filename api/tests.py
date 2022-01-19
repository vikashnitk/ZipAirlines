from rest_framework.test import APITestCase
from api.models import Airplane
from api.views import result
import json

# Create your tests here.
class AirlineAPITestCase(APITestCase):

	def test_get_method(self):
		Airplane.objects.create(id=11, passenger=110)
		url='http://127.0.0.1:8000/'
		response=self.client.get(url)
		self.assertEqual(response.status_code,200)
		qs=Airplane.objects.filter(id=11)
		self.assertEqual(qs.count(),1)

	def test_post_method_success_upto_ten(self):
		url='http://127.0.0.1:8000/'
		data={
		'id': 12,
		'passenger': 122
		}
		response=self.client.post(url,data,format='json')
		self.assertEqual(response.status_code,201)

	def test_post_method_success_morethan_ten(self):
		url='http://127.0.0.1:8000/'
		data=[{'id': 1, 'passenger':200},{'id':2, 'passenger':100},{'id':3, 'passenger':100},{'id':4, 'passenger':100},
		      {'id': 5, 'passenger':200},{'id':6, 'passenger':100},{'id':7, 'passenger':100},{'id':8, 'passenger':100},
		      {'id': 9, 'passenger':200},{'id':10, 'passenger':100},{'id':11, 'passenger':100}]
		for i in range(len(data)):
			response=self.client.post(url,data[i],format='json')
		responseData = '{"Message": "Cannot insert more than 10 airplanes data"}'
		self.assertEqual(response.content, str.encode(responseData))

	def test_post_method_fail(self):
		url='http://127.0.0.1:8000/'
		data={
		'id': 12,
		}
		response=self.client.post(url,data,format='json')
		self.assertEqual(response.status_code,400)

	def test_results_lessthan_ten(self):
		Airplane.objects.create(id=11, passenger=110)
		url='http://127.0.0.1:8000/results'
		response=self.client.get(url)
		self.assertEqual(response.status_code,200)

	def test_results_total_ten(self):
		Airplane.objects.bulk_create([Airplane(id=1, passenger=100), Airplane(id=2, passenger=150), 
			Airplane(id=3, passenger=200), Airplane(id=4, passenger=250),
			Airplane(id=5, passenger=300), Airplane(id=6, passenger=350),
			Airplane(id=7, passenger=400), Airplane(id=8, passenger=450),
			Airplane(id=9, passenger=500), Airplane(id=10, passenger=550)] )
		url='http://127.0.0.1:8000/results'
		response=self.client.get(url, format='json')
		responseData = '{"Total fuel consumption per minute in Liter": 19.37, "Maximum minutes able to fly": 1135.78}'
		self.assertEqual(response.content, str.encode(responseData))


		
		