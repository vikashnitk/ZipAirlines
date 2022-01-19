import math
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from api.models import Airplane
from api.serializers import AirplaneSerializer

# Create your views here.
@api_view(['GET','POST'])
def airplanes(request):
	'''
        a function to GET and POST the data.
    '''
	if request.method == 'GET':
		airplanes = Airplane.objects.all()
		serializer = AirplaneSerializer(airplanes,many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = AirplaneSerializer(data=request.data)
		total_airplane = Airplane.objects.count()
		if serializer.is_valid():
			if total_airplane < 10:
				serializer.save()
				return Response(serializer.data,status=status.HTTP_201_CREATED)
			else:
				return Response({"Message": "Cannot insert more than 10 airplanes data"},status=status.HTTP_202_ACCEPTED)		
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def result(request):
	'''
        a function to print the required results.
    '''
	if request.method == 'GET':
		total_airplane = Airplane.objects.count()
		if total_airplane == 10:
			fuel_consm = Airplane.objects.values_list('id', 'passenger')
			total_fuel_consm = round(sum(math.log(t[0]*0.8) + (t[1]*0.002) for t in fuel_consm), 2)		
			min_fly = Airplane.objects.values_list('id', 'passenger')
			total = sum(t[0] * t[1] for t in min_fly )			
			max_min_fly = round(total/total_fuel_consm, 2) 			

			responseData = {
							'Total fuel consumption per minute in Liter': total_fuel_consm,
							'Maximum minutes able to fly': max_min_fly							}
			return JsonResponse(responseData)
		else:			
			return Response({"Success": "Please insert the data for 10 airplanes"}, status=status.HTTP_200_OK)





    