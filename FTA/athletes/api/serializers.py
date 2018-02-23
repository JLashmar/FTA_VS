from rest_framework import serializers
from athletes.models import Athlete

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = (
            'first_name',
            'last_name',
            'initials',
            'nationality',
            'sport'
            )
