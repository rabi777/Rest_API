from rest_framework import serializers
from web.models import *

class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ('first_name, last_name, student_id, level')
        fields = '__all__'
