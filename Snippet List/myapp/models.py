from django.db import models

# Create your models here.
class Snippet(models.Model):
	Title=models.CharField(max_length=100)
	Code=models.CharField(max_length=100)
	Lineos=models.BooleanField()
	Language=models.CharField(max_length=100)
	Style=models.CharField(max_length=100)

	def __str__(self):
		return self.Title