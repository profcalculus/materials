import logging

logger = logging.getLogger(__name__)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import logging

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ToDoItem, ToDoList


# class IndexView(ListView):
#     model = ToDoList
#     template_name = "todo_list/index.html"


# List of todo lists. Each list title is linked to a list.
class MultiListView(ListView):
    model = ToDoList
    template_name = "todo_list/todo_lists.html"


# list of todo items. Each item title links to an item detail view
class SingleListView(ListView):
    model = ToDoItem
    template_name = "todo_list/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super(SingleListView, self).get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


# class ItemDetailView(DetailView):
# model = ToDoItem
# template_name = "todo_list/item_detail.html"


class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context


# class ListUpdate(UpdateView):
#     model=ToDoList
#     fields = ['title']


class ListDelete(DeleteView):
    model = ToDoList
    # We have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("lists")


# class ItemsView(ListView):
#     model = ToDoItem


class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "created_date",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


#  def get_initial(self):
#     initial = super(ItemCreate,self).get_initial()
#     initial["todo_list_id"] =self.kwargs["list_id"]
#     return initial


class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "created_date",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super(ItemDelete, self).get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
