from rest_framework import serializers
from .models import Profile, Tag, Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'name', 'website', 'bio']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer()  # Nested serializer for author
    tags = TagSerializer(many=True)  # Nested serializer for tags

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'subtitle', 'slug', 'body',
            'meta_description', 'date_created', 'date_modified',
            'publish_date', 'published', 'author', 'tags'
        ]

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        author_data = validated_data.pop('author')
        
        author, created = Profile.objects.get_or_create(**author_data)
        post = Post.objects.create(author=author, **validated_data)

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)

        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        author_data = validated_data.pop('author', None)

        if author_data:
            author, created = Profile.objects.get_or_create(**author_data)
            instance.author = author

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if tags_data is not None:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(**tag_data)
                instance.tags.add(tag)

        instance.save()
        return instance
