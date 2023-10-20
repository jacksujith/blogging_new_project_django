from django.urls import path
from .views import HomeView,AddCategoryView, ArticleDetailsView, AddPostView, UpdatePostView, LikeView,DeletePostView,CategoryView,CategoryListView

urlpatterns = [
     path('', HomeView.as_view(), name="home"),
     path('article/<int:pk>',ArticleDetailsView.as_view(), name='article-details'),
     path('add_post/', AddPostView.as_view(), name="add_post"),
     path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
     path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
     path('add_category/', AddCategoryView.as_view(), name="add_category"),
     path('category/<str:cats>/',CategoryView,name="category"),
     path('category-list/',CategoryListView,name="category-list"),
     path('like/<int:pk>', LikeView, name='like_post'),
   

]
