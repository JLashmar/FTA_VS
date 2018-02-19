from rest_framework import serializers
from articles.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'post_category',
            'team_a',
            'team_b',
            'short_description',
            'body',
            'headline_image',
            'headline_image_credit',
            'post_image',
            'post_image_credit',
            'youtube_link',
            'team_b',
            'country_slug',
            'posted')
