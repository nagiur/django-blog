
from django.urls import path
from .views import PostListView, detail

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:id>/', detail, name='detail'),
]



