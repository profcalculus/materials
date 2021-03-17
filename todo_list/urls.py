from django.urls import path
from . import views

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.MultiListView.as_view(), name="lists"),
    path("lists/", views.MultiListView.as_view(), name="lists"),
    path("list/<int:list_id>/", views.SingleListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    # CRUD patterns for ToDoItems
    path("list/<int:list_id>/item/add/", views.ItemCreate.as_view(), name="item-add"),
    path(
        "list/<int:list_id>/item/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="item-delete",
    ),
]
