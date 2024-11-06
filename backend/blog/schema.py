import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from datetime import datetime
from graphene import Mutation
from django.db import transaction

from blog import models
from blog.models import Post, Profile, Tag
from django.utils.text import slugify



class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )
     
     
    current_user = graphene.Field(AuthorType)  # Define a query to get a static current user

    def resolve_current_user(self, info):
        # Return a "dummy" user profile for demonstration purposes
        # You can hardcode the values here as needed
        dummy_user = models.Profile(
            id=1,
            name="Test user",
            bio="This is a bio for an Example User.",
            website="https://www.johndoe.com"
        )
        return dummy_user

class TagInput(graphene.InputObjectType):
    name = graphene.String(required=True)

class CreatePostInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    body = graphene.String(required=True)
    author_id = graphene.ID(required=True)
    tags = graphene.List(TagInput)




class CreatePost(graphene.Mutation):
    class Arguments:
        input = CreatePostInput(required=True)

    post = graphene.Field(PostType)  # Define PostType to return the created post
    errors = graphene.List(graphene.String)

    def mutate(self, info, input):
        # Extract the data from the input
        title = input.title
        body = input.body
        author_id = input.author_id
        tags = input.tags

        # Find the author profile
        author = Profile.objects.get(id=author_id)

        # Create the post instance
        post = Post(
            title=title,
            body=body,
            author=author,
            slug=slugify(title),  # Create slug from title
            published=False
        )
        post.save()

        # Handle tags
        if tags:
            for tag_input in tags:
                tag, created = Tag.objects.get_or_create(name=tag_input.name)
                post.tags.add(tag)

        post.save()

        return CreatePost(post=post, errors=None)  # Return errors as well if needed


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()  # Use Field to define the mutation

        
        
schema = graphene.Schema(query=Query, mutation=Mutation)