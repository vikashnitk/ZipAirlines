from rest_framework import serializers
from api.models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Airplane
		fields = ['id', 'passenger']