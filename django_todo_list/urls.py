from . import views

urlpatterns = [
    path("", views.index, name="ToDoLists"),
    paths("item-detail", views.item),
]
