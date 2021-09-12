from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path("users/list",views.ListUserAPIView.as_view(),name="user_list"),
    path("users/create/", views.CreateUserAPIView.as_view(),name="user_create"),
    path("users/update/<int:pk>/",views.UpdateUserAPIView.as_view(),name="update_user"),
    path("users/delete/<int:pk>/",views.DeleteUserAPIView.as_view(),name="delete_user")
]
