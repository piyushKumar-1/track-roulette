from rest_framework import serializers


from .models import EntriesModel



class EntriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = EntriesModel
		fields = "__all__"

		
