from rest_framework import serializers
from blog.models import Post


class LeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
