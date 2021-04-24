from django.urls import path
# from . import views
from .views import AddCategoryView, AddCommentView, AddPostView, CategoryListView, DeleteCommentView, DeletePostView, HomeView , ArticleDetailView, UpdatePostView, CategoryView, LikeView

urlpatterns = [
    # path('',views.home, name='home'),
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='articleDetail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='edit_post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(), name='delete_post'),
    path('add_category/',AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/',CategoryView, name='category'),
    path('category-list/',CategoryListView, name='category-list'),
    path('like/<int:pk>',LikeView, name='like_post'),
    path('article/<int:pk>/comment/',AddCommentView.as_view(), name='add_comment'),
    path('article/comment/<int:pk>/delete',DeleteCommentView.as_view(), name='delete_comment'),
]
