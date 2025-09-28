from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        abstract = True
        exclude = ['uuid']
        fields = ['id', 'created_at', 'updated_at']