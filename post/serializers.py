from rest_framework import serializers
from .models import Category, Tag, Post, Comment

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug',)


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content', 'author', 'category', 'tags','created_at', 'updated_at', 'status')


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author_email', 'content', 'created_at', 'parent_comment')
        

