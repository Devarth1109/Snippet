from rest_framework import serializers
from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model=Snippet
		fields=['id','Title','Code','Lineos',"Language","Style"]


