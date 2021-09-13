from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("nube/users/list",views.ListUserAPIView.as_view(),name="user_list"),
    path("nube/users/create/", views.CreateUserAPIView.as_view(),name="user_create"),
    path("nube/users/update/<int:pk>/",views.UpdateUserAPIView.as_view(),name="update_user"),
    path("nube/users/delete/<int:pk>/",views.DeleteUserAPIView.as_view(),name="delete_user")
]
