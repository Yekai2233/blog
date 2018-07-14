from blog.models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import permissions


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:category-detail',
    )
    post = serializers.HyperlinkedRelatedField(many=True, view_name='blog:post-detail', read_only=True)

    class Meta:
        model = Category
        fields = ('url', 'name', 'post')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    queryset = Post.objects.all()
    #category = serializers.SlugRelatedField(slug_field='id', read_only=True)
    category = CategorySerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:post-detail',
    )

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'views',
                  'author')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(many=True, view_name='blog:post-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:user-detail',
    )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'post')

