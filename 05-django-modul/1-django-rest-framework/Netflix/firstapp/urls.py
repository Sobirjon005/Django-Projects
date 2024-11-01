from django.urls import path, include
from .views import MovieViewSet
from .views import AddCommentView, CommentListView, DeleteCommentView
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, ActorViewSet, MovieActorAPIView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'actors', ActorViewSet)

urlpatterns = [
    # path('movies/', MovieAPIView.as_view(), name='movie'),
    # path('actor/', ActorAPIView.as_view(), name='actor'),
    path('comments/add/', AddCommentView.as_view(), name='add-comment'),
    path('comments/list/', CommentListView.as_view(), name='list-comments'),
    path('comments/delete/<int:id>/', DeleteCommentView.as_view(), name='delete-comment'),
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors')
]
