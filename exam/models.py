from django.db import models

# Create your models here.

class Lac(models.Model):
	name=models.CharField(max_length=100)
	job_position=models.CharField(max_length=100)
	department=models.CharField(max_length=100)
	campus=models.CharField(max_length=100)
	type=models.CharField(max_length=100)
	ict_id=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return "Name : %s Job Position : %s Department : %s Campus : %s type: %s ICT ID : %s "%(self.name,self.job_position,self.department,self.campus,self.type,self.ict_id)
	class Meta:
		ordering = ['id']


	
