from rest_framework import mixins, generics
from teams.models import Team
from .serializers import TeamSerializer


class TeamAPIView(generics.ListCreateAPIView):  # create view
    queryset = Team.objects.all()
    lookup_field = "pk"
    serializer_class = TeamSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TeamRudView(generics.RetrieveUpdateDestroyAPIView):  # detail view
    lookup_field = "pk"
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()