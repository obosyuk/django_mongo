from rest_framework import serializers
from .repositories import get_concrete_models

Author, Post = get_concrete_models()


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    biography = serializers.CharField()
    date_of_birth = serializers.DateField()

    def create(self, validated_data):
        return Author(**validated_data).save()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.biography = validated_data.get('biography', instance.biography)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Post
        fields = ['id', 'title', 'content', 'author', 'publication_date']
