from rest_framework import mixins, generics
from articles.models import Post
from .serializers import PostSerializer


class PostAPIView(generics.ListCreateAPIView):  # create view
    queryset = Post.objects.all()
    lookup_field = "pk"
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRudView(generics.RetrieveUpdateDestroyAPIView):  # detail view
    lookup_field = "pk"
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()