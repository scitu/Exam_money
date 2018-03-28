from exam.models import Lac
from rest_framework import serializers
'''
class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('first_name','last_name','phone')
		#fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Car
		fields = ('model','detail','price',)

class RentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rent
		fields = ('car','customer','start','stop')
		'''
class LacSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lac
		fields = ('name','job_position','department','campus','type','ict_id')
		#fields = '__all__'


