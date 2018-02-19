from rest_framework import serializers
from teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'sport',
            'nation',
            'team_name',
            'gender',
            'tier',
            )
