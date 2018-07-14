from django.conf.urls import url, include

from blog import views
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import PostViewSet, UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
app_name = 'blog'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'category', views.CategoryViewSet)

API_TITLE = 'Pastebin API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    # url(r'^search/$', views.search, name='search'),

    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),

]












# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^posts/$', views.PostList.as_view(), name='post-list'),
#     url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
#     url(r'^posts/(?P<pk>[0-9]+)/highlight/$', views.PostHighlight.as_view(), name='post-highlight'),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ])
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

#
# post_list = PostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# post_detail = PostViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# post_highlight = PostViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^posts/$', post_list, name='post-list'),
#     url(r'^posts/(?P<pk>[0-9]+)/$', post_detail, name='post-detail'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
#     url(r'^posts/(?P<pk>[0-9]+)/highlight/$', post_highlight, name='post-highlight'),
#
# ])