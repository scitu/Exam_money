from django.template.loader import get_template
from django.db import DatabaseError, transaction
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from exam.models import Lac 
import json
import ast
import io

def jo(request):
	data ='static/scidb_staff.json'
	with open(data, 'r', encoding="utf-8") as fp:
		data = json.load(fp)
		#print(data)
		print(type(data[1]))
		print(data[1])
		for d in data:
			print(d)
			with transaction.atomic():
				Lac.objects.update_or_create(**d)
		# for i in len(data):
			# o = Lac.objects.update_or_create(data)
		return HttpResponse("Success")
def test(request):
    return render(request,'test.html')
def login(request):
    return render(request,'login.html')
def form(request):
    return render(request,'form2.html')
def logout(request):
    return render(request,'form2.html')
def home(request):
    return render(request,'form2.html')
