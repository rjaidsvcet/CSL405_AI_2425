from rest_framework.serializers import ModelSerializer
from modelApp.models import Firstname

class FirstnameSerializer (ModelSerializer):
    class Meta:
        model = Firstname
        fields = '__all__'