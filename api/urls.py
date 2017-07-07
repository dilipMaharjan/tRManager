from django.conf.urls import url

from api.views import PostListAPIView, PostDetailAPIView, PostCreateAPIView, PostDeleteAPIView, \
    PostUpdateAPIView

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name="list"),
    url(r'^(?P<title>[\w-]+)/$', PostDetailAPIView.as_view(), name="detail"),
    url(r'^create/$', PostCreateAPIView.as_view(), name="create"),
    url(r'^(?P<title>[\w-]+)/edit$', PostUpdateAPIView.as_view(), name="update"),
    url(r'^(?P<title>[\w-]+)/delete', PostDeleteAPIView.as_view(), name="delete"),
]
